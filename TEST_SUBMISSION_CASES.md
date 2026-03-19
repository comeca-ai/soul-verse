# SoulVerse Test Cases

## Test Case 1

- Scenario: the user expresses anxiety and wants a comforting verse
- User prompt: `Estou muito ansioso com o trabalho. Me traga um versiculo para isso.`
- Tool triggered: `get_comfort_verse`
- Expected output: the app should return a comforting verse card for anxiety, with a heading, exact verse text, reference, short reflection, and a follow-up suggestion

## Test Case 2

- Scenario: the user expresses loneliness and wants spiritual comfort
- User prompt: `Estou me sentindo muito sozinho ultimamente.`
- Tool triggered: `get_comfort_verse`
- Expected output: the app should return a verse card themed around loneliness, companionship, or coragem, with exact verse text and a brief supportive reflection

## Test Case 3

- Scenario: the user asks for the exact text of a specific Bible reference
- User prompt: `Me mostre o texto de Salmos 23:1.`
- Tool triggered: `get_bible_verse`
- Expected output: the app should return a verse card for the explicit reference, including the exact verse text from the Bible API and the requested reference

## Test Case 4

- Scenario: the user feels guilty and asks for a verse about forgiveness
- User prompt: `Estou com muita culpa pelo que fiz. Tem algum versiculo para isso?`
- Tool triggered: `get_comfort_verse`
- Expected output: the app should return a verse card associated with forgiveness, confession, or restoration, with supportive but non-judgmental language

## Test Case 5

- Scenario: the user is exhausted and wants a verse about rest
- User prompt: `Estou cansado e sobrecarregado. Quero uma palavra de descanso.`
- Tool triggered: `get_comfort_verse`
- Expected output: the app should return a verse card centered on rest, comfort, or renewal, with exact verse text and a short reflection

## Test Case 6

- Scenario: the user provides an invalid or malformed reference
- User prompt: `Me mostre o texto de LivroInexistente 99:99.`
- Tool triggered: `get_bible_verse`
- Expected output: the app should return an error card explaining that the verse could not be fetched and suggest checking the reference
