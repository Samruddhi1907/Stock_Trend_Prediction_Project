import streamlit as st
def show_home_page():
    """
    Displays the home page content.
    """
    # Welcome message and app description
    st.write("***Welcome to the Stock Trend Prediction Web App! This app allows you to...***")
    st.markdown("""
    * Analyze historical stock data to identify trends.
    * Predict future stock trends.
    """)
    # Navigation links to other pages
    st.subheader("Explore the App")
    with st.expander("See More"):
        st.write("Click on the options in the sidebar to navigate to different sections:")
        st.markdown("""
        * **Data Exploration:** Analyze historical stock data and visualize trends.
        * **Model Prediction:** Use a machine learning model to predict future trends.
        """)