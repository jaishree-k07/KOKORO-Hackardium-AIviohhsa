import streamlit as st
from huggingface_hub import InferenceClient
import os
import json
from dotenv import load_dotenv

# 1. CONFIGURATION
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
# Using Llama-3.2-3B for speed and instruction following
client = InferenceClient(model="meta-llama/Llama-3.2-3B-Instruct", token=HF_TOKEN)


BOT_CONFIGS = {
    "kelly": {
        "name": "Kelly 🌸",
        "prompt": "Your name is Kelly. You are a comforting and empathizing health assistant. Focus on validating feelings and being soft-spoken.",
        "file": "history_kelly.json"
    },
    "hannah": {
        "name": "Hannah 🧭",
        "prompt": "Your name is Hannah. You are a wise advice-giving bot. Provide structured, grounded, and practical suggestions for improvement.",
        "file": "history_hannah.json"
    },
    "darbie": {
        "name": "Darbie 🍯",
        "prompt": "Your name is Darbie. You are a cheerful and slightly sarcastic bot. Use humor and wit to cheer up the user, but remain helpful.",
        "file": "history_darbie.json"
    }
}

query_params = st.query_params
bot_key = query_params.get("bot", "kelly") 
current_bot = BOT_CONFIGS[bot_key]


def save_history(messages, filename):
    with open(filename, "w") as f:
        json.dump(messages, f)

def load_history(filename, system_prompt):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return [{"role": "system", "content": system_prompt}]


if "current_bot_key" not in st.session_state or st.session_state.current_bot_key != bot_key:
    st.session_state.current_bot_key = bot_key
    st.session_state.messages = load_history(current_bot["file"], current_bot["prompt"])


def search_history_for_context(query, messages):
    """Parses JSON history for keywords to provide temporal memory."""
    relevant_past = []
    keywords = ["last time", "remember", "previous", "happened", "when was"]
    
    if any(word in query.lower() for word in keywords):
        for msg in messages[1:]: 
            
            if "happy" in query.lower() and "happy" in msg['content'].lower():
                relevant_past.append(msg['content'])
            elif "sad" in query.lower() and "sad" in msg['content'].lower():
                relevant_past.append(msg['content'])
        
        return "\n".join(relevant_past[-3:])
    return ""


st.title(current_bot["name"])
st.caption(f"Connected to {current_bot['name']} | Personality: {bot_key.capitalize()}")


chat_log = json.dumps(st.session_state.messages, indent=2)
st.sidebar.download_button(f"💾 Download {current_bot['name']} Log", chat_log, f"{bot_key}_chat.json")


for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("How are you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    bot_text = "" 

    try:
        with st.chat_message("assistant"):
            response = client.chat_completion(messages=st.session_state.messages, max_tokens=300)
            bot_text = response.choices[0].message.content
            st.markdown(bot_text)
        
        
        if bot_text:
            st.session_state.messages.append({"role": "assistant", "content": bot_text})
            save_history(st.session_state.messages, current_bot["file"])
            
    except Exception as e:
        st.error(f"Error: {e}")
