# Tool Descriptions - SoulVerse

## `get_bible_verse`
Use this tool when you need to retrieve the exact, official text of a Bible verse to comfort or encourage the user.
The user will describe their feelings or situation, and you (the model) should first determine the most appropriate biblical reference (Book Chapter:Verse) to address that emotion. Then, use this tool to fetch the text.
**Do not use for** searching verses by keywords directly if you don't have a reference; rely on your internal knowledge to pick the reference first.

### Inputs
- `reference` (string, required): The Bible reference (e.g., "Salmos 23:4", "Filipenses 4:13").
- `translation` (string, optional): Defaults to "almeida" (Portuguese).

### Hints
- `readOnly`: True (fetches data, no side effects).
- `widgetAccessible`: True (the widget can display the verse beautifully).
