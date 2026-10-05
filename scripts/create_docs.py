#!/usr/bin/env python3
"""Generate catalog markdown documents in docs/."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
DOCS_DIR.mkdir(parents=True, exist_ok=True)

data = json.loads((ROOT / "universities.json").read_text(encoding="utf-8"))

# 1. docs/national-univ.md (거점국립대 및 국공립대)
national_list = [u for u in data if u["type"] in ("거점국립대", "국공립대", "공립대") and u["type"] != "전문대학"]

nat_doc = [
    "# 대한민국 국공립대학교 배지 카탈로그 (National & Public Universities)",
    "",
    "전국 10대 거점국립대학교 및 주요 국공립·공립 대학교를 위한 배지 목록입니다.",
    "",
    "## 1. 거점국립대학교 (Flagship National Universities)",
    "",
    "| 대학명 | 약칭 | 권역 | 대표 상징색 | Flat 배지 (학교 공식 상징색) | Flat-Square 배지 | For-the-badge | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
]

for u in national_list:
    if u["type"] == "거점국립대":
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        nat_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} ftb](../badges/{uid}/for-the-badge.svg) | "
            f"[{name}]({hp}) |"
        )

nat_doc.extend([
    "",
    "---",
    "",
    "## 2. 주요 국공립대학교 (Public Universities)",
    "",
    "| 대학명 | 약칭 | 권역 | 대표 상징색 | Flat 배지 (학교 공식 상징색) | Flat-Square 배지 | Outline 배지 | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
])

for u in national_list:
    if u["type"] in ("국공립대", "공립대"):
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        nat_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} outline](../badges/{uid}/outline.svg) | "
            f"[{name}]({hp}) |"
        )

(DOCS_DIR / "national-univ.md").write_text("\n".join(nat_doc) + "\n", encoding="utf-8")
print("Generated docs/national-univ.md")


# 2. docs/tech-institutes.md (과기원 및 특수목적대학)
tech_special_list = [u for u in data if u["type"] in ("과학기술특성화대학", "특별법국립") and u["type"] != "전문대학"]

tech_doc = [
    "# 대한민국 과학기술특성화대학 및 특수목적대학 배지 카탈로그",
    "",
    "KAIST, POSTECH 등 연구중심 과학기술특성화대학과 사관학교, 경찰대, 한예종 등 특별법 국립대학 배지 모음입니다.",
    "",
    "## 1. 과학기술특성화대학 (Science & Technology Institutes)",
    "",
    "| 대학명 | 약칭 | 권역 | 상징색 | Flat 배지 | Flat-Square 배지 | For-the-badge | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
]

for u in tech_special_list:
    if u["type"] == "과학기술특성화대학":
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        tech_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} ftb](../badges/{uid}/for-the-badge.svg) | "
            f"[{name}]({hp}) |"
        )

tech_doc.extend([
    "",
    "---",
    "",
    "## 2. 특수목적 국립대학 및 사관학교 (Special Purpose Academies)",
    "",
    "| 대학명 | 약칭 | 권역 | 상징색 | Flat 배지 | Flat-Square 배지 | Outline 배지 | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
])

for u in tech_special_list:
    if u["type"] == "특별법국립":
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        tech_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} outline](../badges/{uid}/outline.svg) | "
            f"[{name}]({hp}) |"
        )

(DOCS_DIR / "tech-institutes.md").write_text("\n".join(tech_doc) + "\n", encoding="utf-8")
print("Generated docs/tech-institutes.md")


# 3. docs/education-univ.md (전국 10개 교육대학교)
edu_list = [u for u in data if u["type"] == "교육대학"]

edu_doc = [
    "# 대한민국 교육대학교 배지 카탈로그 (Universities of Education)",
    "",
    "초등교원 양성을 담당하는 전국 10개 교육대학교의 공식 배지 모음입니다.",
    "",
    "| 대학교명 | 약칭 | 권역 | 대표 상징색 | Flat 배지 (학교 공식 상징색) | Flat-Square 배지 | Outline 배지 | 공식 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
]

for u in edu_list:
    uid = u["id"]
    name = u["name"]
    en_short = u["en_short"]
    reg = u["region"]
    col = u["brand_color"]
    hp = u["homepage"]
    edu_doc.append(
        f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
        f"![{uid} flat](../badges/{uid}/flat.svg) | "
        f"![{uid} square](../badges/{uid}/flat-square.svg) | "
        f"![{uid} outline](../badges/{uid}/outline.svg) | "
        f"[{name}]({hp}) |"
    )

(DOCS_DIR / "education-univ.md").write_text("\n".join(edu_doc) + "\n", encoding="utf-8")
print("Generated docs/education-univ.md")


# 4. docs/private-univ.md (전국 주요 4년제 사립대학교)
priv_list = [u for u in data if u["type"] == "사립대"]

priv_doc = [
    "# 대한민국 사립대학교 배지 카탈로그 (Private Universities)",
    "",
    "서울, 수도권 및 전국 각 권역을 대표하는 주요 4년제 사립대학교 배지 목록입니다.",
    "",
    "## 1. 서울권 주요 사립대학교",
    "",
    "| 대학명 | 약칭 | 상징색 | Flat 배지 (학교 공식 상징색) | Flat-Square 배지 | For-the-badge | 홈페이지 |",
    "| :--- | :---: | :---: | :--- | :--- | :--- | :--- |",
]

for u in priv_list:
    if u["region"] == "서울":
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        col = u["brand_color"]
        hp = u["homepage"]
        priv_doc.append(
            f"| **{name}** | `{en_short}` | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} ftb](../badges/{uid}/for-the-badge.svg) | "
            f"[{name}]({hp}) |"
        )

priv_doc.extend([
    "",
    "---",
    "",
    "## 2. 경기 / 인천(수도권) 주요 사립대학교",
    "",
    "| 대학명 | 약칭 | 권역 | 상징색 | Flat 배지 | Flat-Square 배지 | Outline 배지 | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
])

for u in priv_list:
    if u["region"] in ("경기", "인천"):
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        priv_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} outline](../badges/{uid}/outline.svg) | "
            f"[{name}]({hp}) |"
        )

priv_doc.extend([
    "",
    "---",
    "",
    "## 3. 지방(충청/호남/영남/강원) 주요 사립대학교",
    "",
    "| 대학명 | 약칭 | 권역 | 상징색 | Flat 배지 | Flat-Square 배지 | Outline 배지 | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
])

for u in priv_list:
    if u["region"] not in ("서울", "경기", "인천"):
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        priv_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} outline](../badges/{uid}/outline.svg) | "
            f"[{name}]({hp}) |"
        )

(DOCS_DIR / "private-univ.md").write_text("\n".join(priv_doc) + "\n", encoding="utf-8")
print("Generated docs/private-univ.md")


# 5. docs/vocational-colleges.md (전국 주요 전문대학교)
vocational_list = [u for u in data if u["type"] in ("전문대학", "기능대학") or (u["type"] == "공립대" and "대학" in u["name"] and "대학교" not in u["name"])]

voc_doc = [
    "# 대한민국 전문대학교 배지 카탈로그 (Vocational Colleges & Junior Colleges)",
    "",
    "실무 중심 교육을 선도하는 전국 주요 전문대학교, 기능대학 및 도립대학 배지 목록입니다.",
    "",
    "## 1. 수도권(서울·경기·인천) 주요 전문대학교",
    "",
    "| 대학명 | 약칭 | 권역 | 상징색 | Flat 배지 | Flat-Square 배지 | For-the-badge | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
]

for u in vocational_list:
    if u["region"] in ("서울", "경기", "인천"):
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        voc_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} ftb](../badges/{uid}/for-the-badge.svg) | "
            f"[{name}]({hp}) |"
        )

voc_doc.extend([
    "",
    "---",
    "",
    "## 2. 지방(충청·호남·영남·강원) 주요 전문대학교 및 도립대학",
    "",
    "| 대학명 | 약칭 | 권역 | 상징색 | Flat 배지 | Flat-Square 배지 | Outline 배지 | 홈페이지 |",
    "| :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |",
])

for u in vocational_list:
    if u["region"] not in ("서울", "경기", "인천"):
        uid = u["id"]
        name = u["name"]
        en_short = u["en_short"]
        reg = u["region"]
        col = u["brand_color"]
        hp = u["homepage"]
        voc_doc.append(
            f"| **{name}** | `{en_short}` | {reg} | `{col}` | "
            f"![{uid} flat](../badges/{uid}/flat.svg) | "
            f"![{uid} square](../badges/{uid}/flat-square.svg) | "
            f"![{uid} outline](../badges/{uid}/outline.svg) | "
            f"[{name}]({hp}) |"
        )

(DOCS_DIR / "vocational-colleges.md").write_text("\n".join(voc_doc) + "\n", encoding="utf-8")
print("Generated docs/vocational-colleges.md")
