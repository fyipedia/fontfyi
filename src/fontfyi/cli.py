"""Command-line interface for fontfyi.

Requires the ``cli`` extra: ``pip install fontfyi[cli]``

Usage::

    fontfyi info inter                     # Font metadata
    fontfyi search mono                    # Search fonts
    fontfyi css inter                      # CSS import snippet
    fontfyi pair inter                     # Font pairings
    fontfyi popular                        # Top fonts by popularity
    fontfyi stacks                         # Font stack presets
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="fontfyi",
    help=("Pure Python Google Fonts toolkit -- metadata, CSS helpers, and font pairings."),
    no_args_is_help=True,
)
console = Console()


@app.command()
def info(
    slug: str = typer.Argument(help="Font slug (e.g. inter, roboto)"),
) -> None:
    """Get comprehensive font metadata."""
    from fontfyi import get_font, parse_variants

    font = get_font(slug)
    if font is None:
        console.print(f"[red]Font not found:[/red] {slug}")
        raise typer.Exit(code=1)

    table = Table(title=f"Font: {font['family']}")
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value")

    table.add_row("Family", font["family"])
    table.add_row("Slug", font["slug"])
    table.add_row("Category", font["category"])
    table.add_row("Designer", font.get("designer", "Unknown"))

    variants = font.get("variants", [])
    weights, has_italic = parse_variants(variants)
    table.add_row("Weights", ", ".join(str(w) for w in weights))
    table.add_row("Italic", "Yes" if has_italic else "No")
    table.add_row("Variants", ", ".join(variants))

    subsets = font.get("subsets", [])
    table.add_row("Subsets", ", ".join(subsets))

    rank = font.get("popularity_rank", "N/A")
    table.add_row("Popularity", f"#{rank}")

    from fontfyi import google_fonts_url

    url = google_fonts_url(font["family"], weights or None)
    table.add_row("CSS Import", url)

    console.print(table)


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. mono, serif)"),
    limit: int = typer.Option(20, help="Maximum results"),
) -> None:
    """Search fonts by family name."""
    from fontfyi import search as _search

    results = _search(query, limit=limit)
    if not results:
        console.print(f"[yellow]No fonts found for:[/yellow] {query}")
        raise typer.Exit()

    table = Table(title=f"Search: {query}")
    table.add_column("#", style="dim", justify="right")
    table.add_column("Family", style="bold")
    table.add_column("Category")
    table.add_column("Rank", justify="right")

    for i, font in enumerate(results, 1):
        table.add_row(
            str(i),
            font["family"],
            font["category"],
            str(font.get("popularity_rank", "")),
        )

    console.print(table)


@app.command()
def css(
    slug: str = typer.Argument(help="Font slug (e.g. inter, roboto)"),
) -> None:
    """Generate CSS import snippet for a font."""
    from fontfyi import css_family, get_font, google_fonts_link, parse_variants

    font = get_font(slug)
    if font is None:
        console.print(f"[red]Font not found:[/red] {slug}")
        raise typer.Exit(code=1)

    weights, _italic = parse_variants(font.get("variants", []))
    link_tag = google_fonts_link(font["family"], weights or None)
    family_decl = css_family(font["family"], font["category"])

    console.print()
    console.print("[bold cyan]HTML link tag:[/bold cyan]")
    console.print(link_tag)
    console.print()
    console.print("[bold cyan]CSS font-family:[/bold cyan]")
    console.print(f"font-family: {family_decl};")
    console.print()


@app.command()
def pair(
    slug: str = typer.Argument(help="Font slug (e.g. inter, roboto)"),
) -> None:
    """Show font pairing recommendations."""
    from fontfyi import get_font, get_pairings_for

    font = get_font(slug)
    if font is None:
        console.print(f"[red]Font not found:[/red] {slug}")
        raise typer.Exit(code=1)

    pairings = get_pairings_for(slug)
    if not pairings:
        console.print(f"[yellow]No pairings found for:[/yellow] {font['family']}")
        raise typer.Exit()

    table = Table(title=f"Pairings for {font['family']}")
    table.add_column("Heading", style="bold")
    table.add_column("Body", style="bold")
    table.add_column("Score", justify="right")
    table.add_column("Mood")
    table.add_column("Rationale", max_width=50)

    for p in pairings:
        table.add_row(
            p.heading,
            p.body,
            str(p.score),
            p.mood,
            p.rationale,
        )

    console.print(table)


@app.command()
def popular(
    limit: int = typer.Option(20, help="Number of fonts to show"),
) -> None:
    """Show the most popular Google Fonts."""
    from fontfyi import popular as _popular

    fonts = _popular(limit)

    table = Table(title=f"Top {limit} Google Fonts")
    table.add_column("Rank", style="dim", justify="right")
    table.add_column("Family", style="bold")
    table.add_column("Category")
    table.add_column("Designer")

    for font in fonts:
        table.add_row(
            str(font.get("popularity_rank", "")),
            font["family"],
            font["category"],
            font.get("designer", ""),
        )

    console.print(table)


@app.command()
def stacks() -> None:
    """Show all CSS font stack presets."""
    from fontfyi import FONT_STACKS

    table = Table(title="Font Stacks")
    table.add_column("Name", style="bold")
    table.add_column("Description")
    table.add_column("Stack", max_width=60)

    for stack in FONT_STACKS:
        table.add_row(stack.name, stack.description, stack.stack)

    console.print(table)
