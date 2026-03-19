# Tool Descriptions - SoulVerse

## `get_comfort_verse`
Use esta tool quando o usuario descrever como esta se sentindo e precisar de conforto espiritual com um versiculo apropriado.

### O que ela faz
- identifica o tema emocional principal do usuario
- escolhe uma referencia biblica adequada
- consulta o texto exato na API biblica publica
- retorna um payload pronto para o widget exibir

### Inputs
- `feeling` (string, obrigatorio): descricao curta do estado emocional do usuario
- `translation` (string, opcional): atualmente `almeida`

### Hints
- `readOnly`: `true`
- `consequenceFree`: `true`
- `widgetAccessible`: `true`

## `get_bible_verse`
Use esta tool quando o usuario informar uma referencia biblica explicita ou pedir o texto exato de uma passagem.

### O que ela faz
- valida a referencia recebida
- consulta o texto exato na API biblica publica
- retorna um payload pronto para o widget exibir

### Inputs
- `reference` (string, obrigatorio): referencia biblica no formato `Livro Capitulo:Versiculo`
- `translation` (string, opcional): atualmente `almeida`

### Hints
- `readOnly`: `true`
- `consequenceFree`: `true`
- `widgetAccessible`: `true`
