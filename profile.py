import streamlit as st

def main():
    # Create two columns with custom width ratios
    col1, col3, col2 = st.columns(3)  # Make column 1 wider than column 2

    # Content for Column 1
    with col1:
        # Display the profile name
        st.header('Rafiul Nakib')

        # Display profile picture with adjusted width
        profile_image_url = '1721265225364.jpeg'  # Replace with actual image URL or path
        st.image(profile_image_url, use_column_width=True)


    # Content for Column 2
    with col2:
        # Display 'About Me' section
        st.header('About Me')
        st.write('Just a curious cat in superposition!')

        # Display 'Contact Information' section
        st.header('Contact Information')
        st.write('📧 Email: rafiul.nakib@mastermosh.ai')
        st.write('📞 WhatsApp: +61466620817')
        # Display 'Interests' section
        st.header('Interests')
        st.write('- Mathematics')
        st.write('- Physics')
        st.write('- Artificial Intelligence')

        # Display 'Education' section
        st.header('Education')
        st.write('- Master in Data Science, University of Sydney')
        st.write('- Bachelor of Science (Physics), University of Sydney')

        # Display 'Skills' section
        st.header('Skills')
        st.write('- Problem Solving')
        st.write('- Teaching and Mentoring')
        st.write('- Research and Development')
