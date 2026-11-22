#!/usr/bin/env python3
"""Render the news-image-20261122 front page: 1024x1024 PNG.

Design: a bold newspaper front page, built for legibility at ~300px.
Two stories genuinely from Sunday 22 November 2026 (verified by search):
  1. COP31 (Antalya) - final deal package agreed at a late-night plenary;
     approval session Sunday 06:00 GMT. Fossil fuels cut from the draft,
     $120bn adaptation target dropped.
  2. G20 summit opens in Johannesburg - first G20 ever held in Africa;
     Ramaphosa hosts; EU leaders meet today on Ukraine + Trump's peace plan.
Deterministic: fixed layout, fixed fonts, no randomness, no network.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

PAPER = (246, 241, 230)
INK = (25, 25, 25)
GREEN = (31, 107, 69)
GREEN_DARK = (22, 77, 50)
GREEN_LIGHT = (46, 125, 91)
GOLD = (198, 152, 40)
GOLD_LIGHT = (232, 196, 90)
BLUE = (27, 79, 114)
BLUE_DARK = (18, 56, 82)
GREY = (90, 86, 76)
WHITE = (255, 255, 255)
CREAM_LINE = (210, 202, 182)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = "DejaVuSerif-Bold.ttf"
SERIF = "DejaVuSerif.ttf"
SANS_B = "DejaVuSans-Bold.ttf"
SANS = "DejaVuSans.ttf"


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, x1, y, fill=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def kicker(draw, x, y, text, color):
    f = font(SANS_B, 20)
    draw.text((x, y), text, font=f, fill=color)
    return y + 26


def draw_globe(draw, cx, cy, r):
    """Stylised globe: gold rays, teal-green disc, abstract continents."""
    # sun rays
    for i in range(12):
        a = math.radians(i * 30)
        x0 = cx + int(math.cos(a) * (r + 12))
        y0 = cy + int(math.sin(a) * (r + 12))
        x1 = cx + int(math.cos(a) * (r + 26))
        y1 = cy + int(math.sin(a) * (r + 26))
        draw.line([(x0, y0), (x1, y1)], fill=GOLD, width=7)
    # disc
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN_LIGHT,
                 outline=GREEN_DARK, width=4)
    # abstract continents (dark green blobs)
    draw.ellipse([cx - r + 18, cy - r + 30, cx - r + 78, cy - r + 78],
                 fill=GREEN_DARK)
    draw.ellipse([cx + 8, cy - r + 58, cx + r - 12, cy - r + 108],
                 fill=GREEN_DARK)
    draw.ellipse([cx - r + 34, cy + 12, cx - r + 96, cy + r - 22],
                 fill=GREEN_DARK)
    draw.ellipse([cx + 22, cy + 34, cx + r - 30, cy + r - 14],
                 fill=GREEN_DARK)
    # latitude arc
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 200, 340,
             fill=WHITE, width=3)
    # two leaves sprouting from the top, splayed apart
    draw.ellipse([cx + 2, cy - r - 36, cx + 36, cy - r + 4], fill=GREEN)
    draw.ellipse([cx - 36, cy - r - 28, cx - 2, cy - r + 10], fill=GREEN_DARK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36  # margin
    R = W - M  # right edge

    # ---------- masthead ----------
    mast = font(SERIF_B, 58)
    t = "THE WORLD IN ONE DAY"
    tw = d.textlength(t, font=mast)
    d.text(((W - tw) / 2, 26), t, font=mast, fill=INK)
    rule(d, M, R, 100, fill=INK, width=3)
    date_f = font(SANS_B, 30)
    dt = "SUNDAY  ·  22 NOVEMBER 2026"
    dw = d.textlength(dt, font=date_f)
    d.text(((W - dw) / 2, 112), dt, font=date_f, fill=INK)
    rule(d, M, R, 152, fill=INK, width=2)

    # ---------- lead: COP31 ----------
    y = kicker(d, M, 168, "CLIMATE  ·  COP31  ·  ANTALYA", GREEN)
    # illustration, left
    draw_globe(d, 200, 350, 118)
    # coastline silhouette under the globe (Antalya: sea + mountains)
    d.polygon([(M, 470), (120, 448), (200, 462), (290, 446), (380, 466),
               (380, 486), (M, 486)], fill=BLUE_DARK)
    d.rectangle([M, 486, 380, 492], fill=GOLD)
    # COP31 badge overlapping the globe
    badge = font(SANS_B, 34)
    bt = "COP31"
    bw = d.textlength(bt, font=badge)
    bx0, by0 = 200 - bw // 2 - 16, 408
    d.rounded_rectangle([bx0, by0, bx0 + bw + 32, by0 + 52], radius=8,
                        fill=GREEN_DARK)
    d.text((bx0 + 16, by0 + 7), bt, font=badge, fill=WHITE)

    # ---------- lead headline + deck (right of globe) ----------
    hx, hw = 420, R - 420
    hf = font(SERIF_B, 56)
    hy = draw_lines(d, ["COP31:", "FINAL DEAL", "IN SIGHT"], hx, 200, hf,
                    INK, 62)
    deck_f = font(SANS, 24)
    deck = ("After talks ran past their Friday deadline, negotiators "
            "agree a final package. Delegates meet this morning to "
            "approve it.")
    draw_lines(d, wrap(d, deck, deck_f, hw), hx, hy + 12, deck_f, INK, 31)

    # ---------- lead bullets (full width) ----------
    by = 512
    bf = font(SANS_B, 22)
    for txt in ("Fossil fuels cut from the draft text",
                "$120bn adaptation target dropped from the draft"):
        d.rectangle([M, by + 6, M + 14, by + 20], fill=GREEN)
        d.text((M + 26, by), txt, font=bf, fill=INK)
        by += 36
    rule(d, M, R, 596, fill=CREAM_LINE, width=2)

    # ---------- G20 ----------
    y = kicker(d, M, 616, "DIPLOMACY  ·  G20  ·  JOHANNESBURG", BLUE)
    gh = font(SERIF_B, 46)
    d.text((M, 652), "G20 OPENS IN AFRICA", font=gh, fill=INK)
    sub_f = font(SANS_B, 24)
    d.text((M, 706), "First summit on African soil", font=sub_f,
           fill=GOLD)
    gdeck_f = font(SANS, 22)
    gdeck = ("President Ramaphosa hosts world leaders in Johannesburg. "
             "Debt, disaster resilience and a just energy transition "
             "top the agenda.")
    gy = draw_lines(d, wrap(d, gdeck, gdeck_f, 620), M, 744, gdeck_f,
                    INK, 28)
    note_f = font(SANS, 19)
    note = ("EU leaders meet today on Ukraine and Trump's peace plan. "
            "Zelenskyy, speaking Saturday, said he would consider "
            "trilateral talks on the sidelines if invited.")
    draw_lines(d, wrap(d, note, note_f, 620), M, gy + 8, note_f, GREY, 24)

    # G20 illustration, right: big G20, gold sun, skyline
    ix0, ix1 = 700, R
    g20_f = font(SANS_B, 76)
    gt = "G20"
    gw = d.textlength(gt, font=g20_f)
    gcx = (ix0 + ix1) // 2
    d.text((gcx - gw / 2, 640), gt, font=g20_f, fill=BLUE_DARK)
    d.ellipse([gcx - 56, 726, gcx + 56, 838], fill=GOLD_LIGHT,
              outline=GOLD, width=3)
    # skyline silhouette
    base = 884
    heights = [52, 84, 64, 104, 72, 92, 58, 78]
    bw_ = (ix1 - ix0) // len(heights)
    for i, hgt in enumerate(heights):
        x0 = ix0 + i * bw_ + 3
        d.rectangle([x0, base - hgt, x0 + bw_ - 6, base], fill=BLUE_DARK)
    d.rectangle([ix0, base, ix1, base + 2], fill=BLUE_DARK)

    # ---------- ALSO strip ----------
    d.rectangle([M, 906, R, 968], fill=INK)
    also_f = font(SANS, 19)
    also = ("ALSO:  COP31 objections due 03:00 GMT · approval session "
            "06:00 GMT   •   G20 theme: Solidarity, Equality, "
            "Sustainability   •   EU leaders meet today on Ukraine")
    ay = draw_lines(d, wrap(d, also, also_f, R - M - 28), M + 14, 916,
                    also_f, WHITE, 25)

    # ---------- footer ----------
    foot_f = font(SANS_B, 16)
    ft = "ALL STORIES REPORTED ON 22 NOVEMBER 2026"
    fw = d.textlength(ft, font=foot_f)
    d.text(((W - fw) / 2, 980), ft, font=foot_f, fill=GREY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
