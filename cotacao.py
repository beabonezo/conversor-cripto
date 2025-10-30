import requests

def obter_cotacao(cripto:str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies=brl"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.RequestException:
        print("Erro ao buscar cotação. Tente novamente mais tarde.")
        return None

    dados = resposta.json()
    if cripto in dados:
        return dados[cripto]["brl"]
    else:
        print("Criptomoeda não encontrada")
        return None
    