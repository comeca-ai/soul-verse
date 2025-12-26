# SoulVerse

Seu assistente de conforto espiritual diário.

## Como rodar o projeto

### Pré-requisitos
- Node.js 18+
- NPM
- Ngrok (para testes com ChatGPT Developer Mode)

### 1. Servidor MCP (Backend)
```bash
cd server
npm install
npm run dev
```
O servidor rodará na porta **8080** com suporte a SSE.

**Para testar no ChatGPT:**
1. Rode o ngrok: `ngrok http 8080`
2. Copie a URL gerada (ex: `https://abcd.ngrok-free.app`)
3. No ChatGPT Developer Mode, use a URL: `https://abcd.ngrok-free.app/sse`

### 2. Widget (Frontend)
```bash
cd web
npm install
npm run dev
```
Acesse `http://localhost:5173` para ver o preview do card (com dados mockados).

## Estrutura
- `/server`: Código do MCP Server (Logic & Tools)
- `/web`: Código do Widget React (UI)
- `app_spec.json`: Especificação do App
- `toolset.json`: Definição de Tools para registro
