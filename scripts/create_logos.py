#!/usr/bin/env python3
"""Generate crisp, high quality university emblem SVG files."""

from pathlib import Path

LOGOS_DIR = Path(__file__).resolve().parents[1] / "assets" / "logos"
LOGOS_DIR.mkdir(parents=True, exist_ok=True)

# 1. univ.svg (Standard University Emblem: Laurels, Mortarboard & Open Book)
univ_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <g fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <!-- Mortarboard -->
    <path d="M50 15 L88 32 L50 49 L12 32 Z" fill="#ffffff" fill-opacity="0.95"/>
    <path d="M26 40 v18 c0 7 10 13 24 13 s24 -6 24 -13 v-18" fill="none" stroke="#ffffff" stroke-width="3"/>
    <!-- Tassel -->
    <path d="M80 34 v22 c0 2 2 4 4 4 s4 -2 4 -4 v-2" stroke="#ffffff" stroke-width="2"/>
    <circle cx="84" cy="58" r="2.5" fill="#ffffff"/>
    <!-- Open Book -->
    <path d="M30 76 c7 -5 14 -3 20 0 c6 -3 13 -5 20 0 v14 c-7 -5 -14 -3 -20 0 c-6 -3 -13 -5 -20 0 Z" fill="#ffffff" fill-opacity="0.9"/>
    <!-- Laurels Left -->
    <path d="M12 60 C8 72 15 84 25 90 M10 66 C14 67 18 64 16 59 M14 76 C19 77 22 73 19 68" stroke="#ffffff" stroke-width="2.5"/>
    <!-- Laurels Right -->
    <path d="M88 60 C92 72 85 84 75 90 M90 66 C86 67 82 64 84 59 M86 76 C81 77 78 73 81 68" stroke="#ffffff" stroke-width="2.5"/>
  </g>
</svg>'''

# 2. snu.svg (Seoul National University: Iconic 'Sha' Gate + Laurels + Pen/Book)
snu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <!-- SNU Blue Circle Background -->
  <circle cx="50" cy="50" r="46" fill="#0f0f70"/>
  <circle cx="50" cy="50" r="42" fill="none" stroke="#ffffff" stroke-width="2"/>
  <!-- SNU Iconic Gate 'Sha' (ㄱ + ㅅ + ㄷ) Geometry -->
  <path d="M50 18 L68 54 H60 L50 32 L40 54 H32 Z" fill="#ffffff"/>
  <!-- Center Crossbar and Vertical of Gate -->
  <path d="M32 54 L32 72 H40 L40 60 H60 L60 72 H68 L68 54 Z" fill="#ffffff"/>
  <!-- Open Book under Gate -->
  <path d="M36 68 Q50 63 50 68 Q50 63 64 68 L64 78 Q50 73 50 78 Q50 73 36 78 Z" fill="#ffffff"/>
  <!-- Pen Nib at Center Top -->
  <path d="M47 38 L50 30 L53 38 L51 44 L49 44 Z" fill="#ffffff"/>
  <!-- Laurels surrounding -->
  <path d="M20 50 C18 66 28 80 42 85 M80 50 C82 66 72 80 58 85" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
</svg>'''

# 3. yonsei.svg (Yonsei University: Shield, 'ㅇ ㅅ', Book & Torch)
yonsei_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <!-- Yonsei Blue Shield -->
  <path d="M50 10 C75 10 85 18 85 45 C85 72 50 90 50 90 C50 90 15 72 15 45 C15 18 25 10 50 10 Z" fill="#003876" stroke="#ffffff" stroke-width="3"/>
  <!-- Inner Shield Border -->
  <path d="M50 16 C71 16 79 23 79 45 C79 67 50 82 50 82 C50 82 21 67 21 45 C21 23 29 16 50 16 Z" fill="none" stroke="#ffffff" stroke-width="1.5"/>
  <!-- 'ㅇ' Circle -->
  <circle cx="50" cy="34" r="10" fill="none" stroke="#ffffff" stroke-width="3"/>
  <!-- 'ㅅ' Chevron -->
  <path d="M50 48 L35 70 M50 48 L65 70" fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round"/>
  <!-- Open Book in Center -->
  <path d="M40 56 Q50 53 50 56 Q50 53 60 56 L60 64 Q50 61 50 64 Q50 61 40 64 Z" fill="#ffffff"/>
  <!-- Torch Flame Top -->
  <path d="M50 20 Q54 26 50 30 Q46 26 50 20 Z" fill="#ffffff"/>
</svg>'''

# 4. korea.svg (Korea University: Crimson Shield with Fierce Tiger)
korea_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <!-- Crimson Shield -->
  <path d="M50 8 C76 8 86 16 86 44 C86 72 50 92 50 92 C50 92 14 72 14 44 C14 16 24 8 50 8 Z" fill="#862633" stroke="#ffffff" stroke-width="3"/>
  <path d="M50 14 C72 14 80 21 80 44 C80 67 50 84 50 84 C50 84 20 67 20 44 C20 21 28 14 50 14 Z" fill="none" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Tiger Silhouette Profile / Head Facing Forward -->
  <path d="M34 32 L40 24 L48 30 L52 30 L60 24 L66 32 L62 44 L68 52 L62 62 L50 72 L38 62 L32 52 L38 44 Z" fill="#ffffff"/>
  <!-- Tiger Features (Crimson Inset) -->
  <circle cx="43" cy="42" r="2.5" fill="#862633"/>
  <circle cx="57" cy="42" r="2.5" fill="#862633"/>
  <path d="M47 50 L53 50 L50 55 Z" fill="#862633"/>
  <path d="M42 58 Q50 64 58 58" fill="none" stroke="#862633" stroke-width="2" stroke-linecap="round"/>
  <!-- Tiger Forehead Stripes (King 王 style) -->
  <path d="M44 32 H56 M46 36 H54 M50 30 V38" stroke="#862633" stroke-width="1.5" stroke-linecap="round"/>
</svg>'''

# 5. kaist.svg (KAIST: Geometric Tech Wordmark / Modern Emblem)
kaist_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#004191"/>
  <!-- Geometric Angled 'K' & Tech Beam -->
  <path d="M24 26 H34 V74 H24 Z" fill="#ffffff"/>
  <path d="M34 50 L56 26 H68 L44 50 L70 74 H57 L34 51 Z" fill="#ffffff"/>
  <!-- Tech Orbit / Node Rings -->
  <ellipse cx="64" cy="50" rx="16" ry="6" transform="rotate(-30 64 50)" fill="none" stroke="#ffffff" stroke-width="2"/>
  <circle cx="76" cy="43" r="3.5" fill="#ffffff"/>
</svg>'''

# 6. postech.svg (POSTECH: Red Emblem with Flame & Atomic Orbit)
postech_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#c80150"/>
  <!-- Atomic Orbit 1 -->
  <ellipse cx="50" cy="50" rx="36" ry="14" transform="rotate(30 50 50)" fill="none" stroke="#ffffff" stroke-width="2.5"/>
  <!-- Atomic Orbit 2 -->
  <ellipse cx="50" cy="50" rx="36" ry="14" transform="rotate(-30 50 50)" fill="none" stroke="#ffffff" stroke-width="2.5"/>
  <!-- Central Torch Flame / P Symbol -->
  <path d="M48 24 C56 32 60 42 54 52 C52 55 48 58 48 68 H42 C42 54 44 48 40 42 C38 38 40 30 48 24 Z" fill="#ffffff"/>
  <circle cx="50" cy="50" r="5" fill="#ffffff"/>
</svg>'''

# 7. skku.svg (Sungkyunkwan University: Iconic Ginkgo Leaf)
skku_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#003e2f"/>
  <!-- Ginkgo Leaf Silhouette -->
  <path d="M50 78 C48 68 47 56 46 48 C30 48 18 36 22 22 C34 18 46 26 50 36 C54 26 66 18 78 22 C82 36 70 48 54 48 C53 56 52 68 50 78 Z" fill="#ffffff"/>
  <!-- Inner leaf vein lines -->
  <path d="M50 38 Q38 30 30 26 M50 38 Q42 24 36 21 M50 38 Q58 24 64 21 M50 38 Q62 30 70 26" fill="none" stroke="#003e2f" stroke-width="1.5" stroke-linecap="round"/>
</svg>'''

# 8. hanyang.svg (Hanyang University: Courageous Lion)
hanyang_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#0e4194"/>
  <!-- Majestic Lion Head Silhouette -->
  <path d="M50 20 C64 20 74 28 78 40 C82 52 76 66 66 74 C58 80 42 80 34 74 C24 66 18 52 22 40 C26 28 36 20 50 20 Z" fill="#ffffff"/>
  <!-- Lion Mane & Face Details in Blue -->
  <path d="M38 34 C44 32 48 38 48 42 M62 34 C56 32 52 38 52 42" fill="none" stroke="#0e4194" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Nose & Mouth -->
  <path d="M47 52 L53 52 L50 57 Z" fill="#0e4194"/>
  <path d="M50 57 V62 M44 64 Q50 68 56 64" fill="none" stroke="#0e4194" stroke-width="2" stroke-linecap="round"/>
  <!-- Mane spikes -->
  <path d="M22 40 L16 46 L24 50 L18 58 L28 60 M78 40 L84 46 L76 50 L82 58 L72 60" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"/>
</svg>'''

# 9. sogang.svg (Sogang University: Albatross Flight & Cardinal Shield)
sogang_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <path d="M50 10 C75 10 85 18 85 45 C85 72 50 90 50 90 C50 90 15 72 15 45 C15 18 25 10 50 10 Z" fill="#a6192e" stroke="#ffffff" stroke-width="3"/>
  <!-- Albatross Soaring Wings -->
  <path d="M18 42 C32 36 44 42 50 48 C56 42 68 36 82 42 C70 54 58 56 50 68 C42 56 30 54 18 42 Z" fill="#ffffff"/>
  <!-- Cross in Center -->
  <path d="M50 22 V36 M44 28 H56" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
</svg>'''

# 10. cau.svg (Chung-Ang University: Blue Dragon & Shield)
cau_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#004c97"/>
  <!-- Ascending Blue Dragon Silhouette -->
  <path d="M50 18 C58 24 64 34 60 44 C56 52 46 54 44 62 C42 70 50 76 56 74 C62 72 66 66 68 60 L74 62 C70 72 62 80 52 80 C40 80 34 70 36 58 C38 48 48 44 52 38 C56 32 52 24 46 22 Z" fill="#ffffff"/>
  <!-- Dragon Pearl / Orb of Wisdom -->
  <circle cx="38" cy="24" r="5" fill="#ffffff"/>
  <circle cx="50" cy="50" r="42" fill="none" stroke="#ffffff" stroke-width="2"/>
</svg>'''

# 11. khu.svg (Kyung Hee University: Magnolia & Peace Palace)
khu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#9b1c2e"/>
  <!-- Magnolia Petals (경희 목련) -->
  <path d="M50 22 C56 34 56 46 50 58 C44 46 44 34 50 22 Z" fill="#ffffff"/>
  <path d="M50 58 C38 52 26 52 22 40 C34 44 44 50 50 58 Z" fill="#ffffff"/>
  <path d="M50 58 C62 52 74 52 78 40 C66 44 56 50 50 58 Z" fill="#ffffff"/>
  <!-- Globe / Torch Base -->
  <circle cx="50" cy="66" r="10" fill="#ffffff"/>
  <circle cx="50" cy="66" r="6" fill="#9b1c2e"/>
  <path d="M46 76 H54 L52 84 H48 Z" fill="#ffffff"/>
</svg>'''

# 12. hufs.svg (HUFS: Owl of Minerva & World Globe)
hufs_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#002c6c"/>
  <!-- Owl Silhouette -->
  <path d="M38 28 L44 34 C48 33 52 33 56 34 L62 28 C64 36 66 44 66 56 C66 68 58 76 50 76 C42 76 34 68 34 56 C34 44 36 36 38 28 Z" fill="#ffffff"/>
  <!-- Big Eyes -->
  <circle cx="44" cy="46" r="5" fill="#002c6c"/>
  <circle cx="56" cy="46" r="5" fill="#002c6c"/>
  <circle cx="44" cy="46" r="2" fill="#ffffff"/>
  <circle cx="56" cy="46" r="2" fill="#ffffff"/>
  <!-- Beak -->
  <path d="M48 52 L52 52 L50 56 Z" fill="#002c6c"/>
  <!-- Feather / Globe Arc -->
  <path d="M26 50 C26 68 36 82 50 82 C64 82 74 68 74 50" fill="none" stroke="#ffffff" stroke-width="2"/>
</svg>'''

# 13. uos.svg (University of Seoul: Iconic 'S' Wings)
uos_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#1e3a8a"/>
  <!-- Futuristic Seoul 'S' Wing Mark -->
  <path d="M24 38 C32 26 48 24 64 28 C74 31 78 38 74 46 C70 54 58 56 46 60 C36 63 32 68 34 72 C37 77 48 78 60 74 L62 80 C46 86 30 84 26 74 C22 64 32 58 44 54 C56 50 64 48 66 42 C68 37 62 32 54 30 C42 27 30 30 24 38 Z" fill="#ffffff"/>
</svg>'''

# 14. ewha.svg (Ewha Womans University: Pear Blossom Cross)
ewha_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#00462a"/>
  <!-- Pear Blossom (5 Petals) -->
  <!-- Center Cross -->
  <g fill="#ffffff">
    <!-- Top Petal -->
    <path d="M50 50 C44 38 42 26 50 18 C58 26 56 38 50 50 Z"/>
    <!-- Top Right -->
    <path d="M50 50 C62 44 74 42 80 50 C74 58 62 56 50 50 Z" transform="rotate(-18 50 50)"/>
    <!-- Bottom Right -->
    <path d="M50 50 C58 62 56 74 50 82 C44 74 42 62 50 50 Z" transform="rotate(-36 50 50)"/>
    <!-- Bottom Left -->
    <path d="M50 50 C42 62 44 74 50 82 C56 74 58 62 50 50 Z" transform="rotate(36 50 50)"/>
    <!-- Top Left -->
    <path d="M50 50 C38 44 26 42 20 50 C26 58 38 56 50 50 Z" transform="rotate(18 50 50)"/>
  </g>
  <!-- Core Flower Pistil -->
  <circle cx="50" cy="50" r="7" fill="#00462a"/>
  <circle cx="50" cy="50" r="4" fill="#ffffff"/>
</svg>'''

# 15. pnu.svg (Pusan National University: Soaring Eagle)
pnu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#003b80"/>
  <!-- Eagle Soaring Silhouette -->
  <path d="M50 26 L58 38 C68 34 78 36 86 44 C76 48 68 50 62 58 C66 66 62 74 50 78 C38 74 34 66 38 58 C32 50 24 48 14 44 C22 36 32 34 42 38 Z" fill="#ffffff"/>
  <!-- Tower / Torch Top -->
  <path d="M48 20 H52 V28 H48 Z" fill="#ffffff"/>
</svg>'''

# 16. knu.svg (Kyungpook National University: Cheomseongdae Tower)
knu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#b71a2b"/>
  <!-- Cheomseongdae Outline -->
  <path d="M42 22 H58 V26 H42 Z M44 26 H56 V30 H44 Z M42 30 H58 L62 74 H38 L42 30 Z M34 74 H66 V80 H34 Z" fill="#ffffff"/>
  <!-- Cheomseongdae Window -->
  <rect x="47" y="46" width="6" height="8" rx="1" fill="#b71a2b"/>
</svg>'''

# 17. cnu.svg (Chungnam National University: White Horse)
cnu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#003366"/>
  <!-- Galloping White Horse Head Silhouette -->
  <path d="M34 76 L36 60 C34 52 36 42 42 34 L40 22 L48 28 C54 26 62 30 66 38 C70 46 66 52 60 56 L64 76 L52 70 L44 76 Z" fill="#ffffff"/>
  <!-- Eye -->
  <circle cx="48" cy="38" r="2" fill="#003366"/>
</svg>'''

# 18. jnu.svg (Chonnam National University: Dragon & Phoenix)
jnu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#00693e"/>
  <!-- Yongbong (용봉) Flame Emblem -->
  <path d="M50 18 C58 26 64 36 60 48 C56 56 46 60 48 70 C50 76 56 78 62 76 C56 82 44 82 38 74 C34 66 38 56 44 48 C48 42 46 32 38 26 C44 24 48 20 50 18 Z" fill="#ffffff"/>
  <!-- Central Torch Core -->
  <circle cx="50" cy="38" r="5" fill="#ffffff"/>
</svg>'''

# 19. inha.svg (Inha University: Flying Dragon / Wings)
inha_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#004b87"/>
  <!-- Biryong (Flying Dragon) Wing Shield -->
  <path d="M50 16 C68 28 82 36 84 54 C86 70 70 82 50 86 C30 82 14 70 16 54 C18 36 32 28 50 16 Z" fill="none" stroke="#ffffff" stroke-width="3"/>
  <path d="M26 46 C38 40 48 44 50 54 C52 44 62 40 74 46 C66 60 58 66 50 76 C42 66 34 60 26 46 Z" fill="#ffffff"/>
</svg>'''

# 20. ajou.svg (Ajou University: Pioneer Torch)
ajou_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#003876"/>
  <!-- Pioneer Flame Torch -->
  <path d="M50 18 C56 26 60 34 54 44 C50 50 44 54 46 64 H54 C56 54 50 50 46 44 C42 34 46 26 50 18 Z" fill="#ffffff"/>
  <!-- Torch Handle -->
  <path d="M45 64 H55 L53 82 H47 Z" fill="#ffffff"/>
  <!-- Flame Rays -->
  <circle cx="50" cy="36" r="4" fill="#003876"/>
</svg>'''

# 21. konkuk.svg (Konkuk University: Ox / Bull)
konkuk_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#005a36"/>
  <!-- Ox Head & Horns -->
  <path d="M28 30 C32 22 42 22 46 32 C48 30 52 30 54 32 C58 22 68 22 72 30 C66 38 64 48 64 56 C64 68 58 76 50 78 C42 76 36 68 36 56 C36 48 34 38 28 30 Z" fill="#ffffff"/>
  <!-- Eyes & Nose -->
  <circle cx="44" cy="50" r="2.5" fill="#005a36"/>
  <circle cx="56" cy="50" r="2.5" fill="#005a36"/>
  <ellipse cx="50" cy="66" rx="5" ry="3" fill="#005a36"/>
</svg>'''

# 22. dongguk.svg (Dongguk University: White Elephant & Lotus)
dongguk_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#ce5b20"/>
  <!-- Lotus & White Elephant -->
  <path d="M50 22 C56 32 58 44 50 54 C42 44 44 32 50 22 Z" fill="#ffffff"/>
  <path d="M34 36 C42 42 46 50 48 58 C38 56 30 48 34 36 Z" fill="#ffffff"/>
  <path d="M66 36 C58 42 54 50 52 58 C62 56 70 48 66 36 Z" fill="#ffffff"/>
  <!-- Lotus Petal Base -->
  <path d="M30 62 Q50 74 70 62 Q50 82 30 62 Z" fill="#ffffff"/>
</svg>'''

# 23. hongik.svg (Hongik University: Creative Wings / Flame)
hongik_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#002c6c"/>
  <!-- Hongik 'H' / Flame Geometry -->
  <path d="M32 26 H42 V46 H58 V26 H68 V74 H58 V56 H42 V74 H32 Z" fill="#ffffff"/>
  <!-- Creative Peak -->
  <polygon points="50,18 42,26 58,26" fill="#ffffff"/>
</svg>'''

# 24. sookmyung.svg (Sookmyung Women's University: Plum Blossom / Mae-Hwa)
sookmyung_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#00205b"/>
  <!-- Plum Blossom (Mae-Hwa) 5 rounded petals -->
  <circle cx="50" cy="30" r="12" fill="#ffffff"/>
  <circle cx="69" cy="44" r="12" fill="#ffffff"/>
  <circle cx="62" cy="67" r="12" fill="#ffffff"/>
  <circle cx="38" cy="67" r="12" fill="#ffffff"/>
  <circle cx="31" cy="44" r="12" fill="#ffffff"/>
  <!-- Center Core -->
  <circle cx="50" cy="50" r="10" fill="#00205b"/>
  <circle cx="50" cy="50" r="5" fill="#ffffff"/>
</svg>'''

# 25. kookmin.svg (Kookmin University: Double Dragon / Symmetrical Mark)
kookmin_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#0c2340"/>
  <!-- Kookmin 'K' Dynamic Geometry -->
  <path d="M28 24 H38 V76 H28 Z" fill="#ffffff"/>
  <path d="M38 52 L58 24 H72 L50 50 L74 76 H60 L42 54 Z" fill="#ffffff"/>
</svg>'''

# 26. soongsil.svg (Soongsil University: White Horse / Cross)
soongsil_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#004c97"/>
  <!-- Soongsil Cross & White Horse Crest -->
  <path d="M46 20 H54 V46 H76 V54 H54 V80 H46 V54 H24 V46 H46 Z" fill="#ffffff"/>
  <circle cx="50" cy="50" r="38" fill="none" stroke="#ffffff" stroke-width="2.5"/>
</svg>'''

# 27. sejong.svg (Sejong University: King Sejong Crest / Flame)
sejong_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#9b1b30"/>
  <!-- Royal Flame & Crown Motif -->
  <path d="M50 18 L56 34 L72 34 L58 44 L64 60 L50 50 L36 60 L42 44 L28 34 L44 34 Z" fill="#ffffff"/>
  <circle cx="50" cy="68" r="8" fill="#ffffff"/>
</svg>'''

# 28. dankook.svg (Dankook University: Bear Crest)
dankook_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#003876"/>
  <!-- Dankook Bear Head Silhouette -->
  <path d="M32 30 C30 22 40 20 44 26 C46 24 54 24 56 26 C60 20 70 22 68 30 C74 36 74 54 70 66 C64 76 58 78 50 78 C42 78 36 76 30 66 C26 54 26 36 32 30 Z" fill="#ffffff"/>
  <!-- Bear Snout -->
  <circle cx="43" cy="46" r="3" fill="#003876"/>
  <circle cx="57" cy="46" r="3" fill="#003876"/>
  <ellipse cx="50" cy="60" rx="6" ry="4" fill="#003876"/>
</svg>'''

# 29. cbnu.svg (Chungbuk National University: Galloping Bull / Flame)
cbnu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#00356b"/>
  <path d="M30 40 C34 30 44 30 48 38 C50 36 56 36 58 38 C62 30 72 30 76 40 C72 56 68 70 50 78 C32 70 28 56 30 40 Z" fill="#ffffff"/>
  <circle cx="50" cy="48" r="6" fill="#00356b"/>
</svg>'''

# 30. jbnu.svg (Jeonbuk National University: Phoenix Wings)
jbnu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#002b49"/>
  <!-- Phoenix Wing Upward Sweep -->
  <path d="M50 20 C60 30 72 36 82 46 C70 50 62 52 56 62 C58 70 54 76 50 78 C46 76 42 70 44 62 C38 52 30 50 18 46 C28 36 40 30 50 20 Z" fill="#ffffff"/>
</svg>'''

# 31. kangwon.svg (Kangwon National University: Bear Crest)
kangwon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#004ea2"/>
  <path d="M34 32 C32 24 42 22 46 28 C48 26 52 26 54 28 C58 22 68 24 66 32 C72 40 72 58 66 68 C58 76 54 76 50 76 C46 76 42 76 34 68 C28 58 28 40 34 32 Z" fill="#ffffff"/>
  <circle cx="44" cy="46" r="2.5" fill="#004ea2"/>
  <circle cx="56" cy="46" r="2.5" fill="#004ea2"/>
</svg>'''

# 32. gnu.svg (Gyeongsang National University: Pioneer Torch)
gnu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#003876"/>
  <path d="M50 18 L58 34 H42 Z M46 36 H54 V74 H46 Z" fill="#ffffff"/>
  <circle cx="50" cy="50" r="40" fill="none" stroke="#ffffff" stroke-width="2.5"/>
</svg>'''

# 33. jeju.svg (Jeju National University: Deer / Hallasan)
jeju_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#004098"/>
  <!-- White Deer & Mountain Contour -->
  <path d="M20 72 L50 32 L80 72 Z" fill="#ffffff"/>
  <path d="M42 46 L50 36 L58 46 Z" fill="#004098"/>
</svg>'''

# 34. pknu.svg (Pukyong National University: Whale & Wave)
pknu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#003f7f"/>
  <!-- Blue Whale Spouting Water / Wave -->
  <path d="M22 62 C34 50 48 48 64 50 C74 52 82 46 86 38 C84 56 74 68 58 72 C42 76 28 72 22 62 Z" fill="#ffffff"/>
  <circle cx="70" cy="56" r="2.5" fill="#003f7f"/>
  <path d="M68 44 C72 38 76 34 82 32 M72 44 C76 40 82 38 86 38" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
</svg>'''

# 35. inu.svg (Incheon National University: Torch of Hope)
inu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#004b87"/>
  <path d="M50 20 C58 28 62 38 56 48 C52 54 48 58 48 66 H52 C52 58 56 54 60 48 C66 38 62 28 50 20 Z" fill="#ffffff"/>
  <rect x="46" y="68" width="8" height="14" rx="2" fill="#ffffff"/>
</svg>'''

# 36. gist.svg (Gwangju Institute of Science and Technology)
gist_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#eb5b25"/>
  <!-- Tech 'G' Spiral / Orbit -->
  <path d="M68 34 C62 26 50 24 38 30 C26 36 22 50 26 62 C30 74 44 80 56 76 C66 72 72 62 72 52 H48 V44 H80 C80 60 72 76 56 82 C38 88 20 80 14 62 C8 44 14 26 30 18 C46 10 64 14 74 26 Z" fill="#ffffff"/>
</svg>'''

# 37. unist.svg (Ulsan National Institute of Science and Technology)
unist_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#0b2265"/>
  <!-- Bold Tech 'U' -->
  <path d="M30 26 H42 V56 C42 64 45 68 50 68 C55 68 58 64 58 56 V26 H70 V56 C70 72 62 78 50 78 C38 78 30 72 30 56 Z" fill="#ffffff"/>
  <circle cx="50" cy="40" r="4" fill="#ffffff"/>
</svg>'''

# 38. dgist.svg (Daegu Gyeongbuk Institute of Science and Technology)
dgist_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#0089cf"/>
  <!-- Bold Tech 'D' Shape with Internal Spark -->
  <path d="M30 24 H50 C66 24 76 34 76 50 C76 66 66 76 50 76 H30 Z M42 36 V64 H50 C58 64 64 58 64 50 C64 42 58 36 50 36 Z" fill="#ffffff"/>
</svg>'''

logos = {
    "univ": univ_svg,
    "snu": snu_svg,
    "yonsei": yonsei_svg,
    "korea": korea_svg,
    "kaist": kaist_svg,
    "postech": postech_svg,
    "skku": skku_svg,
    "hanyang": hanyang_svg,
    "sogang": sogang_svg,
    "cau": cau_svg,
    "khu": khu_svg,
    "hufs": hufs_svg,
    "uos": uos_svg,
    "ewha": ewha_svg,
    "pnu": pnu_svg,
    "knu": knu_svg,
    "cnu": cnu_svg,
    "jnu": jnu_svg,
    "inha": inha_svg,
    "ajou": ajou_svg,
    "konkuk": konkuk_svg,
    "dongguk": dongguk_svg,
    "hongik": hongik_svg,
    "sookmyung": sookmyung_svg,
    "kookmin": kookmin_svg,
    "soongsil": soongsil_svg,
    "sejong": sejong_svg,
    "dankook": dankook_svg,
    "cbnu": cbnu_svg,
    "jbnu": jbnu_svg,
    "kangwon": kangwon_svg,
    "gnu": gnu_svg,
    "jeju": jeju_svg,
    "pknu": pknu_svg,
    "inu": inu_svg,
    "gist": gist_svg,
    "unist": unist_svg,
    "dgist": dgist_svg,
}

for name, svg in logos.items():
    p = LOGOS_DIR / f"{name}.svg"
    p.write_text(svg.strip() + "\n", encoding="utf-8")
    print(f"Created logo: {p.name}")

print(f"Total logos generated: {len(logos)}")
