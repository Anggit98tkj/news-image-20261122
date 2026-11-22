#!/usr/bin/env python3
"""Draw the 1024x1024 front page summing up Sunday 22 November 2026.

Pure Python + PIL, no network, no downloaded art: every picture on the
page is drawn here from shapes. Run: python3 draw.py  (writes entry.png)
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (24, 42, 84)
GOLD = (198, 154, 52)

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF = FD + "DejaVuSerif-Bold.ttf"
SERIF_R = FD + "DejaVuSerif.ttf"
SANS = FD + "DejaVuSans.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines fitting width."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=1.25):
    """Draw wrapped paragraph, return y just below it."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def rule(draw, x0, y, x1, w=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=w)


def burst(draw, cx, cy, r, fill):
    """Starburst: alternating long/short spikes around a centre."""
    import math
    pts = []
    for i in range(24):
        ang = math.pi * i / 12
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

# ---- Masthead -------------------------------------------------------
d.text((W // 2, 34), "THE WORLD IN ONE DAY", font=font(SERIF, 62),
       fill=INK, anchor="ma")
d.text((W // 2, 108), "SUNDAY 22 NOVEMBER 2026  |  ONE DAY, SIX STORIES, THE WORLD",
       font=font(SANS_B, 21), fill=RED, anchor="ma")
rule(d, 28, 146, W - 28, 3)
rule(d, 28, 152, W - 28, 1)

# ---- Lead story: Gulf strikes ---------------------------------------
LY = 168
d.text((28, LY), "IRAN STRIKES US BASES", font=font(SERIF, 32), fill=INK)
d.text((28, LY + 42), "IN THE GULF", font=font(SERIF, 32), fill=INK)
d.text((28, LY + 92), "Missiles hit a US air base in Kuwait and an",
       font=font(SANS, 21), fill=INK)
d.text((28, LY + 118), "industrial site in Bahrain; defences shoot",
       font=font(SANS, 21), fill=INK)
d.text((28, LY + 144), "down other incoming attacks as the region",
       font=font(SANS, 21), fill=INK)
d.text((28, LY + 170), "braces for what comes next.",
       font=font(SANS, 21), fill=INK)
d.text((28, LY + 206), "Sources: Reuters, Al Jazeera",
       font=font(SANS, 15), fill=(90, 90, 90))

# Lead illustration: night sky over the Gulf, explosion, base, sea.
AX, AY, AW, AH = 560, 168, 436, 196
d.rectangle([AX, AY, AX + AW, AY + AH], fill=(16, 28, 58))
d.rectangle([AX, AY + 150, AX + AW, AY + AH], fill=(30, 80, 110))
for bx, bw, bh in [(AX + 30, 90, 46), (AX + 150, 70, 64), (AX + 250, 110, 40)]:
    d.rectangle([bx, AY + 150 - bh, bx + bw, AY + 150], fill=(52, 58, 74))
    for wx in range(bx + 8, bx + bw - 8, 18):
        d.rectangle([wx, AY + 150 - bh + 8, wx + 8, AY + 150 - bh + 18],
                    fill=(240, 200, 90))
burst(d, AX + 330, AY + 62, 52, (255, 140, 40))
burst(d, AX + 330, AY + 62, 30, (255, 210, 90))
burst(d, AX + 120, AY + 48, 26, (255, 170, 70))
d.text((AX + 14, AY + AH - 34), "THE GULF, OVERNIGHT",
       font=font(SANS_B, 16), fill=(255, 255, 255))
rule(d, 28, 404, W - 28, 2)

# ---- Five more stories in a 3 + 2 grid, plus an "Also" box ----------
CELLS = [
    ("MEXICO CAPTURES\n'EL CHAPO ISIDRO'",
     "Troops seize one of the FBI's most-wanted cartel bosses in Sinaloa. "
     "Source: Reuters.",
     "cartel"),
    ("EU AND INDONESIA\nSIGN TRADE DEAL",
     "After ten years of talks, the pact scraps 98.5% of tariffs between "
     "Europe and Southeast Asia's largest economy.",
     "trade"),
    ("ALCARAZ TO FACE\nZVEREV IN FINAL",
     "Alcaraz fights back past Ben Shelton to set up an ATP Finals title "
     "decider against world No. 1 Zverev. Source: BBC Sport.",
     "tennis"),
    ("FOUR NATIONS URGE\nAID INTO FLOODED GAZA",
     "Australia, Canada, Italy and the UK call on Israel to allow immediate, "
     "unrestricted humanitarian access as floods hit Gaza.",
     "aid"),
    ("FRANCE PROTESTS\nENTER 4TH WEEKEND",
     "Nationwide demonstrations over the rising cost of living roll into a "
     "fourth straight weekend across the country.",
     "protest"),
]
CW, CH, GX, GY = 312, 252, 28, 412
GAP = 20


def art_cartel(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 214, 176))
    d.ellipse([x + 60, y + 22, x + 120, y + 82], outline=INK, width=7)
    d.ellipse([x + 172, y + 22, x + 232, y + 82], outline=INK, width=7)
    d.rectangle([x + 116, y + 42, x + 176, y + 62], fill=INK)
    d.text((x + w // 2, y + h - 30), "WANTED", font=font(SANS_B, 24),
           fill=RED, anchor="ma")


def art_trade(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 228, 240))
    d.rectangle([x + 30, y + 18, x + 130, y + 80], fill=(0, 51, 153))
    for k in range(12):
        import math
        a = math.pi * k / 6
        d.ellipse([x + 80 + 24 * math.cos(a) - 3, y + 49 + 24 * math.sin(a) - 3,
                   x + 80 + 24 * math.cos(a) + 3, y + 49 + 24 * math.sin(a) + 3],
                  fill=(255, 204, 0))
    d.rectangle([x + 172, y + 18, x + 272, y + 80], fill=(255, 255, 255))
    d.rectangle([x + 172, y + 18, x + 272, y + 49], fill=(206, 17, 38))
    d.text((x + w // 2, y + h - 30), "98.5% OF TARIFFS GO",
           font=font(SANS_B, 20), fill=NAVY, anchor="ma")


def art_tennis(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(58, 124, 68))
    d.rectangle([x + 18, y + 14, x + w - 18, y + h - 44], outline=(255, 255, 255),
                width=3)
    d.line([(x + 18, y + (h - 30) // 2), (x + w - 18, y + (h - 30) // 2)],
           fill=(255, 255, 255), width=3)
    d.ellipse([x + w - 78, y + 24, x + w - 38, y + 64], fill=(210, 230, 60),
              outline=INK, width=2)
    d.text((x + w // 2, y + h - 30), "ATP FINALS, TURIN",
           font=font(SANS_B, 20), fill=(255, 255, 255), anchor="ma")


def art_aid(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(196, 222, 235))
    for bx in (x + 40, x + 150):
        d.rectangle([bx, y + 44, bx + 92, y + 96], fill=(222, 184, 120),
                    outline=INK, width=3)
        d.rectangle([bx + 36, y + 60, bx + 56, y + 90], fill=RED)
        d.rectangle([bx + 31, y + 70, bx + 61, y + 80], fill=RED)
    for rx in range(x + 24, x + w - 10, 44):
        d.line([(rx, y + 12), (rx - 8, y + 32)], fill=(40, 90, 160), width=4)
    d.text((x + w // 2, y + h - 30), "LET THE AID THROUGH",
           font=font(SANS_B, 20), fill=NAVY, anchor="ma")


def art_protest(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 226, 200))
    for px, py in [(x + 60, y + 78), (x + 140, y + 88), (x + 220, y + 78)]:
        d.ellipse([px - 20, py - 20, px + 20, py + 20], fill=(222, 184, 150),
                  outline=INK, width=3)
        d.arc([px - 36, py + 6, px + 36, py + 42], 180, 360, fill=INK, width=7)
    d.rectangle([x + 96, y + 12, x + 206, y + 44], fill=(255, 255, 255),
                outline=INK, width=3)
    d.text((x + 151, y + 17), "ENOUGH", font=font(SANS_B, 18), fill=RED,
           anchor="ma")


ARTS = {"cartel": art_cartel, "trade": art_trade, "tennis": art_tennis,
        "aid": art_aid, "protest": art_protest}

for i, (head, body, kind) in enumerate(CELLS):
    col, row = i % 3, i // 3
    x = GX + col * (CW + GAP)
    y = GY + row * (CH + GAP)
    ARTS[kind](x, y, CW, 132)
    yy = y + 140
    for ln in head.split("\n"):
        d.text((x, yy), ln, font=font(SERIF, 21), fill=INK)
        yy += 26
    para(d, x, yy, body, font(SANS, 14), CW, leading=1.3)

# "Also in the news" box (bottom right cell).
bx = GX + 2 * (CW + GAP)
by = GY + 1 * (CH + GAP)
d.rectangle([bx, by, bx + CW, by + CH], fill=(232, 228, 214), outline=INK,
            width=2)
d.text((bx + 14, by + 12), "ALSO IN THE NEWS", font=font(SANS_B, 20), fill=RED)
para(d, bx + 14, by + 48,
     "Strong quake shakes Peru's Andes; no damage or casualties reported.",
     font(SANS, 16), CW - 28, leading=1.3)
para(d, bx + 14, by + 128,
     "Israel's president asks ex-army chief Gadi Eisenkot to try to form "
     "the next government, bypassing Netanyahu.",
     font(SANS, 16), CW - 28, leading=1.3)

# ---- Footer -----------------------------------------------------------
FY = GY + 2 * CH + GAP + 12
rule(d, 28, FY, W - 28, 2)
d.text((W // 2, FY + 12),
       "All six stories were reported on Sunday 22 November 2026.",
       font=font(SANS_B, 18), fill=INK, anchor="ma")
d.text((W // 2, FY + 40),
       "Front page drawn in code. No photographs. THE WORLD IN ONE DAY.",
       font=font(SANS, 15), fill=(90, 90, 90), anchor="ma")

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
