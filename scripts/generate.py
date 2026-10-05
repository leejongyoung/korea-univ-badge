#!/usr/bin/env python3
"""Generate self-contained Republic of Korea University SVG badges."""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIVERSITIES = ROOT / "universities.json"
LOGOS_DIR = ROOT / "assets" / "logos"
OUTPUT = ROOT / "badges"
STYLES = ("flat", "flat-square", "plastic", "for-the-badge", "outline")

# 6대 공통 프리셋 테마 (학교 고유 상징색 외에 사용 가능)
COLOR_THEMES = {
    "blue": {
        "message_color": "#134f8c",
        "stroke_color": "#134f8c",
    },
    "navy": {
        "message_color": "#003764",
        "stroke_color": "#003764",
    },
    "black": {
        "message_color": "#24292f",
        "stroke_color": "#24292f",
    },
    "green": {
        "message_color": "#1a7f37",
        "stroke_color": "#1a7f37",
    },
    "red": {
        "message_color": "#cf222e",
        "stroke_color": "#cf222e",
    },
    "gray": {
        "message_color": "#57606a",
        "stroke_color": "#57606a",
    },
}

SLUG_PATTERN = re.compile(r"[a-z0-9_-]+\Z")
SVG_NS = "{http://www.w3.org/2000/svg}"

ET.register_namespace("", "http://www.w3.org/2000/svg")
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


def load_universities():
    data = json.loads(UNIVERSITIES.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("universities.json must contain a nonempty list of universities")
    ids = set()
    names = set()
    short_names = set()
    for item in data:
        univ_id = item.get("id")
        name = item.get("name")
        short_name = item.get("short_name")
        en_short = item.get("en_short")
        brand_color = item.get("brand_color")
        if not univ_id or not SLUG_PATTERN.fullmatch(univ_id):
            raise ValueError(f"invalid university id: {univ_id!r}")
        if not name or not en_short or not short_name or not brand_color:
            raise ValueError(f"university missing required fields: {item!r}")
        if univ_id in ids:
            raise ValueError(f"duplicate university id: {univ_id}")
        if name in names:
            raise ValueError(f"duplicate university name: {name}")
        if short_name in short_names:
            raise ValueError(f"duplicate university short_name: {short_name}")
        ids.add(univ_id)
        names.add(name)
        short_names.add(short_name)
    return data


def clean_inner_svg(element):
    raw = ET.tostring(element, encoding="unicode")
    return re.sub(r'\s+xmlns(:\w+)?="http://www\.w3\.org/2000/svg"', "", raw)


def load_logos():
    logos = {}
    for p in LOGOS_DIR.glob("*.svg"):
        root = ET.parse(p).getroot()
        vb = root.get("viewBox")
        if vb:
            parts = [float(x) for x in vb.split()]
            min_x, min_y, vb_w, vb_h = parts[0], parts[1], parts[2], parts[3]
        else:
            min_x = 0.0
            min_y = 0.0
            vb_w = float(root.get("width", 100))
            vb_h = float(root.get("height", 100))

        inner = []
        for child in root:
            tag = child.tag.split("}")[-1]
            if tag in ("metadata", "namedview"):
                continue
            inner.append(clean_inner_svg(child))

        content = "".join(inner)
        logos[p.stem] = (min_x, min_y, vb_w, vb_h, content)

    if "univ" not in logos:
        raise ValueError("assets/logos/univ.svg is required")

    return logos


def is_korean(text):
    return any(ord(c) >= 128 for c in text)


def render_badge(label_text, message_text, style, logo_key, logos, color_theme="brand", custom_colors=None, brand_color="#003876"):
    if style not in STYLES:
        raise ValueError(f"unsupported badge style: {style!r}")
    if logo_key not in logos:
        # Fallback to univ if specific logo doesn't exist
        logo_key = "univ" if "univ" in logos else logo_key
        if logo_key not in logos:
            raise ValueError(f"unsupported logo key: {logo_key!r}")

    prominent = style == "for-the-badge"
    outlined = style == "outline"
    glossy = style == "plastic"
    squared = style in ("flat-square", "for-the-badge")

    height = 28 if prominent else 22 if outlined else 20
    min_x, min_y, vb_w, vb_h, content = logos[logo_key]
    aspect = vb_w / vb_h if vb_h > 0 else 1.0

    if aspect > 1.8:
        target_h = 14.5 if prominent else 10.5
        max_w = 44.0 if prominent else 34.0
        scale = min(max_w / vb_w, target_h / vb_h)
    else:
        max_icon_h = 18.0 if prominent else 14.0
        max_icon_w = 26.0 if prominent else 20.0
        scale = min(max_icon_w / vb_w, max_icon_h / vb_h)

    icon_w = vb_w * scale
    icon_h = vb_h * scale
    icon_x = 6
    icon_y = (height - icon_h) / 2
    tx = icon_x - min_x * scale
    ty = icon_y - min_y * scale

    text_x = round(icon_x + icon_w + (7 if prominent else 6), 2)
    is_ko_label = is_korean(label_text)
    is_ko_msg = is_korean(message_text)

    char_w_label = 12 if (prominent and is_ko_label) else 11 if is_ko_label else (9 if prominent else 8)
    label_width = round(text_x + len(label_text) * char_w_label + (14 if prominent else 10), 1)

    char_w_msg = 12 if (prominent and is_ko_msg) else 11 if is_ko_msg else (9 if prominent else 8)
    message_width = max(48 if not prominent else 58, round(len(message_text) * char_w_msg + (24 if prominent else 20), 1))

    width = label_width + message_width
    radius = 0 if squared else 4

    # 색상 결정 (커스텀 색상 우선, 프리셋 테마 또는 대학 고유 상징색)
    if custom_colors:
        raw_msg_col = custom_colors.get("message_color", brand_color)
        raw_lbl_col = custom_colors.get("label_color", "#ffffff")
        raw_txt_col = custom_colors.get("text_color", "#1f2328")
        raw_ver_col = custom_colors.get("version_color", "#ffffff")
        raw_strk_col = custom_colors.get("stroke_color", raw_msg_col)
    elif color_theme in COLOR_THEMES:
        theme = COLOR_THEMES[color_theme]
        raw_msg_col = theme["message_color"]
        raw_lbl_col = "#ffffff"
        raw_txt_col = "#1f2328"
        raw_ver_col = "#ffffff"
        raw_strk_col = theme["stroke_color"]
    else:
        # Default: 대학 공식 상징색 (brand)
        raw_msg_col = brand_color
        raw_lbl_col = "#ffffff"
        raw_txt_col = "#1f2328"
        raw_ver_col = "#ffffff"
        raw_strk_col = brand_color

    if outlined:
        label_color = raw_lbl_col
        message_color = raw_lbl_col
        text_color = raw_txt_col
        version_color = raw_msg_col
        stroke_color = raw_strk_col
    else:
        label_color = raw_lbl_col
        message_color = raw_msg_col
        text_color = raw_txt_col
        version_color = raw_ver_col
        stroke_color = raw_strk_col if (prominent or style == "flat-square") else "#d0d7de"

    font_size_label = 11 if (prominent or is_ko_label) else 12
    font_size_msg = 11 if (prominent or is_ko_msg) else 12
    baseline = height / 2 + (4 if prominent else 4)

    font_family_ko = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', 'Malgun Gothic', Arial, sans-serif"
    font_family_en = "Arial, Helvetica, sans-serif"

    label_font = font_family_ko if is_ko_label else font_family_en
    msg_font = font_family_ko if is_ko_msg else font_family_en

    title_text = f"{label_text} {message_text} ({style})"
    aria_label = f"{label_text} {message_text}"

    gloss = (
        f'<defs><linearGradient id="gloss" x2="0" y2="100%">'
        f'<stop offset="0" stop-color="#fff" stop-opacity=".7"/>'
        f'<stop offset=".1" stop-color="#aaa" stop-opacity=".1"/>'
        f'<stop offset=".9" stop-color="#000" stop-opacity=".3"/>'
        f'<stop offset="1" stop-color="#000" stop-opacity=".5"/>'
        f'</linearGradient></defs>\n'
        f'<rect width="{width}" height="{height}" rx="{radius}" fill="url(#gloss)"/>\n'
    ) if glossy else ""

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(aria_label, quote=True)}">
<title>{escape(title_text)}</title>
<defs><clipPath id="badge-shape"><rect width="{width}" height="{height}" rx="{radius}"/></clipPath></defs>
<g clip-path="url(#badge-shape)">
<rect width="{width}" height="{height}" rx="{radius}" fill="{label_color}"/>
<path d="M{label_width} 0h{message_width}v{height}h-{message_width}z" fill="{message_color}"/>
{gloss}</g>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{radius}" fill="none" stroke="{stroke_color}"/>
<g transform="translate({tx:.3f} {ty:.3f}) scale({scale:.6f})">{content}</g>
<text x="{text_x}" y="{baseline:g}" fill="{text_color}" font-family="{label_font}" font-size="{font_size_label}" font-weight="600">{escape(label_text)}</text>
<text x="{label_width + message_width / 2:g}" y="{baseline:g}" fill="{version_color}" text-anchor="middle" font-family="{msg_font}" font-size="{font_size_msg}" font-weight="700">{escape(message_text)}</text>
</svg>
'''


def build_expected_badges(universities, logos):
    expected = {}
    preset_colors = ("blue", "navy", "black", "green", "red", "gray")

    for univ in universities:
        univ_id = univ["id"]
        name = univ["name"]
        short_name = univ["short_name"]
        en_short = univ["en_short"]
        univ_logo = univ.get("logo", "univ")
        brand_color = univ.get("brand_color", "#003876")

        for style in STYLES:
            # 1. 기본 배지 (대학 공식 상징색 brand 테마)
            badge_brand = render_badge(name, en_short, style, univ_logo, logos, "brand", brand_color=brand_color)

            # ID 폴더
            expected[OUTPUT / univ_id / f"{style}.svg"] = badge_brand
            expected[OUTPUT / univ_id / f"{style}-abbr.svg"] = badge_brand
            expected[OUTPUT / univ_id / f"{style}-univ.svg"] = badge_brand

            # 한글 정식 명칭 폴더 (예: 서울대학교)
            expected[OUTPUT / name / f"{style}.svg"] = badge_brand
            expected[OUTPUT / name / f"{style}-abbr.svg"] = badge_brand
            expected[OUTPUT / name / f"{style}-univ.svg"] = badge_brand

            # 한글 약칭 폴더 (예: 서울대)
            expected[OUTPUT / short_name / f"{style}.svg"] = badge_brand
            expected[OUTPUT / short_name / f"{style}-abbr.svg"] = badge_brand
            expected[OUTPUT / short_name / f"{style}-univ.svg"] = badge_brand

            # 2. 색상 프리셋 테마 (<style>-<color>.svg)
            for c_name in preset_colors:
                badge_c = render_badge(name, en_short, style, univ_logo, logos, c_name, brand_color=brand_color)
                expected[OUTPUT / univ_id / f"{style}-{c_name}.svg"] = badge_c
                expected[OUTPUT / name / f"{style}-{c_name}.svg"] = badge_c
                expected[OUTPUT / short_name / f"{style}-{c_name}.svg"] = badge_c

    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify committed badges match generated output")
    parser.add_argument("--univ", help="generate on-demand custom badge for specific university id or name")
    parser.add_argument("--style", default="flat", choices=STYLES, help="badge style")
    parser.add_argument("--color", help="custom message background color (e.g. #8250df or red)")
    parser.add_argument("--label-color", default="#ffffff", help="custom label background color (hex)")
    parser.add_argument("--text-color", default="#1f2328", help="custom label text color (hex)")
    parser.add_argument("--out", help="output file path for custom badge")
    args = parser.parse_args()

    universities = load_universities()
    logos = load_logos()

    # CLI 임의 커스텀 색상 배지 생성 모드
    if args.univ:
        matched = [u for u in universities if u["id"] == args.univ or u["name"] == args.univ or u["short_name"] == args.univ]
        if not matched:
            print(f"Error: university {args.univ!r} not found", file=sys.stderr)
            return 1
        univ = matched[0]
        custom_cols = None
        color_theme = "brand"
        brand_color = univ.get("brand_color", "#003876")

        if args.color:
            if args.color in COLOR_THEMES:
                color_theme = args.color
            else:
                custom_cols = {
                    "message_color": args.color,
                    "label_color": args.label_color,
                    "text_color": args.text_color,
                    "version_color": "#ffffff",
                    "stroke_color": args.color,
                }
        svg = render_badge(
            univ["name"],
            univ["en_short"],
            args.style,
            univ.get("logo", "univ"),
            logos,
            color_theme=color_theme,
            custom_colors=custom_cols,
            brand_color=brand_color,
        )
        if args.out:
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(svg, encoding="utf-8")
            print(f"Generated custom badge for {univ['name']} -> {out_path}")
        else:
            sys.stdout.write(svg)
        return 0

    expected = build_expected_badges(universities, logos)
    existing = set(OUTPUT.glob("**/*.svg"))

    if args.check:
        mismatches = [p for p, content in expected.items() if not p.exists() or p.read_text(encoding="utf-8") != content]
        extras = existing - expected.keys()
        if mismatches or extras:
            for p in sorted([*mismatches, *extras]):
                print(f"out of date: {p.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print(f"Verified {len(expected)} badges")
        return 0

    for path in existing - expected.keys():
        path.unlink()
        curr = path.parent
        while curr != OUTPUT and curr != ROOT:
            try:
                curr.rmdir()
            except OSError:
                break
            curr = curr.parent

    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    print(f"Generated {len(expected)} badges across {len(universities)} universities (including brand & color variants, Korean aliases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
