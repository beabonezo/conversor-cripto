"use client";

// Componente principal do conversor — portado do bloco do conversor em main.py
import { useState } from "react";
import { moedas } from "@/lib/moedas";

interface ResultadoConversao {
  moeda: string;
  simbolo: string;
  quantidade: number;
  cotacao: number;
  valorEmReais: number;
}

export default function Converter() {
  const [criptoSelecionada, setCriptoSelecionada] = useState<string>(
    Object.keys(moedas)[0]
  );
  const [quantidade, setQuantidade] = useState<string>("");
  const [resultado, setResultado] = useState<ResultadoConversao | null>(null);
  const [carregando, setCarregando] = useState<boolean>(false);
  const [erro, setErro] = useState<string | null>(null);

  async function handleConverter(e: React.FormEvent) {
    e.preventDefault();

    const qtd = parseFloat(quantidade);
    if (isNaN(qtd) || qtd <= 0) {
      setErro("Informe uma quantidade válida e maior que zero.");
      return;
    }

    setCarregando(true);
    setErro(null);
    setResultado(null);

    try {
      // Chama a API route interna — equivalente ao requests.get do Streamlit
      const resposta = await fetch(`/api/preco/${criptoSelecionada}`);
      const dados = await resposta.json();

      if (!resposta.ok || dados.erro) {
        setErro(dados.erro ?? "Moeda não encontrada.");
        return;
      }

      const cotacao: number = dados.preco_brl;
      const valorEmReais = qtd * cotacao;

      setResultado({
        moeda: criptoSelecionada,
        simbolo: moedas[criptoSelecionada],
        quantidade: qtd,
        cotacao,
        valorEmReais,
      });
    } catch {
      setErro("Erro ao buscar a cotação. Tente novamente.");
    } finally {
      setCarregando(false);
    }
  }

  return (
    <div className="converter-card">
      <form onSubmit={handleConverter} className="converter-form">
        {/* Seleção de criptomoeda */}
        <div className="field-group">
          <label htmlFor="cripto-select" className="field-label">
            Criptomoeda
          </label>
          <select
            id="cripto-select"
            value={criptoSelecionada}
            onChange={(e) => {
              setCriptoSelecionada(e.target.value);
              setResultado(null);
              setErro(null);
            }}
            className="field-select"
          >
            {Object.entries(moedas).map(([id, simbolo]) => (
              <option key={id} value={id}>
                {simbolo} — {id.charAt(0).toUpperCase() + id.slice(1)}
              </option>
            ))}
          </select>
        </div>

        {/* Quantidade */}
        <div className="field-group">
          <label htmlFor="quantidade-input" className="field-label">
            Quantidade
          </label>
          <input
            id="quantidade-input"
            type="number"
            min="0"
            step="any"
            placeholder="Ex: 0.5"
            value={quantidade}
            onChange={(e) => {
              setQuantidade(e.target.value);
              setResultado(null);
              setErro(null);
            }}
            className="field-input"
            required
          />
        </div>

        {/* Botão de conversão */}
        <button
          id="btn-converter"
          type="submit"
          disabled={carregando}
          className="btn-convert"
        >
          {carregando ? (
            <span className="btn-loading">
              <span className="spinner" aria-hidden="true" /> Buscando cotação...
            </span>
          ) : (
            "Converter"
          )}
        </button>
      </form>

      {/* Mensagem de erro */}
      {erro && (
        <div role="alert" className="error-box">
          ⚠️ {erro}
        </div>
      )}

      {/* Resultado da conversão */}
      {resultado && (
        <div className="result-box" aria-live="polite">
          <div className="result-main">
            💎 {resultado.quantidade} {resultado.simbolo} ={" "}
            <span className="result-value">
              R${" "}
              {resultado.valorEmReais.toLocaleString("pt-BR", {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2,
              })}
            </span>
          </div>
          <div className="result-sub">
            1 {resultado.simbolo} = R${" "}
            {resultado.cotacao.toLocaleString("pt-BR", {
              minimumFractionDigits: 2,
              maximumFractionDigits: 2,
            })}
          </div>
        </div>
      )}
    </div>
  );
}
