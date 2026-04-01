import streamlit as st
import requests
from supabase import create_client
from moedas_suportadas import moedas
from cotacao import obter_cotacao
from dotenv import load_dotenv
import os

# configuração da página
st.set_page_config(page_title="Conversor Cripto", page_icon="💰", layout="centered")

st.markdown("""
    <style>
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

# conexão com supabase — uma só vez
load_dotenv()
URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(URL, KEY)

# tela de login — bloqueia o resto do app até autenticar
if "usuario" not in st.session_state:
    st.title("Login")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        try:
            resposta = supabase.auth.sign_in_with_password({
                "email": email,
                "password": senha
            })
            st.session_state["usuario"] = resposta.user
            st.rerun()
        except:
            st.error("Email ou senha incorretos")
    st.stop()

# app principal — só chega aqui se estiver logado
st.title("💰 Conversor de Criptomoedas para Reais (BRL)")
st.write("Converta rapidamente suas criptomoedas favoritas com dados em tempo real da API CoinGecko.")

cripto = st.selectbox("Selecione a Criptomoeda:", list(moedas.keys()))
quantidade = st.number_input("Digite a quantidade:", min_value=0.0, format="%.6f")

if st.button("Converter"):
    with st.spinner("Buscando cotação..."):
        try:
            resposta = requests.get(f"http://localhost:8000/preco/{cripto}")
            dados = resposta.json()

            if "erro" in dados:
                st.error("Moeda não encontrada.")
            else:
                cotacao = dados["preco_brl"]
                valor_em_reais = quantidade * cotacao

                st.markdown(f"""
                <div class="result">
                    <h3>💎 {quantidade} {moedas[cripto]} = R$ {valor_em_reais:,.2f}</h3>
                    <p>1 {moedas[cripto]} = R$ {cotacao:,.2f}</p>
                </div>
                """, unsafe_allow_html=True)

                supabase.table("conversoes").insert({
                    "user_id": st.session_state["usuario"].id,
                    "moeda_origem": "BRL",
                    "moeda_destino": moedas[cripto],
                    "valor_origem": quantidade,
                    "valor_resultado": valor_em_reais
                }).execute()
                st.success("Conversão salva!")

        except Exception as e:
            st.error(f"Erro: {e}")