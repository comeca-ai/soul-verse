# Data Contract: `get_bible_verse`

## Input (do Modelo para a Tool)
```json
{
  "reference": "Salmos 23:1",
  "translation": "almeida"
}
```

## Output (da Tool para o Modelo/Widget)

### `structuredContent` (O que o modelo lê para gerar a resposta textual)
```json
{
  "success": true,
  "reference": "Salmos 23:1",
  "text": "O SENHOR é o meu pastor, nada me faltará.",
  "translation_id": "almeida"
}
```

### `_meta` (O que o Widget usa para renderizar o Card rico)
```json
{
  "kind": "verse_card",
  "display": {
    "book": "Salmos",
    "chapter": "23",
    "verse": "1",
    "full_text": "O SENHOR é o meu pastor, nada me faltará.",
    "theme_color": "#4A90E2" 
  }
}
```
