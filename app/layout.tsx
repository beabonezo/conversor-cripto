// Layout raiz do App Router
import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Conversor de Criptomoedas",
  description:
    "Converta criptomoedas para reais (BRL) em tempo real com dados da API CoinGecko.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
