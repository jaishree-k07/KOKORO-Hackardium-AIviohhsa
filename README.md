# 🌸 Kokoro: An AI-Powered Mental Health Ecosystem

**Kokoro**  is a holistic wellness platform designed to bridge the gap between traditional mental health tracking and modern AI-driven support. Built for the **AI WARS Hackathon**, this ecosystem provides users with a safe, calming space to log emotions, track achievements, and receive personalized guidance from a trio of specialized AI personalities.

## 🚀 Project Overview

The ecosystem is divided into two main components:

1. **AI WARS Dashboard**: A comprehensive HTML/CSS/JS frontend featuring interactive tools like the Mood Jar and Dear Diary.
2. **Serene Healthbot**: A Python-based multi-personality chatbot powered by Large Language Models (LLMs).

---

## ✨ Key Features

### 🎮 The Dashboard (AI WARS)

* **Mood Jar**: A visual, interactive way to log daily emotions using emoji "droplets".
* **Streak Tracker**: Gamified check-ins using Browser LocalStorage to encourage consistency.
* **Dear Diary & Little Wins**: Dedicated sections for long-form reflection and celebrating micro-victories.
* **Dynamic Motivation**: Real-time affirmation generator to boost user morale.

### 🤖 The AI Chatbot (Triple-Personality System)

* **Kelly (Comfort)**: Empathic and soft-spoken for emotional validation.
* **Hannah (Advice)**: Structured and practical for goal-oriented guidance.
* **Darbie (Wit)**: Cheerful and slightly sarcastic to provide lighthearted distraction.
* **Smart Searchable History**: Implements **Context Injection** allowing the AI to "remember" and recall past conversations from local JSON logs.

---

## 🛠️ Technical Stack

* **Frontend**: HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6+).
* **Backend**: Python 3.11, Streamlit.
* **AI Engine**: **Llama-3.2-3B-Instruct** hosted via **Hugging Face Inference API**.
* **Data Persistence**: JSON-based local storage for chat history and Browser LocalStorage for dashboard stats.

---

## 📦 Installation & Setup

1. **Clone the Repository**:
```bash
git clone https://github.com/YOUR_USERNAME/Kokoro-Project.git

```


2. **Install Python Dependencies**:
```bash
pip install streamlit huggingface-hub python-dotenv

```


3. **Configure Environment**:
Create a `.env` file in the `mental-health-bot` folder and add your Hugging Face Token:
```text
HF_TOKEN=your_huggingface_token_here

```


4. **Launch the Services**:
* **Run Chatbot**: `streamlit run mental-health-bot/app.py`
* **Open Dashboard**: Simply open `AI-WARS/dashboard.html` in any modern web browser.



---

## 🛡️ Privacy & Security

* **Data Isolation**: Each AI personality maintains its own isolated JSON history file to prevent information leakage between bots.
* **Local Storage**: All personal dashboard data is stored locally on the user's machine, ensuring maximum privacy.

---
## 🗺️ Future Roadmap
- [ ] **AI-Powered Sentiment Trends**: Visualizing mood shifts over a month using classification models.
- [ ] **Voice-to-Text Journaling**: Integration of speech recognition for hands-free reflection.
- [ ] **Localized Language Support**: Expanding Kelly, Hannah, and Darbie to speak multiple languages.
