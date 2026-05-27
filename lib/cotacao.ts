// Portado de cotacao.py — preserva toda a lógica de negócio original

/**
 * Busca o preço em BRL de uma criptomoeda na API pública do CoinGecko.
 * Retorna null em caso de erro (sem lançar exceção para o cliente).
 */
export async function obterCotacao(cripto: string): Promise<number | null> {
  // Normaliza o nome da moeda antes de enviar (igual ao .lower().strip() do Python)
  const criptoNormalizada = cripto.toLowerCase().trim();

  const url = `https://api.coingecko.com/api/v3/simple/price?ids=${criptoNormalizada}&vs_currencies=brl`;

  try {
    const controller = new AbortController();
    // Timeout de 10 segundos (equivalente ao timeout=10 do requests.get)
    const timeoutId = setTimeout(() => controller.abort(), 10_000);

    const resposta = await fetch(url, {
      headers: {
        // Header User-Agent para evitar bloqueio da API (igual ao original)
        "User-Agent": "Mozilla/5.0",
      },
      // Desativa cache do Next.js — preço de cripto muda a cada segundo
      cache: "no-store",
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!resposta.ok) {
      console.error(`Erro na resposta da API: ${resposta.status}`);
      return null;
    }

    const dados = await resposta.json();

    if (criptoNormalizada in dados) {
      return dados[criptoNormalizada]["brl"] as number;
    } else {
      console.error(
        `Criptomoeda '${criptoNormalizada}' não encontrada na resposta: ${JSON.stringify(dados)}`
      );
      return null;
    }
  } catch (erro: unknown) {
    if (erro instanceof Error && erro.name === "AbortError") {
      console.error("Tempo de conexão esgotado.");
    } else {
      console.error(`Erro ao buscar cotação: ${erro}`);
    }
    return null;
  }
}
