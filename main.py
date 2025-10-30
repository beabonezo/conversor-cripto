import streamlit as st
from moedas_suportadas import moedas
from cotacao import obter_cotacao

st.set_page_config(page_title="Conversor Cripto", page_icon="💰", layout="centered")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #b8b8ff !important;
    }
    h1, h2, h3 {
        color: #a29bfe;
        text-align: center;
    }
    .result {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💰 Conversor de Criptomoedas para Reais (BRL)")
st.write("Converta rapidamente suas criptomoedas favoritas com dados em tempo real da API CoinGecko.")

cripto = st.selectbox("Selecione a Criptomoeda:", list(moedas.keys()))
quantidade = st.number_input("Digite a quantidade:", min_value=0.0, format="%.6f")

if st.button("Converter"):
    with st.spinner("Buscando cotação..."):
        cotacao = obter_cotacao(cripto)
        if cotacao:
            valor_em_reais = quantidade * cotacao
            st.markdown(f"""
            <div class="result">
                <h3>💎 {quantidade} {moedas[cripto]} = R$ {valor_em_reais:,.2f}</h3>
                <p>1 {moedas[cripto]} = R$ {cotacao:,.2f}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Não foi possível obter a cotação. Verifique a conexão ou o nome da moeda.")

def main():
    print("\n===== CONVERSOR DE MOEDA CRIPTO -> REAL =====\n")

    while True:
        print("Moedas disponíveis:")
        for nome, sigla in moedas.items():
            print(f" --> {nome.capitalize()} = ({sigla})")

        cripto = input("Qual moeda deseja converter?:").lower()
        if cripto not in moedas:
            print("moeda não encontrada.")
            continue
        
        try:
            quantidade = float(input("Digite a quantidade que deseja converter:"))
        except ValueError:
            print("Por favor, insira um número válido")
            continue
        
        cotacao = obter_cotacao(cripto)
        if cotacao:
            valor_em_reais = quantidade * cotacao
            print(f"{quantidade} de {moedas[cripto]} equivalem a R$ {valor_em_reais:,.2f}")
        else:
            print("Não foi possível obter a cotação.")
            continue

        repetir = input("Deseja converter outra moeda? [S/N]:").lower()
        if repetir != "s":
            print("Obrigada por usar o conversor")
            break

if __name__ == "__main__":
    main()
