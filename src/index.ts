import { FastMCP } from 'fastmcp';
import { z } from 'zod';
import axios from 'axios';

// Criação do servidor MCP
const server = new FastMCP({
    name: "SoulVerse Server",
    version: "1.0.0",
});

// Tool: get_bible_verse
server.addTool({
    name: "get_bible_verse",
    description: "Busca o texto oficial completo de uma passagem bíblica baseada em sua referência. Use para garantir a precisão.",
    parameters: z.object({
        reference: z.string().describe("A referência bíblica no formato 'Livro Capítulo:Versículo' (ex: 'João 3:16')."),
        translation: z.enum(["almeida"]).optional().default("almeida").describe("A versão da tradução. Use 'almeida' para português."),
    }),
    execute: async (args, context) => {
        try {
            const { reference, translation } = args;

            // Chamada para a API pública
            // bible-api.com aceita tradução como query param. 'almeida' é a chave para PT.
            const response = await axios.get(`https://bible-api.com/${encodeURIComponent(reference)}?translation=${translation}`);

            const data = response.data;

            // Monta o retorno estruturado para o modelo
            const structuredContent = {
                success: true,
                reference: data.reference,
                text: data.text.trim(),
                translation: translation
            };

            // Monta o _meta para o Widget renderizar bonito
            const _meta = {
                kind: "verse_card",
                display: {
                    book: data.reference.split(' ')[0] || "Bíblia", // Simplificação, pode melhorar com regex se precisar
                    reference: data.reference,
                    full_text: data.text.trim(),
                    theme_color: "#4F46E5" // Indigo
                }
            };

            // Se possível, reportar meta via log (simulação, pois FastMCP abstrai isso, mas retornamos no result para debug/uso)
            // Em produção real com SDK novo, usaríamos context.reportResultMetadata() se disponível.
            // Por enquanto, retornamos um objeto combinado ou apenas o texto, dependendo do contrato.
            // O padrão seguro do FastMCP é retornar o conteúdo.

            // Return compatível com toolCall
            return {
                content: [
                    {
                        type: "text",
                        text: JSON.stringify(structuredContent, null, 2)
                    }
                ],
                _meta: _meta // Convenção nossa, o MCP server real pode precisar adaptar isso para protocol extras se suportado
            };

        } catch (error: any) {
            return {
                content: [
                    {
                        type: "text",
                        text: `Erro ao buscar versículo: ${error.message}`
                    }
                ],
                isError: true
            };
        }
    },
});

// Start server with HTTP Streaming transport (enables SSE at /sse for ChatGPT)
const PORT = process.env.PORT ? parseInt(process.env.PORT) : 8080;

server.start({
    transportType: "httpStream",
    httpStream: {
        port: PORT,
    },
}).then(() => {
    console.log("SoulVerse Server running on HTTP/SSE transport");
    console.log(`SSE Endpoint: http://localhost:${PORT}/sse`);
});
