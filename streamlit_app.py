import streamlit as st

st.set_page_config(
    page_title="Ziggy AI",
    page_icon="🤖",
    layout="wide"
)

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

    # Show user message
    st.chat_message("user").markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Temporary AI response
    response = "Hello! Gemini will answer here after we connect the API."

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )