from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许前端跨域访问

openai.api_key = os.environ.get("OPENAI_API_KEY")  # 从环境变量读取密钥

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    messages = data.get("messages", [])

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return jsonify({
            "reply": response.choices[0].message["content"]
        })

    except Exception as e:
        print("Error calling OpenAI:", str(e))
        return jsonify({"error": str(e)}), 500
    