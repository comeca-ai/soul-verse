from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import quote

import httpx
from fastmcp import FastMCP


mcp = FastMCP(
    "SoulVerse",
    instructions=(
        "Fornece versiculos biblicos de conforto com texto exato, com base no "
        "sentimento do usuario ou em uma referencia biblica explicita."
    ),
)

DEFAULT_TRANSLATION = "almeida"
ALLOWED_TRANSLATIONS = {"almeida"}
BIBLE_API_BASE_URL = "https://bible-api.com"


@dataclass(frozen=True)
class ComfortProfile:
    theme: str
    reference: str
    heading: str
    subheading: str
    reflection: str
    follow_up: str
    theme_color: str
    keywords: tuple[str, ...]


COMFORT_PROFILES: tuple[ComfortProfile, ...] = (
    ComfortProfile(
        theme="ansiedade",
        reference="Filipenses 4:6-7",
        heading="Respire e entregue isso a Deus",
        subheading="Verso para ansiedade e excesso de preocupacao.",
        reflection="Este versiculo lembra que a ansiedade pode ser levada a Deus em oracao, com honestidade e calma.",
        follow_up="Se quiser, eu posso trazer outro versiculo mais focado em paz e descanso.",
        theme_color="#7c3aed",
        keywords=("ansioso", "ansiedade", "preocupado", "preocupacao", "nervoso", "aflito", "aflicao"),
    ),
    ComfortProfile(
        theme="medo",
        reference="Isaias 41:10",
        heading="Voce nao precisa atravessar isso sozinho",
        subheading="Verso para medo, inseguranca e fragilidade.",
        reflection="A promessa central aqui e a presenca de Deus sustentando voce mesmo quando o medo parece dominar.",
        follow_up="Quer que eu busque um versiculo mais voltado para coragem?",
        theme_color="#2563eb",
        keywords=("medo", "com medo", "assustado", "inseguro", "inseguranca", "pavor"),
    ),
    ComfortProfile(
        theme="tristeza",
        reference="Salmos 34:18",
        heading="Deus esta perto do coracao ferido",
        subheading="Verso para tristeza, dor e abatimento.",
        reflection="Quando a dor aperta, este texto aponta para a proximidade de Deus com quem esta quebrantado.",
        follow_up="Se quiser, posso trazer outro versiculo mais voltado a consolo e esperanca.",
        theme_color="#0f766e",
        keywords=("triste", "tristeza", "abatido", "abatida", "desanimado", "desanimada", "dor"),
    ),
    ComfortProfile(
        theme="solidao",
        reference="Josue 1:9",
        heading="Ha presenca mesmo no silencio",
        subheading="Verso para solidao e sensacao de abandono.",
        reflection="Este versiculo reforca que a companhia de Deus nao depende do quanto voce se sente acompanhado agora.",
        follow_up="Quer que eu traga outro versiculo mais voltado a companhia e cuidado?",
        theme_color="#ea580c",
        keywords=("sozinho", "sozinha", "solidao", "abandonado", "abandonada"),
    ),
    ComfortProfile(
        theme="culpa",
        reference="1 Joao 1:9",
        heading="Ha espaco para confessar e recomecar",
        subheading="Verso para culpa, arrependimento e restauracao.",
        reflection="O foco aqui nao e a condenacao, mas a sinceridade diante de Deus e a possibilidade real de restauracao.",
        follow_up="Se quiser, eu posso trazer um versiculo mais focado em perdao e nova vida.",
        theme_color="#dc2626",
        keywords=("culpa", "culpado", "culpada", "arrependido", "arrependida", "pecado", "errei"),
    ),
    ComfortProfile(
        theme="cansaco",
        reference="Mateus 11:28",
        heading="Existe descanso para a alma cansada",
        subheading="Verso para exaustao, sobrecarga e peso emocional.",
        reflection="Este chamado de Jesus fala diretamente a quem esta sobrecarregado e sem folego para continuar sozinho.",
        follow_up="Quer que eu traga outro versiculo mais voltado a renovar as forcas?",
        theme_color="#0891b2",
        keywords=("cansado", "cansada", "exausto", "exausta", "sobrecarregado", "sobrecarregada", "esgotado", "esgotada"),
    ),
    ComfortProfile(
        theme="confusao",
        reference="Proverbios 3:5-6",
        heading="Direcao para quando tudo parece nebuloso",
        subheading="Verso para confusao, duvida e falta de direcao.",
        reflection="Este texto convida a confiar em Deus mesmo quando voce ainda nao enxerga todo o caminho.",
        follow_up="Se quiser, eu posso trazer outro versiculo mais focado em sabedoria.",
        theme_color="#4f46e5",
        keywords=("confuso", "confusa", "perdido", "perdida", "duvida", "duvidas", "sem rumo", "indeciso", "indecisa"),
    ),
)

REFERENCE_PATTERN = re.compile(
    r"^(?P<book>[1-3]?\s?[A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+)*)\s+(?P<chapter>\d+):(?P<verse>\d+(?:-\d+)?)$"
)


def sanitize_translation(translation: str) -> str:
    translation = translation.strip().lower()
    if translation not in ALLOWED_TRANSLATIONS:
        return DEFAULT_TRANSLATION
    return translation


def parse_reference(reference: str) -> dict[str, str]:
    normalized = " ".join(reference.strip().split())
    match = REFERENCE_PATTERN.match(normalized)
    if not match:
        return {
            "reference": normalized,
            "book": normalized,
            "chapter": "",
            "verse": "",
        }

    return {
        "reference": normalized,
        "book": match.group("book"),
        "chapter": match.group("chapter"),
        "verse": match.group("verse"),
    }


def normalize_feeling(feeling: str) -> str:
    return " ".join(feeling.strip().lower().split())


def pick_comfort_profile(feeling: str) -> ComfortProfile:
    normalized = normalize_feeling(feeling)

    for profile in COMFORT_PROFILES:
        if any(keyword in normalized for keyword in profile.keywords):
            return profile

    return ComfortProfile(
        theme="consolo",
        reference="Salmos 46:1",
        heading="Deus e socorro bem presente",
        subheading="Verso de acolhimento geral para tempos dificeis.",
        reflection="Mesmo sem rotular exatamente o que voce sente, este versiculo aponta para refugio e ajuda no meio da angustia.",
        follow_up="Se quiser, eu posso trazer um versiculo mais especifico para o que voce esta sentindo.",
        theme_color="#0f766e",
        keywords=(),
    )


async def fetch_verse(reference: str, translation: str) -> dict[str, Any]:
    encoded_reference = quote(reference)
    url = f"{BIBLE_API_BASE_URL}/{encoded_reference}?translation={translation}"

    async with httpx.AsyncClient(timeout=12.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    verse_text = data.get("text", "").strip()
    reference_out = data.get("reference", reference).strip()

    if not verse_text:
        raise ValueError("A API nao retornou texto para a referencia solicitada.")

    parsed = parse_reference(reference_out)
    return {
        "reference": reference_out,
        "book": parsed["book"],
        "chapter": parsed["chapter"],
        "verse": parsed["verse"],
        "text": verse_text,
        "translation": translation,
    }


def verse_payload(
    *,
    theme: str,
    heading: str,
    subheading: str,
    reflection: str,
    follow_up: str,
    theme_color: str,
    feeling: str,
    verse: dict[str, Any],
) -> dict[str, Any]:
    return {
        "kind": "verse_card",
        "theme": theme,
        "feeling": feeling,
        "display": {
            "heading": heading,
            "subheading": subheading,
            "reference": verse["reference"],
            "book": verse["book"],
            "chapter": verse["chapter"],
            "verse": verse["verse"],
            "full_text": verse["text"],
            "translation": verse["translation"],
            "theme_color": theme_color,
        },
        "reflection": reflection,
        "suggested_follow_up": follow_up,
        "limitations": [
            "O texto do versiculo vem de uma API biblica publica.",
            "O app nao substitui cuidado pastoral, psicologico ou medico.",
        ],
    }


def error_payload(message: str, suggestion: str) -> dict[str, Any]:
    return {
        "kind": "error_card",
        "title": "Nao foi possivel buscar o versiculo",
        "message": message,
        "suggestion": suggestion,
    }


@mcp.tool()
async def get_comfort_verse(
    feeling: str,
    translation: str = DEFAULT_TRANSLATION,
) -> dict[str, Any]:
    """
    Use esta tool quando o usuario expressar um sentimento, desabafo ou necessidade de conforto espiritual.

    Ela escolhe uma referencia biblica apropriada para o estado emocional descrito e busca o texto exato
    em uma API biblica publica, retornando um payload pronto para o card do widget.
    """
    cleaned_feeling = " ".join(feeling.strip().split())
    if len(cleaned_feeling) < 2:
        return error_payload(
            "Descreva um pouco melhor como voce esta se sentindo para eu encontrar um versiculo adequado.",
            "Exemplo: 'estou muito ansioso com o trabalho'.",
        )

    translation = sanitize_translation(translation)
    profile = pick_comfort_profile(cleaned_feeling)

    try:
        verse = await fetch_verse(profile.reference, translation)
    except Exception as exc:
        return error_payload(
            f"Falha ao consultar a API biblica para {profile.reference}: {exc}",
            "Tente novamente em instantes ou me passe uma referencia biblica especifica.",
        )

    return verse_payload(
        theme=profile.theme,
        heading=profile.heading,
        subheading=profile.subheading,
        reflection=profile.reflection,
        follow_up=profile.follow_up,
        theme_color=profile.theme_color,
        feeling=cleaned_feeling,
        verse=verse,
    )


@mcp.tool()
async def get_bible_verse(
    reference: str,
    translation: str = DEFAULT_TRANSLATION,
) -> dict[str, Any]:
    """
    Use esta tool quando o usuario fornecer uma referencia biblica explicita ou pedir o texto exato de um versiculo.

    Ela busca o texto oficial da referencia informada e retorna um payload pronto para o widget.
    """
    cleaned_reference = " ".join(reference.strip().split())
    if len(cleaned_reference) < 3:
        return error_payload(
            "Referencia biblica invalida ou muito curta.",
            "Use algo como 'Salmos 23:1' ou 'Joao 3:16'.",
        )

    translation = sanitize_translation(translation)

    try:
        verse = await fetch_verse(cleaned_reference, translation)
    except Exception as exc:
        return error_payload(
            f"Falha ao consultar a API biblica para {cleaned_reference}: {exc}",
            "Confira a referencia informada e tente novamente.",
        )

    return verse_payload(
        theme="referencia",
        heading="Texto biblico encontrado",
        subheading="Versiculo solicitado pelo usuario.",
        reflection="Abaixo esta o texto retornado pela API biblica para a referencia informada.",
        follow_up="Se quiser, posso trazer um versiculo relacionado ao mesmo tema.",
        theme_color="#4f46e5",
        feeling="referencia explicita",
        verse=verse,
    )


@mcp.prompt()
def soul_verse_system() -> str:
    return """
Voce e o assistente "SoulVerse".

Missao
- Trazer conforto espiritual com versiculos biblicos relevantes e texto preciso.
- Sempre responder com sensibilidade, clareza e acolhimento.

Uso das tools
1) Se o usuario expressar um sentimento, desabafo, medo, tristeza, culpa, cansaco, ansiedade ou solidao:
   - Chame primeiro `get_comfort_verse`.
2) Se o usuario informar uma referencia biblica explicita:
   - Chame `get_bible_verse`.
3) Nunca cite o texto biblico de memoria quando a tool puder ser usada.

Formato de resposta
- Entregue primeiro o versiculo e a referencia.
- Depois, conecte o texto a situacao do usuario em 1 a 3 frases.
- Termine com uma pergunta curta de continuidade.

Tom
- Gentil, respeitoso, sem julgamento e sem moralismo.
- Responda no idioma do usuario.

Seguranca
- Se houver risco de autoagressao, suicidio ou violencia iminente, priorize encorajar ajuda humana imediata e servicos de emergencia locais.
- Depois disso, se apropriado, ofereca um versiculo de apoio usando a tool.
"""


if __name__ == "__main__":
    mcp.run()
