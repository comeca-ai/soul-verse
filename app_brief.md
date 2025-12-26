# App Brief: SoulVerse (Conforto Diário)

## Problema
As pessoas frequentemente enfrentam momentos diários de ansiedade, tristeza ou incerteza e buscam conforto espiritual rápido, mas podem ter dificuldade em localizar passagens bíblicas específicas que abordem seus sentimentos no momento exato.

## Público
Pessoas que buscam apoio espiritual, encorajamento e conforto na fé cristã, de forma rápida e contextualizada com seu estado emocional.

## Cenário Principal
O usuário diz como está se sentindo (ex: "estou muito ansioso com o trabalho" ou "me sentindo sozinho"). O assistente consulta uma API bíblica e retorna um versículo específico de conforto/sabedoria, interpretando a emoção do usuário para fazer a busca correta.

## Valor (Por que um App?)
Diferente de apenas pedir ao ChatGPT (que alucina ou cita de memória), este app consulta uma fonte externa (API Bíblia) garantindo que o texto seja a exata tradução consagrada (Almeida/NVI) e formata a entrega visualmente para leitura reflexiva.

## Intenção Principal (MVP)
`get_comfort_verse`: Buscar versículos baseados em palavras-chave de sentimento/tema.

## Non-Goals (O que NÃO é agora)
- Plano de leitura bíblica anual.
- Exegese ou estudos teológicos profundos.
- Rede social de oração.
- Histórico complexo ou login de usuário.

## Integrações
- **Bible API** (bible-api.com) ou **ABíbliaDigital**: Para buscar o texto sagrado em português (versão Almeida).

## Dados Sensíveis/PII
- **Não**. O sentimento do usuário é efêmero e usado apenas para a consulta. Não armazenamos identidade.
