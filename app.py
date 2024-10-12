import streamlit as st
from streamlit_option_menu import option_menu
import mathematics  # Your lesson module
import physics
import biology
import profile  # Import the profile module
import friends  # Import the friends module

# Set the page configuration
st.set_page_config(page_title="MastermoshAI", page_icon=":books:", layout="wide")

# Hide the default Streamlit header and footer (optional)
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Define the logo HTML
logo_html = """
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="
            font-family: 'Arial Black', Gadget, sans-serif;
            color: #1E90FF; /* Updated color: Dodger Blue */
            text-shadow: 2px 2px #000000;
        ">
            MastermoshAI
        </h1>
    </div>
    """

# Add a dark background for the header and navigation
header_style = """
    <style>
    .header-container {
        background-color: #333333;
        padding: 20px;
    }
    </style>
    """

st.markdown(header_style, unsafe_allow_html=True)

# Create a container for the logo and navigation
with st.container():
    # Display the logo
    st.markdown(logo_html, unsafe_allow_html=True)
    
    # Create the main navigation menu with the new tabs
    selected = option_menu(
        menu_title=None,
        options=["Home", "Profile", "Friends", "Study"],
        icons=["house", "person", "people", "book"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#333"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "center",
                "margin": "0px",
                "color": "white",
                "padding": "10px 12px",
                "background-color": "#333",
            },
            "nav-link-selected": {"background-color": "#555"},
        },
    )

# Handle navigation logic
if selected == "Home":
    # st.title('Welcome to MastermoshAI')

    # Generate 25 dummy activity records
    import random
    from datetime import datetime, timedelta

    # List of friends with names and profile images (same as in friends.py)
    friends_list = [
        {'name': 'Alice Smith', 'profile_image': 'https://picsum.photos/id/1/75'},
        {'name': 'Bob Johnson', 'profile_image': 'https://picsum.photos/id/2/75'},
        {'name': 'Carol Williams', 'profile_image': 'https://picsum.photos/id/12/75'},
        {'name': 'David Brown', 'profile_image': 'https://picsum.photos/id/13/75'},
        {'name': 'Emma Jones', 'profile_image': 'https://picsum.photos/id/23/75'},
        {'name': 'Frank Miller', 'profile_image': 'https://picsum.photos/id/534/75'},
        {'name': 'Grace Davis', 'profile_image': 'https://picsum.photos/id/121/75'},
        {'name': 'Henry Wilson', 'profile_image': 'https://picsum.photos/id/154/75'},
        {'name': 'Isabel Taylor', 'profile_image': 'https://picsum.photos/id/123/75'},
        {'name': 'Jack Anderson', 'profile_image': 'https://picsum.photos/id/178/75'},
        {'name': 'Karen Thomas', 'profile_image': 'https://picsum.photos/id/156/75'},
        {'name': 'Liam Jackson', 'profile_image': 'https://picsum.photos/id/154/75'},
        {'name': 'Mia White', 'profile_image': 'https://picsum.photos/id/166/75'},
        {'name': 'Noah Harris', 'profile_image': 'https://picsum.photos/id/15/75'},
        {'name': 'Olivia Martin', 'profile_image': 'https://picsum.photos/id/13/75'},
        {'name': 'Peter Thompson', 'profile_image': 'https://picsum.photos/id/157/75'},
        {'name': 'Quinn Garcia', 'profile_image': 'https://picsum.photos/id/199/75'},
        {'name': 'Rachel Martinez', 'profile_image': 'https://picsum.photos/id/142/75'},
        {'name': 'Samuel Robinson', 'profile_image': 'https://picsum.photos/id/18/75'},
        {'name': 'Tina Clark', 'profile_image': 'https://picsum.photos/id/75/75'},
    ]

    # List of possible activities
    activities = [
        'completed Lesson 1',
        'completed Lesson 2',
        'took Quiz 1',
        'took Quiz 2',
        'achieved a high score of 95%',
        'achieved a score of 85%',
        'spent 2 hours studying',
        'spent 30 minutes studying',
        'made a new friend',
        'started following you',
        'commented on your post',
        'shared a new resource',
        'updated their profile picture',
        'joined the group "Advanced Mathematics"',
        'posted a new article',
        'liked your post',
        'earned a badge for "Consistent Learner"',
        'asked a question in the forum',
        'answered a question in the forum',
        'started a new discussion',
    ]

    # Generate 25 activity records
    activity_feed = []
    for _ in range(25):
        friend = random.choice(friends_list)
        activity = random.choice(activities)
        # Generate a random timestamp within the last 7 days
        time_delta = timedelta(days=random.randint(0, 7), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        timestamp = datetime.now() - time_delta
        timestamp_str = timestamp.strftime('%b %d at %I:%M %p')
        activity_feed.append({
            'friend': friend,
            'activity': activity,
            'timestamp': timestamp_str
        })

    # Sort the activity feed by timestamp (most recent first)
    activity_feed.sort(key=lambda x: x['timestamp'], reverse=True)

    # Display the activity feed
    for activity in activity_feed:
        friend = activity['friend']
        activity_text = f"**{friend['name']}** {activity['activity']} - *{activity['timestamp']}*"
        # Create a container for each activity
        with st.container():
            cols = st.columns([1, 8])  # Adjust column widths as needed
            with cols[0]:
                st.image(friend['profile_image'], width=50)
            with cols[1]:
                st.write(activity_text)

elif selected == "Profile":
    profile.main()  # Call the main function from profile.py

elif selected == "Friends":
    friends.main()  # Call the main function from friends.py

elif selected == "Study":
    # Create a submenu for Study with styles matching the main navigation menu
    lesson_selected = option_menu(
        menu_title=None,
        options=["Mathematics", "Physics", "Biology"],
        icons=["book", "book", "book"],
        menu_icon=None,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#333"},
            "icon": {"color": "white", "font-size": "0px"},  # Hide icons to reduce space
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "color": "white",
                "padding": "7px 8px",
                "background-color": "#333",
            },
            "nav-link-selected": {"background-color": "#555"},
        },
    )
    if lesson_selected == "Mathematics":
        mathematics.main()
    elif lesson_selected == "Physics":
        physics.main()
    elif lesson_selected == "Biology":
        biology.main()
