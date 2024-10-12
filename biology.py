import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import logging
import streamlit as st

load_dotenv()
client = OpenAI()

ass_id = "asst_BJwfKr5czXKwSWYsaVnsF8ox"

def main():
    # Initialize session state
    if "file_id_list" not in st.session_state:
        st.session_state.file_id_list = []
    if "start_chat" not in st.session_state:
        st.session_state.start_chat = False
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = None

    # Removed the button from the sidebar and will place it in col2

    # Function to process messages with citations and handle long responses
    def process_message_with_citations(message):
        message_content = message.content[0].text
        annotations = (
            message_content.annotations if hasattr(message_content, "annotations") else []
        )
        citations = []

        for index, annotation in enumerate(annotations):
            message_content.value = message_content.value.replace(
                annotation.text, f" [{index + 1}]"
            )
            if file_citation := getattr(annotation, "file_citation", None):
                cited_file = client.files.retrieve(file_citation.file_id)
                citations.append(
                    f'[{index + 1}] from {cited_file.filename}'
                )

        full_response = message_content.value + "\n\n" + "\n".join(citations)
        max_chunk_size = 2000
        chunks = [full_response[i:i+max_chunk_size] for i in range(0, len(full_response), max_chunk_size)]

        return chunks

    # Function to handle run status with timeout and error handling
    def wait_for_run_completion(thread_id, run_id, timeout=60, poll_interval=1):
        start_time = time.time()
        while time.time() - start_time < timeout:
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id, run_id=run_id
            )
            if run.status == "completed":
                return run
            elif run.status == "failed":
                st.error("Something went wrong! Please try again.")
                logging.error(f"Run failed with ID: {run_id}")
                return None
            time.sleep(poll_interval)

        st.error("Request timed out. Please try again later.")
        logging.error(f"Run timed out after {timeout} seconds.")
        return None

    # Main interface
    st.title("Lesson 1 - MastermoshAI")

    # Create two columns: left for video, right for chat
    col1, col2 = st.columns([7, 3])  # Adjust the width ratios as needed

    with col1:
        # Video section on the left
        video_file = open('IMG_4257.MOV', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    with col2:
        # Moved the "Ask anything about the lesson" button here
        if st.button("Ask anything about the lesson"):
            if st.session_state.file_id_list:
                st.session_state.start_chat = True
                chat_thread = client.beta.threads.create()
                st.session_state.thread_id = chat_thread.id
            else:
                st.session_state.start_chat = True
                if not st.session_state.thread_id:
                    chat_thread = client.beta.threads.create()
                    st.session_state.thread_id = chat_thread.id
                    st.write("Thread ID:", chat_thread.id)

        # Chat session
        if st.session_state.start_chat:
            if "openai_model" not in st.session_state:
                st.session_state.openai_model = "gpt-4o-mini"
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Display existing messages
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            # Chat input for user
            if prompt := st.chat_input("Ask"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                client.beta.threads.messages.create(
                    thread_id=st.session_state.thread_id, role="user", content=prompt
                )

                # Create a run with additional instructions
                run = client.beta.threads.runs.create(
                    thread_id=st.session_state.thread_id,
                    assistant_id=ass_id,
                    instructions="""You are a helpful tutor. However, you only and only answer questions related to Pythagorean theorem, and nothing else.

                                Writing math formulas:
                                Start all mathematical equations with the $ delimiters, no exception.
                                For every single mathematical equation, use a new line.
                                You have a MathJax render environment.
                                - Any LaTeX text between single dollar sign ($) will be rendered as a TeX formula; no exception.
                                - Use $(tex_formula)$ in-line delimiters to display equations instead of backslash; no exception.
                                - The render environment only uses $ (single dollarsign) as a container delimiter, never output $$, no exception.

                                Example: $x^2 + 3x$ is output for "x² + 3x" to appear as TeX.

                                PHYSICAL AND MATHEMATICAL UNITS SHOULD ALWAYS BE IN ENGLISH.""",
                )

                with st.spinner("Please wait a bit..."):
                    run = wait_for_run_completion(
                        thread_id=st.session_state.thread_id, run_id=run.id, timeout=60
                    )

                    if run:
                        messages = client.beta.threads.messages.list(
                            thread_id=st.session_state.thread_id
                        )
                        assistant_messages_for_run = [
                            message
                            for message in messages
                            if message.run_id == run.id and message.role == "assistant"
                        ]

                        for message in assistant_messages_for_run:
                            response_chunks = process_message_with_citations(message=message)
                            for chunk in response_chunks:
                                st.session_state.messages.append(
                                    {"role": "assistant", "content": chunk}
                                )
                                with st.chat_message("assistant"):
                                    st.markdown(chunk, unsafe_allow_html=True)
