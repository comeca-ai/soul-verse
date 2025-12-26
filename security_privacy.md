# Security & Privacy

## Validação
- **Server-side Zod Validation**: O MCP Server valida se "reference" segue padrão básico de string antes de chamar a API externa.
- **Sanatization**: O texto retornado pela API externa é tratado como Plain Text para evitar XSS antes de ser enviado ao widget.

## Privacidade
- **Zero Persistência**: Não salvamos logs das emoções do usuário.
- **Anonimato**: A chamada para a API externa (bible-api.com) não envia dados do usuário, apenas a referência bíblica (ex: "request: John 3:16").

## Logs
- Apenas logs de erro de conexão ("Failed to fetch API") sem detalhes do conteúdo do prompt.
