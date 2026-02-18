from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    idea = data.get("idea")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en marketing digital."},
            {"role": "user", "content": idea}
        ]
    )

    return jsonify({
        "result": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)
