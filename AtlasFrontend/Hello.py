import streamlit as st
from PIL import Image
import base64

# Function to load the image from the file system
def load_image(image_file):
    img = Image.open(image_file)
    return img

# Set the page configuration for the landing page
st.set_page_config(
    page_title="Diet Recommendation System",
    page_icon="👋",
)

# Load and display the logo
logo = load_image('logo.png')
st.image(logo, width=300)

# Introduction to the Diet Recommendation System
st.title("Welcome to Atlad SmartEat! 👋")
st.subheader("Your Personalized Nutrition Guide")
st.markdown(
    """
    The **Diet Recommendation System** is a cutting-edge platform that leverages a content-based approach
    with Scikit-Learn, FastAPI, and Streamlit to deliver tailored diet plans. Designed for health-conscious
    individuals and fitness enthusiasts, our system provides diet recommendations based on your unique health
    profile and preferences.

    - **Personalized Experience:** Receive diet plans that match your health goals and dietary restrictions.
    - **Data-Driven Insights:** Utilize the power of machine learning to make informed food choices.
    - **User-Friendly Interface:** Navigate through the application with ease and access your recommendations quickly.

    Get started by selecting a recommendation app from the sidebar, and embark on your journey to a healthier lifestyle!

    For more details about the project and to view the source code, visit the GitHub [repository](https://github.com/hadryyassine/Atlas-SmartEat).
    """
)

# Sidebar navigation
st.sidebar.success("Select a recommendation app.")
st.sidebar.info(
    "Choose between Automatic Diet Recommendation, Custom Food Recommendation to begin or an Assistant Diet"
)


