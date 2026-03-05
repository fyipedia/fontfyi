# fontfyi

[![PyPI](https://img.shields.io/pypi/v/fontfyi)](https://pypi.org/project/fontfyi/)
[![Python](https://img.shields.io/pypi/pyversions/fontfyi)](https://pypi.org/project/fontfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Pure Python Google Fonts toolkit. Access [50 popular fonts](https://fontfyi.com/fonts/) metadata, generate CSS import URLs, browse [10 web-safe font stacks](https://fontfyi.com/tools/font-stack/), and [15 curated font pairings](https://fontfyi.com/pairings/) -- all with zero dependencies.

> **Explore all fonts at [fontfyi.com](https://fontfyi.com/)** -- [font explorer](https://fontfyi.com/fonts/), [font pairings](https://fontfyi.com/pairings/), [font stacks](https://fontfyi.com/tools/font-stack/), and [developer API](https://fontfyi.com/developers/).

<p align="center">
  <img src="demo.gif" alt="fontfyi CLI demo" width="800">
</p>

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

## FYIPedia Developer Tools

Part of the [FYIPedia](https://github.com/fyipedia) open-source developer tools ecosystem:

| Package | Description |
|---------|-------------|
| [colorfyi](https://colorfyi.com/) | [Hex to RGB converter](https://colorfyi.com/tools/converter/), [WCAG contrast checker](https://colorfyi.com/tools/contrast-checker/), [color harmonies](https://colorfyi.com/tools/palette-generator/) |
| [emojifyi](https://emojifyi.com/) | [Emoji encoding](https://emojifyi.com/developers/) & metadata for 3,781 Unicode emojis |
| [symbolfyi](https://symbolfyi.com/) | [Symbol encoder](https://symbolfyi.com/developers/) -- 11 encoding formats for any character |
| [unicodefyi](https://unicodefyi.com/) | [Unicode character lookup](https://unicodefyi.com/developers/) -- 17 encodings + character search |
| **fontfyi** | [Google Fonts explorer](https://fontfyi.com/developers/) -- metadata, CSS helpers, font pairings |
| [distancefyi](https://pypi.org/project/distancefyi/) | Haversine distance, bearing, travel times -- [distancefyi.com](https://distancefyi.com/) |
| [timefyi](https://pypi.org/project/timefyi/) | Timezone operations, time differences -- [timefyi.com](https://timefyi.com/) |
| [namefyi](https://pypi.org/project/namefyi/) | Korean romanization, Five Elements -- [namefyi.com](https://namefyi.com/) |
| [unitfyi](https://pypi.org/project/unitfyi/) | Unit conversion, 200 units, 20 categories -- [unitfyi.com](https://unitfyi.com/) |
| [holidayfyi](https://pypi.org/project/holidayfyi/) | Holiday dates, Easter calculation -- [holidayfyi.com](https://holidayfyi.com/) |

## Links

- [Font Explorer](https://fontfyi.com/fonts/) -- Browse all Google Fonts
- [Font Pairings](https://fontfyi.com/pairings/) -- Curated heading + body combinations
- [Font Stacks](https://fontfyi.com/tools/font-stack/) -- CSS-ready font stack presets
- [REST API Documentation](https://fontfyi.com/developers/) -- Free API with OpenAPI spec
- [Source Code](https://github.com/fyipedia/fontfyi) -- MIT licensed

## License

MIT
