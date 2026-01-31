import streamlit as st
from huggingface_hub import InferenceClient
import json
import os
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

# 2. Personality Configuration
personalities = {
    "Kelly": {
        "description": "Empathic, soft-spoken, and comforting.",
        "system_message": "You are Kelly, a comforting and empathic wellness assistant. Speak softly and kindly.",
        "file": "history_kelly.json"
    },
    "Hannah": {
        "description": "Structured, practical, and advice-oriented.",
        "system_message": "You are Hannah, a practical and grounded mentor. Provide structured advice and clear steps.",
        "file": "history_hannah.json"
    },
    "Darbie": {
        "description": "Cheerful, witty, and lighthearted.",
        "system_message": "You are Darbie, a cheerful and witty companion. Use humor and positive energy.",
        "file": "history_darbie.json"
    }
}

# 3. Helper Functions
def load_history(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_history(messages, filename):
    with open(filename, "w") as f:
        json.dump(messages, f)

# 4. Streamlit UI Setup
st.set_page_config(page_title="Kokoro Assistant", page_icon="🌸")
st.title("🌸 Kokoro AI Companion")

# Personality Selector
choice = st.sidebar.selectbox("Choose your companion:", list(personalities.keys()))
current_bot = personalities[choice]
st.sidebar.write(f"**Current Personality:** {current_bot['description']}")

# Initialize Chat History for the specific bot
if "messages" not in st.session_state or st.sidebar.button("Clear Conversation"):
    st.session_state.messages = load_history(current_bot["file"])
    if not st.session_state.messages:
        st.session_state.messages = [{"role": "system", "content": current_bot["system_message"]}]

# Display Chat History
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# 5. Chat Interaction Logic
if prompt := st.chat_input(f"Talk to {choice}..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # CRITICAL: Initialize bot_text as empty to prevent NameError
    bot_text = ""

    try:
        with st.chat_message("assistant"):
            # Call Hugging Face API
            response = client.chat_completion(
                model="meta-llama/Llama-3.2-3B-Instruct",
                messages=st.session_state.messages,
                max_tokens=500,
                stream=False
            )
            bot_text = response.choices[0].message.content
            st.markdown(bot_text)
        
        # Save to history ONLY if response was successful
        if bot_text:
            st.session_state.messages.append({"role": "assistant", "content": bot_text})
            save_history(st.session_state.messages, current_bot["file"])
            
    except Exception as e:
        st.error(f"⚠️ Connection Error: {e}. Please check your HF_TOKEN.")