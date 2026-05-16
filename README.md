# AI Chat App 🤖

A simple terminal-based AI chat application built with Python, powered by **Llama 3** via the Groq API.

Built by [Vinay Kommalapati](https://github.com/vinaykommalapati) — AI Engineer & Full Stack Developer.

---

## Features

- 💬 Multi-turn conversation (remembers chat history)
- ⚡ Super fast responses using Groq's LPU inference
- 🧠 Powered by Meta's Llama 3 (8B) model
- 🖥️ Clean terminal interface

---

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/vinaykommalapati/ai-chat-app.git
cd ai-chat-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up for free and copy your API key

### 4. Set your API key
```bash
# On Windows
set GROQ_API_KEY=your_api_key_here

# On Mac/Linux
export GROQ_API_KEY=your_api_key_here
```

### 5. Run the app
```bash
python app.py
```

---

## Demo

```
==================================================
   AI Chat App — Built by Vinay Kommalapati
==================================================
Type your message and press Enter to chat.
Type 'quit' or 'exit' to stop.

You: What is machine learning?
AI: Machine learning is a branch of AI where systems learn
    from data to make predictions or decisions without being
    explicitly programmed for each task...

You: Give me an example
AI: Sure! A spam filter is a great example...
```

---

## Tech Stack

- **Python** 3.8+
- **Groq API** — ultra-fast LLM inference
- **Llama 3** — Meta's open source LLM

---

## License

MIT License — free to use and modify.
