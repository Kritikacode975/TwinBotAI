from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get responses from Gemini
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo", layout="centered")

st.title("Gemini LLM Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat history at the top
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.markdown(f"**{role}:** {text}")

# Input section at the bottom
with st.container():
    input_text = st.text_input("Your Message:", key="input", placeholder="Type your question here...")
    if st.button("Submit", key="submit"):
        if input_text.strip():  # Ensure input is not empty
            # Add user query to chat history
            st.session_state['chat_history'].append(("You", input_text))
            # Get response from Gemini
            response = get_gemini_response(input_text)
            # Stream Gemini's response and add to chat history
            for chunk in response:
                st.session_state['chat_history'].append(("Bot", chunk.text))
            # Clear the input field
            # st.experimental_rerun()
