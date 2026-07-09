import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page configuration
st.set_page_config(
    page_title="Ziggy AI",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Ziggy AI")
st.caption("Your Professional AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Ziggy is thinking..."):
            response = model.generate_content(prompt)
            ai_response = response.text
            st.markdown(ai_response)

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )