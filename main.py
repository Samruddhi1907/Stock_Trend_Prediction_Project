import streamlit as st
# Import pages
import data_exploration, model_prediction, user_registration, home_page
# Set page title, icon, and layout
st.set_page_config(
    page_title="Stock Trend Prediction",
    page_icon="",
    layout="wide",
)
def main():
    """
    Defines the main app structure and navigation.
    - Shows User Registration initially.
    - Redirects to Home Page after successful registration.
    """
    # Check if user is registered (using session state)
    if 'registered' not in st.session_state:
        st.session_state.registered = False
    # Display logo 
    st.image("logo.png", width=200)
    # User Registration (displayed initially)
    if not st.session_state.registered:
        user_registration.show_user_registration_page()
        if st.session_state.get('registration_successful', False):
            st.session_state.registered = True
    else:
        # Navigation bar after successful registration
        st.title("Stock Trend Prediction")
        page_names = ["Home", "Data Exploration", "Model Prediction"]
        page = st.sidebar.selectbox("Select a page:", page_names)
        if page == "Home":
            home_page.show_home_page()
        elif page == "Data Exploration":
            data_exploration.show_data_exploration_page()
        elif page == "Model Prediction":
            processed_data = st.session_state.get('processed_data')
            model_prediction.show_model_prediction_page(processed_data)
if __name__ == "__main__":
    main()