#!/usr/bin/env python3
"""Fetch and clean authentic university logo SVGs."""

import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGOS_DIR = ROOT / "assets" / "logos"

OFFICIAL_SVG_URLS = {
    "snu": "https://upload.wikimedia.org/wikipedia/en/7/77/Seoul_national_university_emblem.svg",
    "korea": "https://upload.wikimedia.org/wikipedia/en/f/f6/Korea_University_Global_Symbol.svg",
    "yonsei": "https://upload.wikimedia.org/wikipedia/en/9/95/YonseiUniversityEmblem.svg",
    "kaist": "https://upload.wikimedia.org/wikipedia/commons/0/0a/KAIST_logo.svg",
    "postech": "https://upload.wikimedia.org/wikipedia/en/a/a5/POSTECH_emblem.svg",
    "ewha": "https://upload.wikimedia.org/wikipedia/en/5/50/Ewha_Womans_University_logo.svg",
    "pnu": "https://upload.wikimedia.org/wikipedia/en/5/50/Pusan_National_University_logo.svg",
    "jnu": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Logo_of_Chonnam_National_University.svg",
    "cnu": "https://upload.wikimedia.org/wikipedia/en/0/0d/Chungnam_National_University_logo.svg",
    "konkuk": "https://upload.wikimedia.org/wikipedia/en/3/3d/Konkuk_University_logo.svg",
    "hongik": "https://upload.wikimedia.org/wikipedia/commons/8/82/Hongik_emblem.svg",
    "dankook": "https://upload.wikimedia.org/wikipedia/en/8/8a/Dankook_University_emblem.svg",
    "khu": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Kyung_Hee_University_Logo.svg",
    "cau": "https://upload.wikimedia.org/wikipedia/commons/6/68/Logo_of_Chung-Ang_University.svg",
    "uos": "https://upload.wikimedia.org/wikipedia/commons/1/13/University_of_Seoul.svg",
    "kangwon": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Logo_of_kangwon_national_university.svg",
    "kyonggi": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Logo_of_Kyonggi_University.svg",
    "yu": "https://upload.wikimedia.org/wikipedia/commons/4/41/Yeungnam_University_Logo.svg",
    "knue": "https://upload.wikimedia.org/wikipedia/commons/0/0a/KNUE_logotype.svg",
    "knpu": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Korean_National_Police_University_Emblem.svg",
    "inu": "https://upload.wikimedia.org/wikipedia/commons/0/08/Logo_of_INCHEON_NATIONAL_UNIVERSITY.svg",
    "gist": "https://upload.wikimedia.org/wikipedia/commons/3/30/Logo_of_GWANGJU_INSTITUTE_OF_SCIENCE_AND_TECHNOLOGY.svg",
    "kentech": "https://upload.wikimedia.org/wikipedia/commons/2/27/Logo_of_KOREA_INSTITUTE_OF_ENERGY_TECHNOLOGY.svg",
    "kit": "https://upload.wikimedia.org/wikipedia/commons/0/03/Logo_of_kumoh_national_institute_of_technology.svg",
    "wku": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Logo_WonKwang_University.svg",
    "catholic": "https://upload.wikimedia.org/wikipedia/commons/0/04/Catholic_University_of_Korea_logo.svg",
    "unist": "https://upload.wikimedia.org/wikipedia/commons/8/87/%EC%9C%A0%EB%8B%88%EC%8A%A4%ED%8A%B8_%EB%A1%9C%EA%B3%A0.svg",
    "gwnu": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Logo_of_Gangneung-Wonju_National_University.svg",
    "tukorea": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Logo_of_TECH_UNIVERSITY_OF_KOREA.svg",
    "sejong": "https://upload.wikimedia.org/wikipedia/en/e/ee/Sejong_University_logo.svg",
    "swu": "https://upload.wikimedia.org/wikipedia/en/2/20/Seoul_Women%27s_University_logo.svg",
}

headers = {
    "User-Agent": "KoreaUnivBadgeBot/1.0 (https://github.com/leejongyoung/korea-univ-badge; leejongyoung@icloud.com)",
    "Accept": "image/svg+xml,image/*,*/*;q=0.8",
}

for univ_id, url in OFFICIAL_SVG_URLS.items():
    dest = LOGOS_DIR / f"{univ_id}.svg"
    print(f"Fetching official logo for {univ_id}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            # Verify valid SVG XML
            root = ET.fromstring(content)
            # Ensure viewBox exists
            vb = root.get("viewBox")
            if not vb:
                w = root.get("width", "100").replace("px", "").replace("mm", "")
                h = root.get("height", "100").replace("px", "").replace("mm", "")
                try:
                    wf = float(w)
                    hf = float(h)
                    root.set("viewBox", f"0 0 {wf} {hf}")
                    content = ET.tostring(root, encoding="unicode")
                except ValueError:
                    pass
            dest.write_text(content, encoding="utf-8")
            print(f"  -> Saved {dest.name} ({len(content)} bytes)")
    except Exception as e:
        print(f"  -> Failed to fetch {univ_id}: {e}")
    time.sleep(1.0)

print("Done fetching official logos.")
