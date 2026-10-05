#!/usr/bin/env python3
"""Tests for Korea University Badge generator and data integrity."""

import importlib.util
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generate", ROOT / "scripts" / "generate.py")
generate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate)


class KoreaUnivBadgeTests(unittest.TestCase):
    def test_university_data_integrity(self):
        universities = generate.load_universities()
        self.assertGreaterEqual(len(universities), 160)

        # 1. Verify 10 flagship national universities (거점국립대)
        flagships = [u for u in universities if u.get("type") == "거점국립대"]
        self.assertEqual(len(flagships), 10)
        flagship_ids = {u["id"] for u in flagships}
        expected_flagships = {
            "snu", "pnu", "knu", "jnu", "cnu", "cbnu", "jbnu", "kangwon", "jeju", "gnu"
        }
        self.assertEqual(flagship_ids, expected_flagships)

        # 2. Verify 6 institutes of science and technology (과학기술특성화대학)
        tech_institutes = [u for u in universities if u.get("type") == "과학기술특성화대학"]
        self.assertEqual(len(tech_institutes), 6)
        tech_ids = {u["id"] for u in tech_institutes}
        self.assertEqual(tech_ids, {"kaist", "postech", "gist", "unist", "dgist", "kentech"})

        # 3. Verify 10 universities of education (교육대학)
        edu_univs = [u for u in universities if u.get("type") == "교육대학"]
        self.assertEqual(len(edu_univs), 10)
        edu_ids = {u["id"] for u in edu_univs}
        self.assertEqual(edu_ids, {
            "snue", "ginue", "bnue", "dnue", "gnue",
            "cnue-chuncheon", "cnue-cheongju", "gnue-gongju", "jnue", "cue"
        })

        # 4. Verify vocational colleges exist (전문대학)
        vocational_colleges = [u for u in universities if u.get("type") == "전문대학"]
        self.assertGreaterEqual(len(vocational_colleges), 30)
        voc_ids = {u["id"] for u in vocational_colleges}
        for expected in ("inha-tc", "mjc", "dongyang", "seoularts", "bc", "yuhan", "daelim"):
            self.assertIn(expected, voc_ids)

        # 5. Check key major private and public universities
        univ_ids = {u["id"] for u in universities}
        for expected in (
            "yonsei", "korea", "sogang", "skku", "hanyang", "cau", "khu", "hufs", "uos", "ewha",
            "konkuk", "dongguk", "hongik", "kookmin", "soongsil", "sejong", "dankook",
            "ajou", "inha", "pknu", "inu", "yu", "donga", "chosun"
        ):
            self.assertIn(expected, univ_ids)

        # 6. Check all logo references and brand colors
        logos = generate.load_logos()
        for u in universities:
            logo_key = u.get("logo")
            self.assertIn(logo_key, logos, f"University {u['id']} specifies missing logo {logo_key}")
            brand_color = u.get("brand_color")
            self.assertTrue(
                brand_color.startswith("#") and len(brand_color) in (4, 7),
                f"Invalid brand_color {brand_color} for {u['id']}"
            )

    def test_badges_are_valid_accessible_svg(self):
        logos = generate.load_logos()
        sample_univs = [
            u for u in generate.load_universities()
            if u["id"] in ("snu", "yonsei", "korea", "kaist", "postech", "skku", "hanyang", "uos", "ewha", "pnu", "inha-tc")
        ]

        for univ in sample_univs:
            for style in generate.STYLES:
                # 1. Brand theme (university official school color)
                svg = generate.render_badge(
                    univ["name"], univ["en_short"], style, univ["logo"], logos,
                    color_theme="brand", brand_color=univ["brand_color"]
                )
                root = ET.fromstring(svg)
                self.assertEqual(root.attrib["role"], "img")
                self.assertIn(univ["en_short"], root.attrib["aria-label"])
                self.assertNotIn("<script", svg.lower())

                # 2. Preset color themes
                for c_name in ("blue", "navy", "black", "green", "red", "gray"):
                    svg_c = generate.render_badge(
                        univ["name"], univ["en_short"], style, univ["logo"], logos,
                        color_theme=c_name, brand_color=univ["brand_color"]
                    )
                    root_c = ET.fromstring(svg_c)
                    self.assertEqual(root_c.attrib["role"], "img")
                    self.assertNotIn("<script", svg_c.lower())

    def test_custom_color_generation(self):
        logos = generate.load_logos()
        custom = {
            "message_color": "#7952b3",
            "label_color": "#f8f9fa",
            "text_color": "#1f2328",
            "version_color": "#ffffff",
            "stroke_color": "#7952b3",
        }
        svg = generate.render_badge("서울대학교", "SNU", "flat", "snu", logos, custom_colors=custom)
        self.assertIn('fill="#7952b3"', svg)
        self.assertIn('fill="#f8f9fa"', svg)
        root = ET.fromstring(svg)
        self.assertEqual(root.attrib["role"], "img")

    def test_rejects_invalid_styles(self):
        logos = generate.load_logos()
        with self.assertRaises(ValueError):
            generate.render_badge("서울대학교", "SNU", "invalid_style", "snu", logos)

    def test_expected_badges_generation_coverage(self):
        universities = generate.load_universities()
        logos = generate.load_logos()
        expected = generate.build_expected_badges(universities, logos)

        # N universities * 5 styles * (3 base + 6 color presets) * 3 alias folders
        self.assertEqual(len(expected), len(universities) * 5 * 9 * 3)

        # Check key alias paths exist in expected keys
        sample_paths = [
            generate.OUTPUT / "snu" / "flat.svg",
            generate.OUTPUT / "서울대학교" / "flat.svg",
            generate.OUTPUT / "서울대" / "flat.svg",
            generate.OUTPUT / "inha-tc" / "flat.svg",
            generate.OUTPUT / "인하공업전문대학" / "flat.svg",
            generate.OUTPUT / "인하공전" / "flat.svg",
            generate.OUTPUT / "kaist" / "for-the-badge.svg",
            generate.OUTPUT / "카이스트" / "outline.svg",
        ]
        for p in sample_paths:
            self.assertIn(p, expected, f"Path {p} not found in expected badges")

    def test_cli_on_demand_generation(self):
        logos = generate.load_logos()
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "test_badge.svg"
            svg = generate.render_badge(
                "인하공업전문대학", "ITC", "flat", "inha", logos,
                color_theme="black", brand_color="#004b87"
            )
            out_file.write_text(svg, encoding="utf-8")
            self.assertTrue(out_file.exists())
            self.assertIn("ITC", out_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
