from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Prompt(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"mensaje": "MarketingIAapp está funcionando 🚀"}

@app.post("/generar")
def generar_contenido(prompt: Prompt):
    respuesta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en marketing digital y creación de contenido persuasivo."},
            {"role": "user", "content": prompt.texto}
        ]
    )

    return {"resultado": respuesta.choices[0].message.content}
