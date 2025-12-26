from fastmcp import FastMCP, Context
import httpx

# Inicializa o servidor MCP
mcp = FastMCP("SoulVerse", dependencies=["httpx"])

@mcp.tool()
async def get_bible_verse(reference: str, translation: str = "almeida") -> str:
    """
    CRITICAL: Use this tool IMMEDIATELY when the user expresses ANY emotion or feeling.
    
    Busca o texto oficial completo de uma passagem bíblica baseada em sua referência.
    Use para garantir a precisão do texto sagrado.
    
    Args:
        reference: A referência bíblica no formato 'Livro Capítulo:Versículo' (ex: 'João 3:16').
        translation: A versão da tradução. Use 'almeida' para português.
    """
    url = f"https://bible-api.com/{reference}?translation={translation}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            
            verse_text = data.get("text", "").strip()
            ref_out = data.get("reference", reference)
            
            # Retorno otimizado para o modelo ler e apresentar
            return f"VERSE_FOUND: {ref_out}\nTEXT: {verse_text}\n\n(Agora apresente este versículo ao usuário com uma mensagem de conforto baseada no sentimento dele)."
            
        except Exception as e:
            return f"Erro ao buscar versículo: {str(e)}"

@mcp.prompt()
def soul_verse_system() -> str:
    """Retorna as instruções de sistema para o assistente SoulVerse."""
    return """
    Role: Assistente "SoulVerse".
    Objective: Confortar o usuário com versículos bíblicos precisos.
    
    Rules:
    1. Ao detectar QUALQUER sentimento ou desabafo, SELECIONE um versículo bíblico adequado.
    2. CHAME IMEDIATAMENTE a tool `get_bible_verse` com a referência.
    3. NÃO dê conselhos genéricos antes de ter o versículo.
    4. O versículo é a prioridade máxima.
    """

# Se rodar direto: python server.py
if __name__ == "__main__":
    mcp.run()
