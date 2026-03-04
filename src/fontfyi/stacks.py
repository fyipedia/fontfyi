"""CSS web-safe font stack presets — 10 curated stacks for common use cases.

Each stack provides a complete CSS font-family value with
platform-specific fallbacks.
"""

from __future__ import annotations

from typing import NamedTuple


class FontStack(NamedTuple):
    """A CSS font stack preset."""

    slug: str
    name: str
    description: str
    stack: str


FONT_STACKS: list[FontStack] = [
    FontStack(
        slug="system-ui",
        name="System UI",
        description="The native system font on each platform.",
        stack="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
    ),
    FontStack(
        slug="transitional",
        name="Transitional",
        description="Classic serif stack for traditional body text.",
        stack="Charter, 'Bitstream Charter', 'Sitka Text', Cambria, serif",
    ),
    FontStack(
        slug="old-style",
        name="Old Style",
        description="Elegant serif fonts with calligraphic origins.",
        stack="'Iowan Old Style', 'Palatino Linotype', 'URW Palladio L', P052, serif",
    ),
    FontStack(
        slug="humanist",
        name="Humanist Sans",
        description="Organic, calligraphic-inspired sans serif.",
        stack="Seravek, 'Gill Sans Nova', Ubuntu, Calibri, 'DejaVu Sans', source-sans-pro, sans-serif",
    ),
    FontStack(
        slug="geometric-humanist",
        name="Geometric Humanist",
        description="Clean, modern geometric sans.",
        stack="Avenir, Montserrat, Corbel, 'URW Gothic', source-sans-pro, sans-serif",
    ),
    FontStack(
        slug="neo-grotesque",
        name="Neo-grotesque",
        description="Neutral, versatile sans-serif.",
        stack="Inter, Roboto, 'Helvetica Neue', 'Arial Nova', 'Nimbus Sans', Arial, sans-serif",
    ),
    FontStack(
        slug="monospace-slab",
        name="Monospace Slab",
        description="Monospace with slab serif character.",
        stack="'Nimbus Mono PS', 'Courier New', monospace",
    ),
    FontStack(
        slug="monospace-code",
        name="Monospace Code",
        description="Modern monospace optimized for code.",
        stack="ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace",
    ),
    FontStack(
        slug="industrial",
        name="Industrial",
        description="Bold, impactful sans serif.",
        stack="Bahnschrift, 'DIN Alternate', 'Franklin Gothic Medium', 'Nimbus Sans Narrow', sans-serif-condensed, sans-serif",
    ),
    FontStack(
        slug="rounded",
        name="Rounded Sans",
        description="Friendly, rounded sans serif.",
        stack="ui-rounded, 'Hiragino Maru Gothic ProN', Quicksand, Comfortaa, Manjari, 'Arial Rounded MT', 'Arial Rounded MT Bold', Calibri, source-sans-pro, sans-serif",
    ),
]

_BY_SLUG: dict[str, FontStack] = {s.slug: s for s in FONT_STACKS}


def get_stack(slug: str) -> FontStack | None:
    """Get a font stack by slug.

    >>> stack = get_stack("system-ui")
    >>> stack.name if stack else None
    'System UI'
    """
    return _BY_SLUG.get(slug)
