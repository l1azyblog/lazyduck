import os
from flask import Flask, request, jsonify, render_template #flask - web app, request - to read the message came from user, jsonify - answer as a JSON file 
from flask_cors import CORS # allows to access resources from a different origin.
from groq import Groq 
from dotenv import load_dotenv #read key-value pairs from .env, for example

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise EnvironmentError("GROQ_API_KEY is not set in .env file.")

client = Groq(api_key=api_key)

@app.route("/")
def index():
    return render_template("lhome.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided."}), 400

    user_message = data["message"].strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_message}]
        )
        return jsonify({"reply": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": f"AI error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)