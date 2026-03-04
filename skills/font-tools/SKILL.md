---
name: font-tools
description: Look up Google Fonts metadata, generate CSS import snippets, get font pairing recommendations, and browse font stack presets.
---

# Font Tools

Google Fonts metadata, CSS generation, and font pairing powered by [fontfyi](https://fontfyi.com/) -- a pure Python font toolkit with bundled data for 50 popular Google Fonts.

## Setup

Install the MCP server:

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

## Available Tools

| Tool | Description |
|------|-------------|
| `font_info` | Font metadata (family, category, weights, subsets, CSS import URL) |
| `font_search` | Search fonts by name |
| `font_css` | Generate CSS import snippet (HTML link tag + font-family declaration) |
| `font_pairings` | Font pairing recommendations with rationale and mood |
| `font_stacks` | 10 preset font stacks (system-ui, humanist, neo-grotesque, etc.) |
| `popular_fonts` | Most popular Google Fonts by rank |

## When to Use

- Choosing fonts for a web project
- Generating CSS @import or link tags for Google Fonts
- Finding font pairings (heading + body combinations)
- Looking up font weights, subsets, and categories
- Using system font stacks as fallbacks

## Links

- [Google Fonts Explorer](https://fontfyi.com/fonts/)
- [Font Pairings](https://fontfyi.com/pairings/)
- [Font Stacks](https://fontfyi.com/font-stacks/)
- [API Documentation](https://fontfyi.com/developers/)
- [PyPI Package](https://pypi.org/project/fontfyi/)
