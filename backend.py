from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__, static_folder=".")
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Ruta para mostrar el index.html
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Ruta para generar contenido
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    texto = data.get("texto")

    if not texto:
        return jsonify({"error": "No se envió texto"}), 400

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en marketing digital y copywriting persuasivo."},
            {"role": "user", "content": texto}
        ]
    )

    return jsonify({
        "resultado": respuesta.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)
