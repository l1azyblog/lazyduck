# Project Documentation — Private AI Chat

---

## 1. What I Built

I built a simple AI-powered chat web application called **Private AI Chat**.

The app allows a user to type any message in a browser and receive a response from an AI model in real time. It has a clean chat interface on the frontend and a lightweight Python server on the backend that connects to the Groq AI API.

There is no login, no database, and no complex setup — just a simple question-and-answer chat powered by a large language model.

---

## 2. Tools and Technologies Used

| Tool / Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Flask** | Web framework — runs the backend server |
| **Flask-CORS** | Allows cross-origin requests between frontend and backend |
| **Groq API** | Provides access to the LLaMA 3.3 AI model |
| **python-dotenv** | Loads the API key securely from a `.env` file |
| **HTML/CSS** | Frontend chat interface |
| **JavaScript** | Sends user messages to the backend and displays responses |

---

## 3. How LLM APIs Work (In My Own Words)

LLM stands for **Large Language Model** — these are AI models trained on huge amounts of text data (like books, websites, code, etc.) so they can understand and generate human language.

When I use the Groq API, here is what happens step by step:

1. The user types a message in the browser
2. My Flask server receives that message
3. Flask sends the message to Groq's servers over the internet
4. Groq runs the message through the LLaMA 3.3 model
5. The model generates a text response
6. Groq sends that response back to my Flask server
7. Flask sends it to the browser and it appears in the chat

I never run the AI model on my own computer — I just send requests to Groq's servers and get answers back. This is what "using an API" means.

---

## 4. How Frontend and Backend Communicate

The frontend (HTML/CSS/JavaScript) and backend (Flask/Python) are two separate parts of the app. They communicate using **HTTP requests**.

Here is the flow:

```
User types message
      ↓
JavaScript sends POST request to /chat
      ↓
Flask receives the request and reads the message
      ↓
Flask sends message to Groq AI
      ↓
Groq returns AI response
      ↓
Flask sends response back as JSON
      ↓
JavaScript receives JSON and displays it in the chat
```

The key endpoint is:

- `GET /` — loads the chat page (HTML)
- `POST /chat` — receives a message, returns AI response as JSON

Example of what JavaScript sends:
```json
{ "message": "What is Python?" }
```

Example of what Flask returns:
```json
{ "reply": "Python is a high-level programming language..." }
```

---

## 5. How I Handled the API Key Securely

The Groq API key is a secret — if someone else gets it, they can use my account and I could get charged or banned.

To keep it safe I used these steps:

1. Created a `.env` file in the project folder and put the key there:
```
GROQ_API_KEY=my_secret_key_here
```

2. Used the `python-dotenv` library to load it in `app.py`:
```python
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
```

3. Added `.env` to `.gitignore` so it never gets uploaded to GitHub:
```
.env
```

This way the key only exists on my local machine and is never exposed publicly.

---

## 6. What Prompts I Used When Asking AI Tools for Help

During this project I used AI tools (like Kiro) to help me understand and build the app. Some of the prompts I used:

- *"Explain what Flask is and how it works for a beginner"*
- *"What is CORS and why do I need flask-cors?"*
- *"Why do we use `__name__` in `Flask(__name__)`?"*
- *"How do I read an API key from a .env file in Python?"*
- *"Explain how LLM APIs work in simple words"*
- *"What does `.gitignore` do and why is `.env` in it?"*

I tried to understand each answer rather than just copy-paste the code.

---

## 7. Problems I Faced and How I Solved Them

**Problem 1: `ModuleNotFoundError: No module named 'flask'`**
- Cause: Flask was not installed
- Solution: Ran `pip install -r requirements.txt`

**Problem 2: `ModuleNotFoundError: No module named 'groq'`**
- Cause: `groq` was missing from `requirements.txt`
- Solution: Added `groq` to `requirements.txt` and ran `pip install -r requirements.txt`

**Problem 3: `TemplateNotFound: index.html`**
- Cause: I renamed the HTML file to `LHome.html` but forgot to restart the server
- Solution: Stopped the server with `Ctrl+C` and restarted with `python app.py`

---

## 8. What I Learned from This Project

- How to build a basic web app using **Flask**
- How **frontend and backend communicate** using HTTP and JSON
- What an **API** is and how to use one (Groq/LLaMA)
- How to keep **secrets safe** using `.env` and `.gitignore`
- What **LLMs** are and how they work at a high level
- How to read error messages and **debug** problems step by step
- The importance of **restarting the server** after making changes
