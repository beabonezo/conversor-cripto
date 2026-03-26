import requests

def obter_cotacao(cripto: str):
    cripto = cripto.lower().strip()  # garante formato correto
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies=brl"

    headers = {
        "User-Agent": "Mozilla/5.0"  # evita bloqueio da API
    }

    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
    except requests.exceptions.Timeout:
        print("Tempo de conexão esgotado.")
        return None
    except requests.RequestException as e:
        print(f"Erro ao buscar cotação: {e}")
        return None

    dados = resposta.json()
    if cripto in dados:
        return dados[cripto]["brl"]
    else:
        print(f"Criptomoeda '{cripto}' não encontrada na resposta: {dados}")
        return None