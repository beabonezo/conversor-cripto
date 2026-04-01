from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client
import requests
import os

load_dotenv()

app = FastAPI()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(URL, KEY)

@app.get("/preco/{moeda}")
def buscar_preco(moeda: str):
    resposta = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": moeda, "vs_currencies": "brl"}
    )
    dados = resposta.json()
    if moeda not in dados:
        return {"erro": "moeda não encontrada"}
    return {"moeda": moeda, "preco_brl": dados[moeda]["brl"]}

@app.post("/conversoes")
def salvar_conversao(user_id: str, moeda_origem: str, moeda_destino: str, valor_origem: float, valor_resultado: float):
    resposta = supabase.table("conversoes").insert({
        "user_id": user_id,
        "moeda_origem": moeda_origem,
        "moeda_destino": moeda_destino,
        "valor_origem": valor_origem,
        "valor_resultado": valor_resultado
    }).execute()
    return {"salvo": True, "id": resposta.data[0]["id"]}

@app.get("/conversoes/{user_id}")
def buscar_historico(user_id: str):
    resposta = supabase.table("conversoes").select("*").eq("user_id", user_id).execute()
    return {"conversoes": resposta.data}