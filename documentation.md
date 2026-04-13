# LAZYDUCK AI Chat — Documentation

---

## 1. What I Built

I built a simple AI chat website called **LAZYDUCK**.

You open it in a browser, type a question, and an AI answers you. That's it.

It has two parts:
- **Frontend** — the chat page you see in the browser (HTML, CSS, JavaScript)
- **Backend** — a Python server that talks to the AI (Flask + Groq API)

---

## 2. Tools and Technologies I Used

- **Python** — the programming language I used for the backend
- **Flask** — a Python library that lets you build websites and APIs
- **Groq API** — gives me access to a powerful AI model (LLaMA 3.3)
- **HTML/CSS** — the chat page design
- **JavaScript** — sends the user's message to the server and shows the reply
- **python-dotenv** — safely loads the API key from a `.env` file
- **Flask-CORS** — allows the frontend to talk to the backend

---

## 3. How LLM APIs Work

LLM means **Large Language Model** — it's an AI trained on a lot of text so it can understand and answer questions.

I don't run the AI on my computer. Instead:

1. I send the user's message to Groq's servers over the internet
2. Groq runs it through the LLaMA AI model
3. The AI generates a reply
4. Groq sends the reply back to me
5. I show it to the user

Think of it like texting someone — I send a message, they reply, I read it.

---

## 4. How Frontend and Backend Communicate

The frontend (browser) and backend (Python server) talk to each other using **HTTP requests** — the same way your browser loads any website.

Here's the flow:

```
User types a message
       ↓
JavaScript sends it to Flask  →  POST /chat
       ↓
Flask sends it to Groq AI
       ↓
Groq AI replies
       ↓
Flask sends reply back to browser
       ↓
JavaScript shows the reply in the chat
```

The data is sent as **JSON**, like this:

- Browser sends: `{ "message": "What is Python?" }`
- Flask returns: `{ "reply": "Python is a programming language..." }`

---

## 5. How I Handled the API Key Securely

The API key is like a password — if someone else gets it, they can use my account.

Here's what I did to keep it safe:

1. Put the key in a `.env` file:
```
GROQ_API_KEY=my_secret_key
```

2. Loaded it in Python without hardcoding it:
```python
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
```

3. Added `.env` to `.gitignore` so it never gets uploaded to GitHub:
```
.env
```

This way the key only lives on my computer and is never public.

---

## 6. Prompts I Used When Asking AI for Help

I used Kiro AI to help me understand and build this project. Some prompts I used:

**Backend (Python/Flask):**
- *"Explain what Flask is for a beginner"*
- *"What is CORS and why do I need it?"*
- *"How do I load an API key from a .env file?"*
- *"Why do we write Flask(__name__)?"*
- *"How does an LLM API work in simple words?"*
- *"What does .gitignore do?"*

**Frontend (HTML/CSS):**

Since I don't know HTML and CSS well, I also asked AI to help me write parts of the frontend. Some prompts I used:

- *"Write me a simple chat UI in HTML and CSS"*
- *"Make the chat bubbles look different for user and AI messages"*
- *"How do I make the input stay at the bottom of the page?"*
- *"Write a JavaScript function that sends a message to /chat and shows the reply"*
- *"Make the chat page look clean and modern with CSS"*

---

## 7. Problems I Faced and How I Fixed Them

**Problem 1: API key was exposed on GitHub**
I accidentally committed the `.env` file which contained my secret Groq API key. GitHub detected it and blocked the push entirely.
Fix: Removed `.env` from the entire git history using `git filter-branch`, force pushed, then immediately deleted the old API key and created a new one on Groq console.

**Problem 2: Frontend and backend were not connecting**
When JavaScript sent a message to `/chat`, the browser was blocking the request because the frontend and backend were on different origins.
Fix: Added `Flask-CORS` to the backend so the server accepts requests from the frontend.

**Problem 3: The AI response had no error handling**
Early on, if the Groq API was down or the key was wrong, the whole app would crash with an unhandled exception.
Fix: Wrapped the API call in a `try/except` block so the app returns a clean error message instead of crashing.

**Problem 4: Empty messages were being sent to the AI**
If the user clicked send without typing anything, an empty string was sent to Groq which wasted API calls.
Fix: Added a check with `.strip()` — if the message is empty after removing spaces, return an error before calling the API.

**Problem 5: Chat history disappeared on page refresh**
Every time the user refreshed the page, all previous messages were gone. This made the app feel broken and unusable.
Fix: Used the browser's `localStorage` to save chat messages. Now when the page loads, it reads the saved history and shows it back to the user automatically.

**Problem 6: Users could not fix typos after sending a message**
Once a message was sent, there was no way to correct it. This was frustrating especially for longer messages.
Fix: Added an edit feature — each sent message has an edit button. The user can click it, change the text, and resend it to the AI.

---

## 8. What I Learned

- How to build a basic web app with Flask
- How frontend and backend talk to each other using HTTP and JSON
- What an API is and how to use one
- How to keep secrets safe with `.env` and `.gitignore`
- What LLMs are and how they work
- How to read error messages and fix bugs step by step
- That you should always restart the server after making changes
