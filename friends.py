import streamlit as st

def main():
    st.title('Your Friends')

    # Define a list of friends with dummy names and placeholder images
    friends = [
        {'name': 'Alice Smith', 'profile_image': 'https://picsum.photos/id/1/100'},
        {'name': 'Bob Johnson', 'profile_image': 'https://picsum.photos/id/2/100'},
        {'name': 'Carol Williams', 'profile_image': 'https://picsum.photos/id/12/100'},
        {'name': 'David Brown', 'profile_image': 'https://picsum.photos/id/13/100'},
        {'name': 'Emma Jones', 'profile_image': 'https://picsum.photos/id/23/100'},
        {'name': 'Frank Miller', 'profile_image': 'https://picsum.photos/id/534/100'},
        {'name': 'Grace Davis', 'profile_image': 'https://picsum.photos/id/121/100'},
        {'name': 'Henry Wilson', 'profile_image': 'https://picsum.photos/id/154/100'},
        {'name': 'Isabel Taylor', 'profile_image': 'https://picsum.photos/id/123/100'},
        {'name': 'Jack Anderson', 'profile_image': 'https://picsum.photos/id/178/100'},
        {'name': 'Karen Thomas', 'profile_image': 'https://picsum.photos/id/156/100'},
        {'name': 'Liam Jackson', 'profile_image': 'https://picsum.photos/id/154/100'},
        {'name': 'Mia White', 'profile_image': 'https://picsum.photos/id/166/100'},
        {'name': 'Noah Harris', 'profile_image': 'https://picsum.photos/id/15/100'},
        {'name': 'Olivia Martin', 'profile_image': 'https://picsum.photos/id/13/100'},
        {'name': 'Peter Thompson', 'profile_image': 'https://picsum.photos/id/157/100'},
        {'name': 'Quinn Garcia', 'profile_image': 'https://picsum.photos/id/199/100'},
        {'name': 'Rachel Martinez', 'profile_image': 'https://picsum.photos/id/142/100'},
        {'name': 'Samuel Robinson', 'profile_image': 'https://picsum.photos/id/18/100'},
        {'name': 'Tina Clark', 'profile_image': 'https://picsum.photos/id/100/100'},
    ]

    # Display friends in a grid format
    cols = st.columns(4)  # Adjust the number of columns as needed

    for index, friend in enumerate(friends):
        with cols[index % 4]:
            st.image(friend['profile_image'], width=100)
            st.write(friend['name'])
