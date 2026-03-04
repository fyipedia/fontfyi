"""MCP server for fontfyi -- font tools for AI assistants.

Requires the ``mcp`` extra: ``pip install fontfyi[mcp]``

Run as a standalone server::

    python -m fontfyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "fontfyi": {
                "command": "python",
                "args": ["-m", "fontfyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fontfyi")


@mcp.tool()
def font_info(slug: str) -> str:
    """Get comprehensive metadata for a Google Font.

    Returns family name, category, weights, subsets, designer, and popularity rank.

    Args:
        slug: Font slug (e.g. "inter", "roboto", "playfair-display").
    """
    from fontfyi import get_font, parse_variants

    font = get_font(slug)
    if font is None:
        return f"Font not found: {slug}"

    variants = font.get("variants", [])
    weights, has_italic = parse_variants(variants)
    subsets = font.get("subsets", [])

    return "\n".join(
        [
            f"## {font['family']}",
            "",
            "| Property | Value |",
            "|----------|-------|",
            f"| Family | {font['family']} |",
            f"| Slug | `{font['slug']}` |",
            f"| Category | {font['category']} |",
            f"| Designer | {font.get('designer', 'Unknown')} |",
            f"| Weights | {', '.join(str(w) for w in weights)} |",
            f"| Italic | {'Yes' if has_italic else 'No'} |",
            f"| Subsets | {', '.join(subsets)} |",
            f"| Popularity | #{font.get('popularity_rank', 'N/A')} |",
        ]
    )


@mcp.tool()
def font_search(query: str, limit: int = 10) -> str:
    """Search Google Fonts by family name.

    Returns matching fonts with their category and popularity rank.

    Args:
        query: Search term (e.g. "mono", "serif", "rob").
        limit: Maximum number of results (default 10).
    """
    from fontfyi import search

    results = search(query, limit=limit)
    if not results:
        return f"No fonts found for: {query}"

    lines = [
        f"## Search: {query}",
        "",
        "| Family | Category | Rank |",
        "|--------|----------|------|",
    ]
    for font in results:
        lines.append(
            f"| {font['family']} | {font['category']} | #{font.get('popularity_rank', 'N/A')} |"
        )

    return "\n".join(lines)


@mcp.tool()
def font_css(slug: str) -> str:
    """Get CSS import snippet for a Google Font.

    Returns the HTML link tag and CSS font-family declaration.

    Args:
        slug: Font slug (e.g. "inter", "roboto-mono").
    """
    from fontfyi import css_family, get_font, google_fonts_url, parse_variants

    font = get_font(slug)
    if font is None:
        return f"Font not found: {slug}"

    weights, _italic = parse_variants(font.get("variants", []))
    url = google_fonts_url(font["family"], weights or None)
    family_decl = css_family(font["family"], font["category"])

    return "\n".join(
        [
            f"## CSS for {font['family']}",
            "",
            "**HTML link tag:**",
            "```html",
            f'<link rel="stylesheet" href="{url}">',
            "```",
            "",
            "**CSS font-family:**",
            "```css",
            f"font-family: {family_decl};",
            "```",
        ]
    )


@mcp.tool()
def font_pairings(slug: str) -> str:
    """Get font pairing recommendations for a Google Font.

    Returns heading + body combinations with rationale, score, and mood.

    Args:
        slug: Font slug (e.g. "inter", "playfair-display").
    """
    from fontfyi import get_font, get_pairings_for

    font = get_font(slug)
    if font is None:
        return f"Font not found: {slug}"

    pairings = get_pairings_for(slug)
    if not pairings:
        return f"No pairings found for: {font['family']}"

    lines = [
        f"## Pairings for {font['family']}",
        "",
    ]
    for p in pairings:
        lines.extend(
            [
                f"### {p.heading} + {p.body} (score: {p.score})",
                f"- **Mood**: {p.mood}",
                f"- **Use cases**: {', '.join(p.use_cases)}",
                f"- {p.rationale}",
                "",
            ]
        )

    return "\n".join(lines)


@mcp.tool()
def font_stacks() -> str:
    """Get all 10 CSS font stack presets.

    Returns curated font stacks for common use cases like system UI,
    monospace, serif, and humanist sans.
    """
    from fontfyi import FONT_STACKS

    lines = [
        "## Font Stacks",
        "",
        "| Name | Description | Stack |",
        "|------|-------------|-------|",
    ]
    for stack in FONT_STACKS:
        lines.append(f"| {stack.name} | {stack.description} | `{stack.stack}` |")

    return "\n".join(lines)


@mcp.tool()
def popular_fonts(limit: int = 10) -> str:
    """Get the most popular Google Fonts by usage rank.

    Args:
        limit: Number of fonts to return (default 10).
    """
    from fontfyi import popular

    fonts = popular(limit)

    lines = [
        f"## Top {limit} Google Fonts",
        "",
        "| Rank | Family | Category | Designer |",
        "|------|--------|----------|----------|",
    ]
    for font in fonts:
        lines.append(
            f"| #{font.get('popularity_rank', 'N/A')}"
            f" | {font['family']}"
            f" | {font['category']}"
            f" | {font.get('designer', '')} |"
        )

    return "\n".join(lines)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
