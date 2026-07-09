import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit.components.v1 as components
from datetime import datetime

# -----------------------------
# Load Gemini API
# -----------------------------
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found. Check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Ziggy AI",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🤖 Ziggy AI")

    st.markdown("---")

    if st.button("🆕 New Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.subheader("About")

    st.write("""
Welcome to **Ziggy AI**!

Your professional AI assistant powered by Google's Gemini.

Version **1.0**
""")


# -----------------------------
# Main Header
# -----------------------------
col1, col2 = st.columns([1, 6])

with col1:
    st.image("assets/logo.png", width=80)

with col2:
    st.title("Ziggy AI")
    st.caption("Build • Learn • Create")


# -----------------------------
# Welcome Screen
# -----------------------------
if len(st.session_state.messages) == 0:

    st.markdown("""
# 👋 Welcome to Ziggy AI

### Your Personal AI Assistant

Ask me anything about:

- 🤖 Artificial Intelligence
- 💻 Programming
- 🐍 Python
- 📊 Machine Learning
- 🚀 Career Guidance

---

💡 **Try asking:**

- What is Artificial Intelligence?
- Explain Machine Learning.
- Help me write Python code.
- Teach me Git and GitHub.

---

✨ Ziggy AI can help you learn, create, and explore new ideas.
""")
# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:

    avatar = "👤" if message["role"] == "user" else "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])
        st.caption(f"🕒 {message['time']}")


# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask me anything...")


if prompt:

    current_time = datetime.now().strftime("%I:%M %p")

    # Display User Message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        st.caption(f"🕒 {current_time}")

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
            "time": current_time
        }
    )

    system_prompt = f"""
You are Ziggy AI.

You are a friendly professional AI assistant.

Rules:
- Greet users briefly.
- Reply politely.
- Explain AI, Python and programming clearly.
- Keep answers concise unless asked for details.
- Never say you are Gemini.
- Always introduce yourself as Ziggy AI.

User:
{prompt}
"""

    # -----------------------------
    # AI Response
    # -----------------------------
    try:

        with st.chat_message("assistant", avatar="🤖"):

            with st.spinner("🤖 Ziggy is thinking..."):

                response = model.generate_content(system_prompt)

                ai_response = response.text

                ai_time = datetime.now().strftime("%I:%M %p")

                st.markdown(ai_response)
                st.caption(f"🕒 {ai_time}")

                # Copy Button
                components.html(
                    f"""
                    <button onclick="
                    navigator.clipboard.writeText(`{ai_response}`);
                    this.innerHTML='✅ Copied!';
                    ">
                    📋 Copy Response
                    </button>
                    """,
                    height=50,
                )

        # Save AI Message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_response,
                "time": ai_time
            }
        )

    except Exception as e:

        st.error(
            "⚠️ Ziggy AI is temporarily unavailable or the API quota has been exceeded."
        )

