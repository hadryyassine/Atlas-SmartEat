import openai
import streamlit as st

# Set the page config for the chatbot page
st.set_page_config(page_title="Diet Assistant Chatbot", page_icon="🤖", layout="wide")

# Function to call the OpenAI API and get the response
def ask_gpt(prompt, user_info):
    # Construct context with user information
    context = f"Age: {user_info['age']}, Gender: {user_info['gender']}, " \
              f"Weight: {user_info['weight']}, Height: {user_info['height']}, " \
              f"Activity Level: {user_info['activity_level']}, " \
              f"Meals per day: {user_info['meals_per_day']}, " \
              f"Health Issues: {user_info['health_issues']}, Vegan: {user_info['vegan']}."

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": context}, {"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

# Ensure that the OpenAI API key is set in your environment variables before running the app
openai_api_key = st.sidebar.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

if not openai_api_key:
    st.error("OpenAI API key not found. Please enter your API key in the sidebar.")
    st.stop()

# Set the API key for your session
openai.api_key = openai_api_key
# Collect user information
with st.form("user_info_form"):
    age = st.number_input('Age', min_value=12, max_value=120)
    gender = st.radio("Gender", options=['Male', 'Female', 'Other'])
    weight = st.number_input('Weight (kg)', min_value=30.0, max_value=200.0)
    height = st.number_input('Height (cm)', min_value=100.0, max_value=250.0)
    activity_level = st.selectbox("Activity Level", options=["Sedentary", "Active", "Very Active"])
    meals_per_day = st.select_slider("Meals per day", options=[1, 2, 3, 4, 5])
    health_issues = st.text_input("Health issues (comma-separated)")
    vegan = st.checkbox("Vegan")
    user_info_submitted = st.form_submit_button("Submit")

# Save user information in session state for use in chat responses
if user_info_submitted:
    st.session_state.user_info = {
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "activity_level": activity_level,
        "meals_per_day": meals_per_day,
        "health_issues": health_issues,
        "vegan": vegan
    }

# Chat interface
st.header("Chat with our Diet Assistant")
user_prompt = st.text_input("Ask me anything about diet and nutrition:")

if st.button("Send"):
    if user_prompt and 'user_info' in st.session_state:
        gpt_response = ask_gpt(user_prompt, st.session_state.user_info)
        st.write(gpt_response)
    else:
        st.write("Please submit your information above before chatting.")