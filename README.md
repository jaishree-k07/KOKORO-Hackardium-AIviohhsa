🌸 Kokoro Holistic Wellness Ecosystem
This repository contains a holistic emotional wellness platform built for the AI WARS Hackathon. The ecosystem integrates traditional self-reflection tools with an advanced, multi-personality AI assistant to provide a safe and calming space for personal growth.

📋 Overview
Kokoro (Japanese for "Heart") bridges the gap between manual wellness tracking and modern intelligent support. The project leverages Streamlit for its backend logic and a sophisticated Llama-3.2-3B model to offer personalized guidance through three distinct AI personas.

✨ Features
Interactive Mood Jar: A visual tracking system using LocalStorage to log daily feelings via digital "droplets".

Triple-Personality AI Support: Specialized assistance through three unique personas:

Kelly: Focused on empathy and comfort.

Hannah: Focused on grounded, practical advice.

Darbie: Focused on cheerful wit and lighthearted distraction.

Smart Searchable History: Utilizes Context Injection to allow the AI to recall and summarize past user conversations from local JSON logs.

Gamified Wellness: Built-in streak tracking and achievement milestones to encourage consistent self-care.

🛠️ Tech Stack
Frontend: HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6+).

Backend: Python 3.11, Streamlit.

AI Logic: Hugging Face Inference API using Llama-3.2-3B-Instruct.

Data Persistence: Browser LocalStorage and JSON-based file storage.

🚀 Getting Started
1. Installation
Clone the repository and install the necessary dependencies:

Bash
git clone https://github.com/YOUR_USERNAME/KOKORO-Hackardium-AIviohhsa.git
cd KOKORO-Hackardium-AIviohhsa
pip install -r requirements.txt

2. Configure Environment
Create a .env file in the mental-health-bot/ directory and add your Hugging Face API token:

Plaintext
HF_TOKEN=your_token_here

3. Run the Ecosystem
Launch the AI Assistant:

Bash
streamlit run mental-health-bot/app.py
Launch the Dashboard: Open AI-WARS/dashboard.html in any modern web browser.

🛡️ Privacy & Security
The platform is designed with a Privacy-First approach:

Data Isolation: Each AI personality maintains separate JSON logs to prevent cross-persona data leakage.

Local-First Storage: Personal metrics and logs are stored strictly on the user's local machine.

## 🗺️ Future Roadmap
- [ ] **AI-Powered Sentiment Trends**: Visualizing mood shifts over a month using classification models.
- [ ] **Voice-to-Text Journaling**: Integration of speech recognition for hands-free reflection.
- [ ] **Localized Language Support**: Expanding Haru, Atlas, and Honey to speak multiple languages.