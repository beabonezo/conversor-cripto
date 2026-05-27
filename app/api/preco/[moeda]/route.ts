// API Route Next.js — equivalente ao endpoint GET /preco/{moeda} do FastAPI
import { NextRequest, NextResponse } from "next/server";
import { obterCotacao } from "@/lib/cotacao";

// Garante que a route sempre execute no servidor a cada requisição (nunca cacheada)
export const dynamic = "force-dynamic";


export async function GET(
  _request: NextRequest,
  { params }: { params: Promise<{ moeda: string }> }
) {
  const { moeda } = await params;

  // Validação básica do parâmetro
  if (!moeda || typeof moeda !== "string") {
    return NextResponse.json(
      { erro: "Parâmetro 'moeda' inválido." },
      { status: 400 }
    );
  }

  const preco = await obterCotacao(moeda);

  if (preco === null) {
    return NextResponse.json(
      { erro: "Moeda não encontrada ou erro ao buscar cotação." },
      { status: 404 }
    );
  }

  return NextResponse.json({ moeda: moeda.toLowerCase().trim(), preco_brl: preco });
}
