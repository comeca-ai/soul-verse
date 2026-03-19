from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 706
HEIGHT = 720
PADDING = 28
LINE = (227, 232, 244)
TEXT = (15, 23, 42)
MUTED = (71, 85, 105)
WHITE = (255, 255, 255)
ROOT = Path("/root/soul-verse")
OUTPUT_DIR = ROOT / "output" / "screenshots"


def load_font(size: int, bold: bool = False):
    path = (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    )
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


FONT_XS = load_font(12)
FONT_SM = load_font(14)
FONT_MD = load_font(16)
FONT_LG = load_font(18, bold=True)
FONT_XL = load_font(32, bold=True)
FONT_VERSE = load_font(24)


def hex_color(value: str):
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def rounded(draw, box, fill, outline=LINE, radius=20, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def gradient(image, top: str, bottom: str):
    start = hex_color(top)
    end = hex_color(bottom)
    pixels = image.load()
    for y in range(image.height):
        ratio = y / max(1, image.height - 1)
        color = tuple(int(start[i] * (1 - ratio) + end[i] * ratio) for i in range(3))
        for x in range(image.width):
            pixels[x, y] = color


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = " ".join(current + [word]).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_chip(draw, x, y, text):
    bbox = draw.textbbox((0, 0), text, font=FONT_XS)
    width = bbox[2] - bbox[0] + 24
    rounded(draw, (x, y, x + width, y + 30), WHITE, radius=15)
    draw.text((x + 12, y + 8), text, fill=MUTED, font=FONT_XS)
    return width


def draw_screen(filename, bg1, bg2, hero1, hero2, title, subtitle, chips, verse, reference, reflection, footer):
    image = Image.new("RGB", (WIDTH, HEIGHT))
    gradient(image, bg1, bg2)
    draw = ImageDraw.Draw(image)

    rounded(draw, (0, 0, WIDTH - 1, HEIGHT - 1), (255, 255, 255), radius=30)
    rounded(draw, (0, 0, WIDTH - 1, HEIGHT - 1), None, outline=LINE, radius=30)

    rounded(draw, (PADDING, PADDING, WIDTH - PADDING, 170), hex_color(hero1), outline=hex_color(hero1), radius=26)
    for y in range(PADDING, 171):
        r = (y - PADDING) / max(1, 170 - PADDING)
        color = tuple(int(hex_color(hero1)[i] * (1 - r) + hex_color(hero2)[i] * r) for i in range(3))
        draw.line((PADDING + 1, y, WIDTH - PADDING - 1, y), fill=color, width=1)
    rounded(draw, (PADDING, PADDING, WIDTH - PADDING, 170), None, outline=hex_color(hero1), radius=26)

    draw.text((PADDING + 22, PADDING + 18), "SOULVERSE", fill=(255, 255, 255), font=FONT_XS)
    draw.text((PADDING + 22, PADDING + 42), title, fill=(255, 255, 255), font=FONT_XL)
    sub_lines = wrap_text(draw, subtitle, FONT_MD, WIDTH - PADDING * 2 - 44)
    y = PADDING + 82
    for line in sub_lines[:2]:
      draw.text((PADDING + 22, y), line, fill=(240, 240, 255), font=FONT_MD)
      y += 22

    chip_x = WIDTH - PADDING
    for chip in reversed(chips):
        bbox = draw.textbbox((0, 0), chip, font=FONT_XS)
        w = bbox[2] - bbox[0] + 24
        chip_x -= w
        rounded(draw, (chip_x, 184, chip_x + w, 214), WHITE, radius=15)
        draw.text((chip_x + 12, 192), chip, fill=MUTED, font=FONT_XS)
        chip_x -= 8

    rounded(draw, (PADDING, 232, WIDTH - PADDING, 470), (252, 252, 255), radius=26)
    draw.text((PADDING + 28, 258), "“", fill=(230, 232, 240), font=load_font(72))
    verse_lines = wrap_text(draw, verse, FONT_VERSE, WIDTH - PADDING * 2 - 80)
    y = 286
    for line in verse_lines[:6]:
        draw.text((PADDING + 30, y), line, fill=TEXT, font=FONT_VERSE)
        y += 34
    rounded(draw, (PADDING + 30, 420, PADDING + 210, 452), (243, 244, 246), outline=(243,244,246), radius=16)
    draw.text((PADDING + 44, 429), reference, fill=MUTED, font=FONT_SM)

    rounded(draw, (PADDING, 490, WIDTH - PADDING, 646), (248, 250, 252), radius=24)
    draw.text((PADDING + 20, 510), "REFLEXAO", fill=MUTED, font=FONT_XS)
    reflection_lines = wrap_text(draw, reflection, FONT_MD, WIDTH - PADDING * 2 - 40)
    y = 538
    for line in reflection_lines[:4]:
        draw.text((PADDING + 20, y), line, fill=TEXT, font=FONT_MD)
        y += 24

    draw.text((PADDING, HEIGHT - 30), "Preview do widget SoulVerse", fill=MUTED, font=FONT_SM)
    bbox = draw.textbbox((0, 0), footer, font=FONT_SM)
    draw.text((WIDTH - PADDING - (bbox[2] - bbox[0]), HEIGHT - 30), footer, fill=MUTED, font=FONT_SM)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT_DIR / filename, format="PNG")


draw_screen(
    "soulverse-directory-anxiety.png",
    "#F7F5FF",
    "#EEF2FF",
    "#7C3AED",
    "#2563EB",
    "Respire e entregue isso a Deus",
    "Verso para ansiedade e excesso de preocupacao.",
    ["Ansiedade", "Versiculo exato", "Somente leitura"],
    "Nao andeis ansiosos por coisa alguma; antes, em tudo, sejam os vossos pedidos conhecidos diante de Deus...",
    "Filipenses 4:6-7",
    "Este versiculo relembra que a ansiedade pode ser levada a Deus em oracao, com honestidade e calma.",
    "Consolo espiritual",
)

draw_screen(
    "soulverse-directory-reference.png",
    "#F5F9FF",
    "#EFF6FF",
    "#2563EB",
    "#0891B2",
    "Texto biblico encontrado",
    "Versiculo solicitado pelo usuario.",
    ["Referencia explicita", "API biblica", "Widget"],
    "O SENHOR e o meu pastor; nada me faltara.",
    "Salmos 23:1",
    "Abaixo esta o texto retornado pela API biblica para a referencia solicitada pelo usuario.",
    "Referencia confirmada",
)

draw_screen(
    "soulverse-directory-loneliness.png",
    "#FFF8F2",
    "#FFF1E8",
    "#EA580C",
    "#C2410C",
    "Ha presenca mesmo no silencio",
    "Verso para solidao e sensacao de abandono.",
    ["Solidao", "Acolhimento", "Sem ads"],
    "Nao to mandei eu? Esforca-te, e tem bom animo; nao pasmes, nem te espantes...",
    "Josue 1:9",
    "Mesmo quando o usuario se sente sozinho, o app devolve um versiculo de encorajamento e proximidade.",
    "Apoio devocional",
)
