import { FastMCP } from 'fastmcp';
import { z } from 'zod'; // Import zod to match formatting, though strict types aren't needed for this client-side simulation

// Simples script para testar a lógica interna (unitário) ou conectar se fosse cliente.
// Vou reimplentar a lógica de chamada da API aqui apenas para validar a integração externa,
// já que conectar via stdio no mesmo processo é complexo.

import axios from 'axios';

async function testBiblia() {
    console.log("Testando busca de versículo: Salmos 23:1 (Almeida)...");

    try {
        const response = await axios.get(`https://bible-api.com/${encodeURIComponent("Salmos 23:1")}?translation=almeida`);

        if (response.data && response.data.text) {
            console.log("✅ Sucesso!");
            console.log("Texto:", response.data.text);
            console.log("Ref:", response.data.reference);
        } else {
            console.error("❌ Resposta inesperada:", response.data);
        }

    } catch (error: any) {
        console.error("❌ Falha na chamada:", error.message);
    }
}

testBiblia();
