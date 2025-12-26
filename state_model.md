# State Model

## Widget State (`window.openai.widgetState`)

Não precisamos de estado complexo persistido entre turnos para este MVP, pois cada consulta é independente.
Usaremos o estado local do React para gerenciar a exibição do último versículo recebido.

### Campos Planejados (se houver expansão futura)
- `lastVerseId`: string (para evitar re-renderizar o mesmo card se o usuário só comentar "amém") 
