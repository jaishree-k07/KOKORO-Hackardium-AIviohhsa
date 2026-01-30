import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# FIX 1: Use a model that is currently supported by the free Inference API
MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"

client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

# FIX 2: Gemma doesn't like 'system' roles, but Llama handles them perfectly
messages = [
    {"role": "system", "content": "You are a supportive, concise health assistant."}
]

print("\nHF Chatbot (Llama-3.2) - type 'exit' to quit")

while True:
    user_text = input("You: ").strip()
    if user_text.lower() in {"exit", "quit"}:
        print("Bot: Bye!")
        break
    
    if not user_text: continue

    messages.append({"role": "user", "content": user_text})

    try:
        resp = client.chat_completion(
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )
        
        bot_text = resp.choices[0].message.content
        print(f"Bot: {bot_text}\n")
        messages.append({"role": "assistant", "content": bot_text})

    except Exception as e:
        print(f"Bot (error): {e}")
        messages.pop()
        continue