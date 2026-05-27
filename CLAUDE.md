# CLAUDE.md — Conversor de Criptomoedas

## Contexto do projeto

Este projeto é um conversor de criptomoedas em tempo real. O usuário seleciona uma criptomoeda, informa uma quantidade em BRL e recebe o valor convertido em tempo real.

**Stack original:**
- Frontend: Streamlit (Python)
- Backend: FastAPI (Python)
- Preços: CoinGecko API (pública, sem chave)

**Stack de destino (refatoração):**
- Frontend + API Routes: Next.js 14 (App Router)
- Linguagem: TypeScript
- Preços: CoinGecko API (mesmos endpoints)

---

## Regra principal

> Preservar toda a lógica de negócio e os endpoints externos.
> Apenas a camada de framework muda (Streamlit → React, FastAPI → Next.js API Routes).
> Autenticação e histórico de conversões estão fora do escopo desta refatoração (fase 2).

---

## Mapeamento de arquivos — fase 1 (escopo atual)

| Arquivo original (Python) | Arquivo de destino (TypeScript) | O que preservar |
|---|---|---|
| `cotacao.py` | `lib/cotacao.ts` | Lógica de fetch na CoinGecko, tratamento de timeout e erro, normalização do nome da moeda |
| `moedas_suportadas.py` | `lib/moedas.ts` | Dicionário exato: chave = ID CoinGecko, valor = símbolo |
| `api.py` (endpoint GET /preco/{moeda}) | `app/api/preco/[moeda]/route.ts` | Busca preço na CoinGecko e retorna JSON |
| `main.py` (bloco do conversor) | `components/Converter.tsx` | Lógica: selecionar moeda → buscar preço → calcular resultado → exibir |
| `main.py` (estrutura geral) | `app/page.tsx` | Renderizar diretamente o `<Converter />` sem verificação de sessão |

---

## Arquivos que NÃO devem ser portados nesta fase

| Arquivo | Motivo |
|---|---|
| `banco.py` | Sem uso no escopo atual (fase 2) |
| `api.py` (POST /conversoes) | Histórico fora do escopo (fase 2) |
| `api.py` (GET /conversoes/{user_id}) | Histórico fora do escopo (fase 2) |
| `main.py` (bloco de login) | Auth fora do escopo (fase 2) |
| `teste.py` | Rascunho de aprendizado |
| `testerun.py` | Rascunho de aprendizado |
| `teste_api.py` | Rascunho de aprendizado |
| `auth.py` | Contém credenciais hardcoded — ignorar |

---

## API externa — CoinGecko

Endpoint utilizado:
```
GET https://api.coingecko.com/api/v3/simple/price?ids={moeda}&vs_currencies=brl
```

**Regras a preservar:**
- Normalizar o nome da moeda com `.toLowerCase().trim()` antes de enviar
- Incluir header `User-Agent: Mozilla/5.0` para evitar bloqueio
- Timeout de 10 segundos
- Retornar `null` em caso de erro (sem lançar exceção para o cliente)

---

## Variáveis de ambiente

Criar arquivo `.env.local` na raiz. Nesta fase não há variáveis obrigatórias (CoinGecko é pública). Deixar o arquivo preparado para a fase 2:

```
# Fase 2 — Auth e histórico (não necessário agora)
# NEXT_PUBLIC_SUPABASE_URL=https://<project-id>.supabase.co
# NEXT_PUBLIC_SUPABASE_ANON_KEY=<anon_key>
```

---

## Estrutura de pastas esperada

```
conversor-cripto/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── globals.css
│   └── api/
│       └── preco/
│           └── [moeda]/
│               └── route.ts
├── components/
│   └── Converter.tsx
├── lib/
│   ├── cotacao.ts
│   └── moedas.ts
├── .env.local
├── CLAUDE.md
├── next.config.ts
├── package.json
├── tsconfig.json
└── .gitignore
```

---

## Ordem de execução recomendada

Seguir esta sequência para evitar quebrar dependências:

1. `lib/moedas.ts` — sem dependências externas
2. `lib/cotacao.ts` — depende apenas de fetch nativo
3. `app/api/preco/[moeda]/route.ts` — depende de `lib/cotacao.ts`
4. `components/Converter.tsx` — depende da API route de preço
5. `app/page.tsx` — depende de `Converter`
6. `app/layout.tsx` e `app/globals.css` — estrutura base

---

## Restrições

- Não usar `pages/` router — usar exclusivamente App Router (`app/`)
- Não instalar bibliotecas de UI (sem Chakra, MUI, shadcn) — HTML e CSS padrão com Tailwind apenas se já estiver configurado
- Não criar novos endpoints além de `GET /api/preco/[moeda]`
- Não remover o tratamento de erros de `cotacao.py` ao portar para `cotacao.ts`
- Não implementar autenticação ou gravação no banco nesta fase

---

## Fase 2 — stand by (não implementar agora)

Os itens abaixo estão documentados para implementação futura, após a fase 1 estar funcionando e deployada na Vercel.

**Funcionalidades:**
- Autenticação de usuário via Supabase Auth (`signInWithPassword`)
- Tela de login (`components/LoginForm.tsx`)
- Proteção de rota em `app/page.tsx` (verificar sessão antes de renderizar o conversor)
- Salvar conversão na tabela `conversoes` do Supabase após cada cálculo
- Exibir histórico de conversões do usuário logado

**Arquivos a criar na fase 2:**
- `lib/supabase.ts`
- `components/LoginForm.tsx`
- `app/api/conversoes/route.ts`

**Banco de dados (já existe no Supabase — não alterar):**

| Coluna | Tipo |
|---|---|
| `id` | uuid (PK) |
| `user_id` | uuid (FK → auth.users) |
| `moeda_origem` | text |
| `moeda_destino` | text |
| `valor_origem` | numeric |
| `valor_resultado` | numeric |
| `data_conversao` | timestamptz (default: now()) |
