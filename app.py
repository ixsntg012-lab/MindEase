import streamlit as st
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append('utils')

from rag_pipeline import initialize, get_response

st.set_page_config(
    page_title="MindEase — Mental Health Support",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.chat-message-user {
    background: #1e3a5f;
    padding: 12px 16px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0;
    color: white;
    text-align: right;
}
.chat-message-bot {
    background: #1a2e1a;
    padding: 12px 16px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px 0;
    color: white;
}

/* Quick topic buttons ki custom style */
.stButton button {
    border-radius: 20px;
    border: 1px solid #4ADE80;
    background-color: transparent;
    color: #4ADE80;
    transition: all 0.3s ease;
}
.stButton button:hover {
    background-color: #4ADE80;
    color: #0E1117;
    transform: scale(1.05);
}

/* Title ki custom gradient */
h1 {
    background: linear-gradient(90deg, #4ADE80, #22D3EE);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

/* Disclaimer box ki custom border */
.stAlert {
    border-left: 4px solid #F59E0B;
    border-radius: 8px;
}

/* Chat input box ki custom style */
.stChatInput {
    border-radius: 24px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🧠 MindEase")
st.markdown("**Your compassionate AI mental health support companion**")
st.markdown("*Anonymous · Judgment-free · Available 24/7*")

st.info("⚠️ MindEase is an AI support tool, not a replacement for professional mental health care. If you are in crisis, please call **988** immediately.")

st.markdown("---")

# Initialize RAG pipeline
@st.cache_resource
def load_pipeline():
    with st.spinner("Loading MindEase..."):
        collection, groq_client = initialize()
    return collection, groq_client

collection, groq_client = load_pipeline()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I'm MindEase, your compassionate AI support companion. 💚\n\nThis is a safe, anonymous space to share what's on your mind. How are you feeling today?"
    })

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-message-user">👤 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message-bot">🧠 {msg["content"]}</div>', unsafe_allow_html=True)

st.markdown("---")

# Quick topic buttons
st.markdown("**Quick topics:**")
cols = st.columns(4)
topics = ["😰 Anxiety", "😔 Depression", "😴 Sleep", "😤 Stress"]
for i, topic in enumerate(topics):
    if cols[i].button(topic, use_container_width=True):
        st.session_state.quick_topic = topic.split(" ", 1)[1]
        st.rerun()

# Handle quick topic
if "quick_topic" in st.session_state:
    user_input = f"I need help with {st.session_state.quick_topic}"
    del st.session_state.quick_topic
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    response, is_crisis = get_response(collection, groq_client, user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# Text input
user_input = st.chat_input("Share what's on your mind...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("MindEase is thinking..."):
        response, is_crisis = get_response(collection, groq_client, user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    if is_crisis:
        st.error("🆘 Crisis resources have been shared above. Please reach out for help immediately.")
    
    st.rerun()

# Footer
st.markdown("---")
st.caption("MindEase — Built with ChromaDB, Groq AI & Streamlit | For educational purposes only")
st.caption("Crisis support: **988** (call/text) | Emergency: **911**")