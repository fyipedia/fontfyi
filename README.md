# fontfyi

[![PyPI](https://img.shields.io/pypi/v/fontfyi)](https://pypi.org/project/fontfyi/)
[![Python](https://img.shields.io/pypi/pyversions/fontfyi)](https://pypi.org/project/fontfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Pure Python Google Fonts toolkit. Access 50 popular fonts metadata, generate CSS import URLs, browse 10 web-safe font stacks, and 15 curated font pairings — all with zero dependencies.

> Explore all fonts at [fontfyi.com](https://fontfyi.com/)

## Install

```bash
pip install fontfyi
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

## Advanced Usage

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
| `weight_name(weight) -> str` | `400` → `"Regular"` |

### Font Stacks

| Function | Description |
|----------|-------------|
| `get_stack(slug) -> FontStack \| None` | Get a font stack by slug |
| `FONT_STACKS` | All 10 curated font stacks |

Available stacks: `system-ui`, `transitional`, `old-style`, `humanist`, `geometric-humanist`, `classical-humanist`, `neo-grotesque`, `monospace-slab`, `monospace-code`, `industrial`

### Font Pairings

| Function | Description |
|----------|-------------|
| `get_pairings_for(slug) -> list[FontPairing]` | Pairings containing a font |
| `featured_pairings() -> list[FontPairing]` | Score >= 8 pairings |
| `PAIRINGS` | All 15 curated pairings |

## Data Types

- **`FontStack`** — NamedTuple: slug, name, description, stack
- **`FontPairing`** — NamedTuple: heading, body, rationale, score, use_cases, mood

## Features

- **50 Google Fonts**: family, category, variants, subsets, designer, popularity rank
- **CSS generation**: font-family declarations, Google Fonts URLs, HTML link tags
- **Weight parsing**: variant strings to numeric weights with italic detection
- **10 font stacks**: system-ui, transitional, humanist, neo-grotesque, monospace, and more
- **15 font pairings**: Curated heading + body combinations with rationale and scores
- **Homebrew commands**: `brew install --cask font-{name}` generator
- **Zero dependencies**: Pure Python, bundled JSON data
- **Type-safe**: Full type annotations, `py.typed` marker (PEP 561)

## Related Packages

| Package | Description |
|---------|-------------|
| [colorfyi](https://github.com/fyipedia/colorfyi) | Color conversion, contrast, harmonies, shades |
| [emojifyi](https://github.com/fyipedia/emojifyi) | Emoji encoding & metadata for 3,781 emojis |
| [symbolfyi](https://github.com/fyipedia/symbolfyi) | Symbol & character encoding (11 formats) |
| [unicodefyi](https://github.com/fyipedia/unicodefyi) | Unicode character toolkit (17 encodings) |

## Links

- [Font Explorer](https://fontfyi.com/) — Browse all Google Fonts
- [API Documentation](https://fontfyi.com/developers/) — REST API with free access
- [Source Code](https://github.com/fyipedia/fontfyi)

## License

MIT
