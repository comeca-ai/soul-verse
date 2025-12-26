# Widget CSP (Content Security Policy)

Como o widget roda dentro do ambiente sandboxed do ChatGPT:

```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  connect-src 'self'; 
  img-src 'self' data:;
  style-src 'self' 'unsafe-inline';
  script-src 'self' 'unsafe-inline';
">
```

**Nota:** `connect-src 'self'` é suficiente pois a comunicação de dados ocorre via `window.openai` (bridge), não via fetch direto do browser para a internet. O MCP server (backend) é quem acessa a internet.
