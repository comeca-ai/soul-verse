# SoulVerse

SoulVerse e um app MCP com widget para trazer versiculos biblicos de conforto com texto preciso, baseado no sentimento do usuario ou em uma referencia explicita.

## O que o app faz

- busca um versiculo de conforto a partir do sentimento informado
- busca o texto exato de uma referencia biblica explicita
- exibe o resultado em um card visual no widget

## Estrutura real do repositorio

- `server.py`: MCP server em Python com as tools
- `web/`: widget React/Vite
- `toolset.json`: definicao das tools
- `app_spec.json`: especificacao original do app

## Como rodar o backend

```bash
cd /root/soul-verse
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python server.py
```

## Como rodar o widget

```bash
cd /root/soul-verse/web
npm install
npm run dev
```

## Estado atual do MVP

- tool principal: `get_comfort_verse`
- tool secundaria: `get_bible_verse`
- widget com leitura de `window.openai.toolOutput` e fallback local para preview

## Observacoes

- o app depende de `bible-api.com` para obter o texto biblico exato
- a traducao atual suportada e `almeida`
- o app nao substitui apoio pastoral, psicologico ou medico
