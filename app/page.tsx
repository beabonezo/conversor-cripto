// Página principal — renderiza o conversor diretamente (sem verificação de sessão nesta fase)
import Converter from "@/components/Converter";

export const metadata = {
  title: "Conversor de Criptomoedas | Dados em Tempo Real",
  description:
    "Converta rapidamente suas criptomoedas favoritas para reais (BRL) com dados em tempo real da API CoinGecko.",
};

export default function Home() {
  return (
    <main className="main-container">
      <header className="page-header">
        <div className="logo-badge">₿</div>
        <h1 className="page-title">Conversor de Criptomoedas</h1>
        <p className="page-subtitle">
          Dados em tempo real via CoinGecko · Sem cadastro necessário
        </p>
      </header>

      <Converter />

      <footer className="page-footer">
        Preços fornecidos por{" "}
        <a
          href="https://www.coingecko.com"
          target="_blank"
          rel="noopener noreferrer"
          className="footer-link"
        >
          CoinGecko
        </a>
      </footer>
    </main>
  );
}
