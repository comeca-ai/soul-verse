from fastmcp import FastMCP, Context
import httpx

# Inicializa o servidor MCP
mcp = FastMCP("SoulVerse", dependencies=["httpx"])

@mcp.tool()
async def get_bible_verse(reference: str, translation: str = "almeida") -> str:
    """
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
            
            # Formata o retorno. 
            # O FastMCP Python retorna strings ou objetos simples diretamente.
            # Para retornar metadados ricos (UI), podemos retornar um JSON stringificado ou dict.
            # Aqui retornaremos o texto limpo para o modelo + metadados estruturados se precisar.
            
            verse_text = data.get("text", "").strip()
            ref_out = data.get("reference", reference)
            
            return f"{verse_text} ({ref_out})"
            
        except Exception as e:
            return f"Erro ao buscar versículo: {str(e)}"

# Se rodar direto: python server.py
if __name__ == "__main__":
    mcp.run()
