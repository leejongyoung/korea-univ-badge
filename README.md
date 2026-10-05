# Korea Univ Badge (대한민국 대학교 배지)

[![Verify badges](https://github.com/leejongyoung/korea-univ-badge/actions/workflows/verify.yml/badge.svg)](https://github.com/leejongyoung/korea-univ-badge/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Universities: 165+](https://img.shields.io/badge/Universities-165+-003876.svg)](universities.json)

대한민국 전국 4년제 대학교 및 전문대학교를 위한 자립형(Self-contained) SVG 배지 모음입니다. 대학생 소프트웨어 프로젝트, 교내 동아리 및 학회, 연구실(Lab) 논문/오픈소스 코드, 산학협력 R&D 과제, 해커톤 및 캡스톤 디자인 등의 README에서 소속 대학교를 명확하고 세련되게 표시할 수 있습니다.

별도의 외부 배포 서버나 JavaScript 없이 GitHub raw URL 한 줄로 즉시 임베드할 수 있습니다.

---

## 대학교 상징 및 엠블럼 사용 안내

> [!IMPORTANT]
> **대학교 상징 및 UI 저작권 준수사항**
> - 본 저장소에서 제공하는 배지에 포함된 각 대학교의 공식 엠블럼, 심벌마크, 시그니처 및 명칭에 대한 권리와 상표권은 각 해당 대학교 및 학교법인에 귀속됩니다.
> - 학술 연구, 오픈소스 프로젝트, 교내 동아리 활동, 산학 연구 등 비상업적 학문·개발 협력 및 소속 안내 목적으로 정당하게 사용해야 합니다.
> - 특정 대학의 공식 인증 시스템인 것처럼 기망하거나 사칭하는 행위는 엄격히 금지됩니다.

각 대학교의 아이덴티티를 살리기 위해 **해당 대학의 공식 대표 상징색(School Color / Brand Color)** 이 배지 메시지 배경색으로 자동 적용됩니다.

---

## 한 줄로 사용

원하는 대학교의 영문 식별자 ID(`snu`, `kaist`, `yonsei`, `korea`, `postech`, `skku`, `inha-tc`, `dongyang` 등), 또는 **한글 정식 명칭**(`서울대학교`, `인하공업전문대학` 등), **한글 약칭**(`서울대`, `연세대`, `고려대`, `카이스트`, `인하공전`, `동양미래대` 등)을 URL 경로에 지정하여 즉시 사용할 수 있습니다.

### 1. 영문 식별자 ID 사용
```md
<!-- 서울대학교 (SNU) -->
[![서울대학교](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/snu/flat.svg)](https://www.snu.ac.kr)

<!-- 카이스트 (KAIST) -->
[![KAIST](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/kaist/flat.svg)](https://www.kaist.ac.kr)

<!-- 인하공업전문대학 (ITC) -->
[![인하공전](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/inha-tc/flat.svg)](https://www.itc.ac.kr)

<!-- 고려대학교 (Korea) -->
[![고려대학교](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/korea/flat.svg)](https://www.korea.ac.kr)
```

### 2. 한글 정식 명칭 및 약칭 사용 (100% 동일 지원)
```md
<!-- 한글 정식 명칭 -->
[![포항공과대학교](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/포항공과대학교/flat.svg)](https://www.postech.ac.kr)

<!-- 한글 약칭 -->
[![카이스트](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/카이스트/flat.svg)](https://www.kaist.ac.kr)
[![서울대](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/서울대/flat.svg)](https://www.snu.ac.kr)
[![인하공전](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/인하공전/flat.svg)](https://www.itc.ac.kr)
```

---

## 스타일 및 배지 미리보기

[shields.io](https://shields.io)의 대표적인 스타일 4종(`flat`, `flat-square`, `plastic`, `for-the-badge`)과 테두리 전용 `outline` 스타일까지 총 5개 스타일을 완벽 지원합니다.

| 스타일 | 서울대학교 (`snu`) | KAIST (`kaist`) | 고려대학교 (`korea`) | 연세대학교 (`yonsei`) |
| :--- | :--- | :--- | :--- | :--- |
| **flat** | ![snu flat](badges/snu/flat.svg) | ![kaist flat](badges/kaist/flat.svg) | ![korea flat](badges/korea/flat.svg) | ![yonsei flat](badges/yonsei/flat.svg) |
| **flat-square** | ![snu square](badges/snu/flat-square.svg) | ![kaist square](badges/kaist/flat-square.svg) | ![korea square](badges/korea/flat-square.svg) | ![yonsei square](badges/yonsei/flat-square.svg) |
| **plastic** | ![snu plastic](badges/snu/plastic.svg) | ![kaist plastic](badges/kaist/plastic.svg) | ![korea plastic](badges/korea/plastic.svg) | ![yonsei plastic](badges/yonsei/plastic.svg) |
| **for-the-badge** | ![snu ftb](badges/snu/for-the-badge.svg) | ![kaist ftb](badges/kaist/for-the-badge.svg) | ![korea ftb](badges/korea/for-the-badge.svg) | ![yonsei ftb](badges/yonsei/for-the-badge.svg) |
| **outline** | ![snu outline](badges/snu/outline.svg) | ![kaist outline](badges/kaist/outline.svg) | ![korea outline](badges/korea/outline.svg) | ![yonsei outline](badges/yonsei/outline.svg) |

---

## 컬러 테마 커스터마이징

### 1. 학교 공식 상징색 (기본값)
기본 파일(`flat.svg`, `for-the-badge.svg` 등)은 각 대학교의 공식 상징색(School Color)으로 자동 렌더링됩니다:
- **서울대학교**: Navy (`#0f0f70`)
- **고려대학교**: Crimson (`#862633`)
- **연세대학교**: Yonsei Blue (`#003876`)
- **KAIST**: KAIST Blue (`#004191`)
- **POSTECH**: POSTECH Red (`#c80150`)
- **성균관대학교**: SKKU Green (`#003e2f`)
- **한양대학교**: Hanyang Blue (`#0e4194`)
- **서강대학교**: Cardinal Red (`#a6192e`)
- **이화여자대학교**: Ewha Green (`#00462a`)
- **동국대학교**: Orange (`#ce5b20`)

### 2. 내장 공통 컬러 테마 (URL로 즉시 사용)
README의 톤앤매너에 맞추어 스타일 이름 뒤에 `-<color>`를 붙여 언제든 호출할 수 있습니다 (예: `flat-navy.svg`, `flat-black.svg`):

| 컬러 테마 | 코드 | Hex 색상 | 서울대학교 예시 | 고려대학교 예시 |
| :--- | :---: | :---: | :--- | :--- |
| **블랙 / 다크** | `black` | `#24292f` | ![snu black](badges/snu/flat-black.svg) | ![korea black](badges/korea/flat-black.svg) |
| **네이비** | `navy` | `#003764` | ![snu navy](badges/snu/flat-navy.svg) | ![korea navy](badges/korea/flat-navy.svg) |
| **블루** | `blue` | `#134f8c` | ![snu blue](badges/snu/flat-blue.svg) | ![korea blue](badges/korea/flat-blue.svg) |
| **그린** | `green` | `#1a7f37` | ![snu green](badges/snu/flat-green.svg) | ![korea green](badges/korea/flat-green.svg) |
| **레드** | `red` | `#cf222e` | ![snu red](badges/snu/flat-red.svg) | ![korea red](badges/korea/flat-red.svg) |
| **그레이** | `gray` | `#57606a` | ![snu gray](badges/snu/flat-gray.svg) | ![korea gray](badges/korea/flat-gray.svg) |

```md
<!-- 블랙 테마 사용 예시 -->
[![서울대학교](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/snu/flat-black.svg)](https://www.snu.ac.kr)

<!-- 네이비 테마 사용 예시 -->
[![고려대학교](https://raw.githubusercontent.com/leejongyoung/korea-univ-badge/main/badges/korea/flat-navy.svg)](https://www.korea.ac.kr)
```

### 3. 임의의 Hex 색상으로 직접 생성 (CLI)
내장된 파이썬 스크립트를 통해 원하는 Hex 색상 코드로 맞춤형 SVG를 즉시 생성할 수 있습니다:

```sh
# 보라색(#8250df) 메시지 배경의 KAIST flat 배지 생성
python3 scripts/generate.py --univ kaist --color "#8250df" --style flat --out custom-kaist.svg

# 배경색과 텍스트 색상 모두 커스텀 지정
python3 scripts/generate.py --univ snu --label-color "#ffffff" --text-color "#0f0f70" --color "#0969da" --out custom-snu.svg
```

---

## 분야별 대학교 배지 카탈로그

전국 165개 이상의 4년제 대학교 및 전문대학교가 유형 및 권역별로 체계적으로 분류되어 있습니다.

| 카탈로그 구분 | 수록 대상 | 대학 수 | 바로가기 |
| :--- | :--- | :---: | :---: |
| **거점국립대 및 국공립대** | 서울대, 부산대, 경북대, 전남대, 충남대, 서울시립대, 부경대, 인천대 등 | 34개 | [국공립대 카탈로그 바로가기 →](docs/national-univ.md) |
| **과학기술특성화대학 & 특수목적대** | KAIST, POSTECH, GIST, UNIST, DGIST, KENTECH, 사관학교, 경찰대, 한예종 | 10개 | [과기원·특수대 카탈로그 바로가기 →](docs/tech-institutes.md) |
| **전국 10대 교육대학교** | 서울교대, 경인교대, 부산교대, 대구교대, 광주교대, 춘천교대, 청주교대 등 | 10개 | [교육대 카탈로그 바로가기 →](docs/education-univ.md) |
| **전국 주요 사립대학교** | 연세대, 고려대, 서강대, 성균관대, 한양대, 중앙대, 경희대, 한국외대, 이화여대 등 | 73개 | [사립대 카탈로그 바로가기 →](docs/private-univ.md) |
| **전국 주요 전문대학교** | 인하공전, 명지전문대, 동양미래대, 서울예대, 계원예대, 동아방송예대, 부천대, 유한대 등 | 38개 | [전문대 카탈로그 바로가기 →](docs/vocational-colleges.md) |

---

## 주요 대학교 배지 예시

| 대학교명 | 식별자 ID | 한글 약칭 | 공식 상징색 | 기본 Flat 배지 (학교 상징색) | Outline 배지 |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **서울대학교** | `snu` | 서울대 | `#0f0f70` | ![snu](badges/snu/flat.svg) | ![snu outline](badges/snu/outline.svg) |
| **한국과학기술원** | `kaist` | 카이스트 | `#004191` | ![kaist](badges/kaist/flat.svg) | ![kaist outline](badges/kaist/outline.svg) |
| **포항공과대학교** | `postech` | 포스텍 | `#c80150` | ![postech](badges/postech/flat.svg) | ![postech outline](badges/postech/outline.svg) |
| **연세대학교** | `yonsei` | 연세대 | `#003876` | ![yonsei](badges/yonsei/flat.svg) | ![yonsei outline](badges/yonsei/outline.svg) |
| **고려대학교** | `korea` | 고려대 | `#862633` | ![korea](badges/korea/flat.svg) | ![korea outline](badges/korea/outline.svg) |
| **서강대학교** | `sogang` | 서강대 | `#a6192e` | ![sogang](badges/sogang/flat.svg) | ![sogang outline](badges/sogang/outline.svg) |
| **성균관대학교** | `skku` | 성균관대 | `#003e2f` | ![skku](badges/skku/flat.svg) | ![skku outline](badges/skku/outline.svg) |
| **한양대학교** | `hanyang` | 한양대 | `#0e4194` | ![hanyang](badges/hanyang/flat.svg) | ![hanyang outline](badges/hanyang/outline.svg) |
| **중앙대학교** | `cau` | 중앙대 | `#004c97` | ![cau](badges/cau/flat.svg) | ![cau outline](badges/cau/outline.svg) |
| **경희대학교** | `khu` | 경희대 | `#9b1c2e` | ![khu](badges/khu/flat.svg) | ![khu outline](badges/khu/outline.svg) |
| **한국외국어대학교** | `hufs` | 한국외대 | `#002c6c` | ![hufs](badges/hufs/flat.svg) | ![hufs outline](badges/hufs/outline.svg) |
| **서울시립대학교** | `uos` | 서울시립대 | `#1e3a8a` | ![uos](badges/uos/flat.svg) | ![uos outline](badges/uos/outline.svg) |
| **이화여자대학교** | `ewha` | 이화여대 | `#00462a` | ![ewha](badges/ewha/flat.svg) | ![ewha outline](badges/ewha/outline.svg) |
| **부산대학교** | `pnu` | 부산대 | `#003b80` | ![pnu](badges/pnu/flat.svg) | ![pnu outline](badges/pnu/outline.svg) |
| **경북대학교** | `knu` | 경북대 | `#b71a2b` | ![knu](badges/knu/flat.svg) | ![knu outline](badges/knu/outline.svg) |
| **인하공업전문대학** | `inha-tc` | 인하공전 | `#004b87` | ![inha-tc](badges/inha-tc/flat.svg) | ![inha-tc outline](badges/inha-tc/outline.svg) |
| **동양미래대학교** | `dongyang` | 동양미래대 | `#003876` | ![dongyang](badges/dongyang/flat.svg) | ![dongyang outline](badges/dongyang/outline.svg) |
| **서울예술대학교** | `seoularts` | 서울예대 | `#c80150` | ![seoularts](badges/seoularts/flat.svg) | ![seoularts outline](badges/seoularts/outline.svg) |

---

## 설계 원칙 (Design Principles)

1. **Self-contained SVG**:
   - 모든 배지는 각 대학교의 공식 엠블럼 또는 대학 심벌 벡터 패스를 파일 내부에 직접 포함합니다.
   - 외부 폰트 파일이나 외부 이미지 링크에 의존하지 않고 GitHub, GitLab, 블로그 등 어디서나 완벽하게 렌더링됩니다.
2. **삼중 경로(Triple Alias) 지원**:
   - URL 작성의 편의를 위해 영문 소문자 Slug(`snu`, `kaist`, `inha-tc`), 한국어 정식 명칭(`서울대학교`, `인하공업전문대학`), 한국어 일상 약칭(`서울대`, `인하공전`) 폴더 경로를 100% 동일하게 지원합니다.
3. **가독성 최적화 타이포그래피 & 동적 아이콘 마운팅**:
   - 엠블럼과 심벌마크의 고유 비율을 수학적으로 자동 계산하여 6px의 일관된 여백으로 텍스트와 정렬합니다.
   - 시스템 폰트 스택(`-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Noto Sans KR`, `Malgun Gothic` 등)을 선언하여 모든 OS에서 선명한 한글을 지원합니다.
4. **대학교 공식 상징색(School Color) 기본 렌더링**:
   - 단순한 단일 색상 배지가 아닌, 각 대학교가 공식 지정한 대표 브랜드 컬러를 기본 테마로 적용하여 해당 대학의 고유 정체성을 살립니다.
5. **CI 무결성 보증**:
   - GitHub Actions 워크플로를 통해 `generate.py --check`가 자동으로 수행되어 생성된 배지와 데이터 간의 일치를 항시 보장합니다.

---

## 배지 생성 및 테스트

새로운 대학교 추가나 배지 스타일 수정 시 아래 명령어를 통해 배지를 재빌드하고 무결성을 검증할 수 있습니다.

```sh
# 1. 165개+ 대학교 배지 일괄 생성 (컬러 테마 프리셋 포함 22,000개+)
python3 scripts/generate.py

# 2. 단위 테스트 실행 (데이터 무결성, SVG 유효성, 커스텀 색상 검증)
python3 -m unittest discover -s tests -v

# 3. 배지 생성 결과 일치성 검증 (CI 검증용)
python3 scripts/generate.py --check
```

---

## 라이선스

본 저장소의 빌드 스크립트, 테스트 코드 및 CI 설정은 [MIT License](LICENSE)에 따라 자유롭게 사용 및 수정하실 수 있습니다. 각 배지에 포함된 대학교의 상징, 로고, 명칭에 관한 권리는 해당 대학교 및 학교법인에 귀속되며, 문서 상단의 사용 수칙을 준수해 주시기 바랍니다.
