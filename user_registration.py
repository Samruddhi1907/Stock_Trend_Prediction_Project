import streamlit as st
def show_user_registration_page():
    """
    Displays the user registration page.
    """
    st.title("User Registration")
    # Initialize session state variables
    if 'registered_users' not in st.session_state:
        st.session_state.registered_users = []
    # User input fields
    username = st.text_input("Username:")
    email = st.text_input("Email:")
    password = st.text_input("Password:", type = "password")
    confirm_password = st.text_input("Confirm Password:", type = "password")
    # Submit button and registration logic
    if st.button("Register"):
        if password == confirm_password:
            # Check if username already exists
            if username in st.session_state.registered_users:
                st.error("Username already exists. Please choose a different one.")
            else:
                # Store user data in session state (for demonstration)
                st.session_state.registered_users.append(username)
                st.success("Registration successful!")
                # Set registration successful flag
                st.session_state.registration_successful = True
        else:
            st.error("Passwords do not match!")
if __name__ == "__main__":
    show_user_registration_page()