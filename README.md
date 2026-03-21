# fontfyi

[![PyPI version](https://agentgif.com/badge/pypi/fontfyi/version.svg)](https://pypi.org/project/fontfyi/)
[![Python](https://img.shields.io/pypi/pyversions/fontfyi)](https://pypi.org/project/fontfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Pure Python Google Fonts toolkit. Access [50 popular fonts](https://fontfyi.com/fonts/) metadata, generate CSS import URLs, browse [10 web-safe font stacks](https://fontfyi.com/tools/font-stack/), and [15 curated font pairings](https://fontfyi.com/pairings/) -- all with zero dependencies.

> **Explore all fonts at [fontfyi.com](https://fontfyi.com/)** -- [font explorer](https://fontfyi.com/fonts/), [font pairings](https://fontfyi.com/pairings/), [font stacks](https://fontfyi.com/tools/font-stack/), and [developer API](https://fontfyi.com/developers/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/fontfyi/main/demo.gif" alt="fontfyi CLI demo" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Font Metadata](#font-metadata)
  - [Font Pairing](#font-pairing)
- [Font Pairings & Stacks](#font-pairings--stacks)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
  - [Font Data](#font-data)
  - [CSS Utilities](#css-utilities)
  - [Font Stacks](#font-stacks)
  - [Font Pairings](#font-pairings)
- [Data Types](#data-types)
- [Features](#features)
- [Learn More About Fonts](#learn-more-about-fonts)
- [Creative FYI Family](#creative-fyi-family)
- [License](#license)

## Install

```bash
pip install fontfyi                # Core engine (zero deps)
pip install "fontfyi[cli]"         # + Command-line interface
pip install "fontfyi[mcp]"         # + MCP server for AI assistants
pip install "fontfyi[api]"         # + HTTP client for fontfyi.com API
pip install "fontfyi[all]"         # Everything
```

## Quick Start

```python
from fontfyi import get_font, css_family, google_fonts_url, parse_variants

# Look up a font
font = get_font("inter")
print(font["family"])       # Inter
print(font["category"])     # sans-serif
print(font["designer"])     # Rasmus Andersson

# Parse weight variants
weights, italic = parse_variants(font["variants"])
print(weights)              # [100, 200, 300, 400, 500, 600, 700, 800, 900]
print(italic)               # True

# Generate CSS
print(css_family("Inter", "sans-serif"))
# 'Inter', sans-serif
print(google_fonts_url("Inter", [400, 700]))
# https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap
```

## What You Can Do

### Font Metadata

Google Fonts serves over 1,500 font families, but most web projects rely on a curated subset of proven, high-performance typefaces. The package includes metadata for 50 of the most popular Google Fonts -- covering family name, category (serif, sans-serif, display, monospace, handwriting), available weight variants, italic support, character subsets, designer attribution, and popularity ranking. You can generate ready-to-use CSS `font-family` declarations, Google Fonts import URLs, HTML `<link>` tags, and even Homebrew install commands.

| Font | Category | Weights | Designer |
|------|----------|---------|----------|
| Inter | sans-serif | 100--900 + italic | Rasmus Andersson |
| Roboto | sans-serif | 100--900 + italic | Christian Robertson |
| Open Sans | sans-serif | 300--800 + italic | Steve Matteson |
| Lora | serif | 400--700 + italic | Cyreal |
| Fira Code | monospace | 300--700 | Nikita Prokopov |
| Playfair Display | serif | 400--900 + italic | Claus Eggers Sorensen |
| JetBrains Mono | monospace | 100--800 + italic | JetBrains |
| Montserrat | sans-serif | 100--900 + italic | Julieta Ulanovsky |

```python
from fontfyi import get_font, css_family, google_fonts_url, parse_variants

# Access font metadata for any of the 50 included Google Fonts
font = get_font("fira-code")
print(font["family"])       # Fira Code
print(font["category"])     # monospace
print(font["designer"])     # Nikita Prokopov

# Parse available weight variants and italic support
weights, italic = parse_variants(font["variants"])
print(weights)              # [300, 400, 500, 600, 700]
print(italic)               # False

# Generate CSS font-family declaration with fallback
print(css_family("Fira Code", "monospace"))
# 'Fira Code', monospace

# Generate Google Fonts import URL with specific weights
print(google_fonts_url("Fira Code", [400, 700]))
# https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap
```

Learn more: [Google Fonts Explorer](https://fontfyi.com/) · [Font Search by Category](https://fontfyi.com/category/)

### Font Pairing

Choosing complementary heading and body typefaces is one of the most impactful design decisions for readability and visual hierarchy. Good font pairings balance contrast (serif + sans-serif, geometric + humanist) with harmony (matching x-heights, similar proportions). The package includes 15 curated font pairings with compatibility scores, rationale explaining why the combination works, mood descriptors, and suggested use cases -- saving hours of trial and error.

```python
from fontfyi import get_pairings_for, featured_pairings

# Get font pairing recommendations for a specific typeface
pairings = get_pairings_for("inter")
for p in pairings:
    print(f"Heading: {p.heading} + Body: {p.body}")
    print(f"  Score: {p.score}/10")
    print(f"  Rationale: {p.rationale}")
    print(f"  Mood: {p.mood}")
    print(f"  Use cases: {p.use_cases}")

# Browse only high-scoring featured pairings (score >= 8)
top_pairings = featured_pairings()
print(f"{len(top_pairings)} featured pairings with score >= 8")
for p in top_pairings:
    print(f"  {p.heading} + {p.body} ({p.score}/10) -- {p.mood}")
```

Learn more: [Font Pairing Recommendations](https://fontfyi.com/pairings/) · [Font Stack Presets](https://fontfyi.com/tools/font-stack/)

## Font Pairings & Stacks

```python
from fontfyi import (
    search, popular, by_category, get_stack,
    get_pairings_for, featured_pairings, FONT_STACKS,
)

# Search fonts
results = search("mono")
for f in results:
    print(f"{f['family']} ({f['category']})")

# Top 10 most popular fonts
for f in popular(10):
    print(f"{f['popularity_rank']}. {f['family']}")

# Font stacks (CSS-ready)
stack = get_stack("system-ui")
print(stack.stack)
# system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, ...

# Font pairings with rationale
for p in get_pairings_for("inter"):
    print(f"{p.heading} + {p.body} (score: {p.score})")
    print(f"  {p.rationale}")
    print(f"  Mood: {p.mood}")
```

## Command-Line Interface

```bash
pip install "fontfyi[cli]"

fontfyi info inter                     # Font metadata table
fontfyi search mono                    # Search fonts by name
fontfyi css inter                      # CSS import snippet
fontfyi pair inter                     # Font pairing suggestions
fontfyi popular                        # Top fonts by popularity
fontfyi stacks                         # Font stack presets
```

## MCP Server (Claude, Cursor, Windsurf)

Add font tools to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "fontfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "fontfyi": {
            "command": "python",
            "args": ["-m", "fontfyi.mcp_server"]
        }
    }
}
```

**Available tools**: `font_info`, `font_search`, `font_css`, `font_pairings`, `font_stacks`, `popular_fonts`

## REST API Client

```bash
pip install "fontfyi[api]"
```

```python
from fontfyi.api import FontFYI

with FontFYI() as api:
    info = api.font("inter")           # GET /api/font/inter/
    css = api.css("inter")             # GET /api/font/inter/css/
    results = api.search("mono")       # GET /api/search/?q=mono
    pairings = api.pairings("inter")   # GET /api/pairings/inter/
    stacks = api.stacks()              # GET /api/font-stacks/
```

Full [API documentation](https://fontfyi.com/developers/) with OpenAPI spec at [fontfyi.com/api/openapi.json](https://fontfyi.com/api/openapi.json).

## API Reference

### Font Data

| Function | Description |
|----------|-------------|
| `get_font(slug) -> dict \| None` | Look up font by slug |
| `search(query, limit=20) -> list[dict]` | Search fonts by name |
| `by_category(category) -> list[dict]` | Filter by category |
| `popular(limit=20) -> list[dict]` | Top fonts by popularity |
| `all_fonts() -> list[dict]` | All 50 fonts |
| `font_count() -> int` | Total font count |

### CSS Utilities

| Function | Description |
|----------|-------------|
| `css_family(family, category) -> str` | `'Inter', sans-serif` |
| `google_fonts_url(family, weights?) -> str` | Google Fonts CSS URL |
| `google_fonts_link(family, weights?) -> str` | HTML `<link>` tag |
| `google_download_url(family) -> str` | Direct download URL |
| `homebrew_install_cmd(family) -> str` | `brew install --cask font-inter` |
| `parse_variants(variants) -> (weights, italic)` | Parse variant strings |
| `weight_name(weight) -> str` | `400` -> `"Regular"` |

### Font Stacks

| Function | Description |
|----------|-------------|
| `get_stack(slug) -> FontStack \| None` | Get a [font stack](https://fontfyi.com/tools/font-stack/) by slug |
| `FONT_STACKS` | All 10 curated font stacks |

Available stacks: `system-ui`, `transitional`, `old-style`, `humanist`, `geometric-humanist`, `neo-grotesque`, `monospace-slab`, `monospace-code`, `industrial`, `rounded`

### Font Pairings

| Function | Description |
|----------|-------------|
| `get_pairings_for(slug) -> list[FontPairing]` | [Pairings](https://fontfyi.com/pairings/) containing a font |
| `featured_pairings() -> list[FontPairing]` | Score >= 8 pairings |
| `PAIRINGS` | All 15 curated pairings |

## Data Types

- **`FontStack`** -- NamedTuple: slug, name, description, stack
- **`FontPairing`** -- NamedTuple: heading, body, rationale, score, use_cases, mood

## Features

- **50 Google Fonts**: family, category, variants, subsets, designer, popularity rank
- **CSS generation**: font-family declarations, Google Fonts URLs, HTML link tags
- **Weight parsing**: variant strings to numeric weights with italic detection
- **10 font stacks**: system-ui, transitional, humanist, neo-grotesque, monospace, and more
- **15 font pairings**: Curated heading + body combinations with rationale and scores
- **Homebrew commands**: `brew install --cask font-{name}` generator
- **CLI**: Rich terminal output with font info, search, CSS snippets
- **MCP server**: 6 tools for AI assistants (Claude, Cursor, Windsurf)
- **REST API client**: httpx-based client for [fontfyi.com API](https://fontfyi.com/developers/)
- **Zero dependencies**: Core engine uses only `json` and `pathlib` from stdlib
- **Type-safe**: Full type annotations, `py.typed` marker (PEP 561)

## Learn More About Fonts

- **Browse**: [Google Fonts Browser](https://fontfyi.com/) · [Font Search](https://fontfyi.com/search/) · [Categories](https://fontfyi.com/category/)
- **Tools**: - **Guides**: [Glossary](https://fontfyi.com/glossary/) · [Blog](https://fontfyi.com/blog/)
- **API**: [REST API Docs](https://fontfyi.com/developers/) · [OpenAPI Spec](https://fontfyi.com/api/openapi.json)

## Creative FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — design, typography, and character encoding.

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies -- [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis -- [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats -- [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings -- [unicodefyi.com](https://unicodefyi.com/) |
| **fontfyi** | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | **Google Fonts metadata & CSS -- [fontfyi.com](https://fontfyi.com/)** |

## License

MIT
