import requests

# --- Script principal ---
response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={"ids": "bitcoin,ethereum", "vs_currencies": "brl,usd"}
)

print("Status:", response.status_code)
print("Corpo:", response.json())

# --- Experimento 1: navegar no dicionário ---
dados = response.json()
print("Bitcoin em BRL:", dados["bitcoin"]["brl"])
print("Ethereum em USD:", dados["ethereum"]["usd"])

# --- Experimento 2: quebrar a URL de propósito ---
response_erro = requests.get("https://api.coingecko.com/rota/inexistente")
print("Status do erro:", response_erro.status_code)

if response_erro.status_code == 200:
    print("Corpo:", response_erro.json())
else:
    print("Erro — servidor retornou:", response_erro.text)
