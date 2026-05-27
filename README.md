# 💰 Conversor de Criptomoedas

Conversor de criptomoedas em tempo real utilizando dados da API pública do [CoinGecko](https://www.coingecko.com).

## Stack

- **Framework:** Next.js 14+ (App Router)
- **Linguagem:** TypeScript
- **Estilo:** CSS puro (sem bibliotecas de UI)
- **Preços:** CoinGecko API (pública, sem chave)
- **Deploy:** Vercel

## Funcionalidades (Fase 1)

- Seleção de criptomoeda (BTC, ETH, SOL, DOGE, ADA)
- Entrada de quantidade e conversão para BRL em tempo real
- Tratamento de erros e timeout de 10s na chamada à API

## Como rodar localmente

```bash
npm install
npm run dev
```

Acesse: [http://localhost:3000](http://localhost:3000)

## Estrutura de arquivos

```
app/
  layout.tsx          → Layout raiz
  page.tsx            → Página principal
  globals.css         → Design system
  api/preco/[moeda]/
    route.ts          → Endpoint GET /api/preco/{moeda}
components/
  Converter.tsx       → Componente do conversor
lib/
  cotacao.ts          → Lógica de fetch na CoinGecko
  moedas.ts           → Dicionário de moedas suportadas
```

## Fase 2 (stand by)

- Autenticação via Supabase Auth
- Histórico de conversões por usuário
- Consulte `CLAUDE.md` para detalhes do planejamento.
