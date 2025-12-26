# Review Notes

## Limitações Conhecidas (MVP)
- A API pública `bible-api.com` pode ter rate limits não documentados, embora seja generosa.
- A tradução "Almeida" disponível na API pode ter pequenas variações de grafia arcaica.
- O widget não persiste histórico entre sessões (design choice para privacidade).

## Fallback Behaviors
- Se a API falhar, o servidor retorna erro "Erro ao buscar versículo...", que deve ser tratado pelo modelo pedindo desculpas ao usuário.
