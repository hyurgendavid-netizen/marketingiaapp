from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/generar", methods=["POST"])
def generar():
    data = request.get_json()
    idea = data.get("idea")

    if not idea:
        return jsonify({"error": "No se envió la idea"}), 400

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en marketing digital y copywriting persuasivo."},
            {"role": "user", "content": idea}
        ]
    )

    return jsonify({
        "resultado": respuesta.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)
