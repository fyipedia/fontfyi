"""fontfyi — Pure Python Google Fonts toolkit.

Access 50 popular Google Fonts metadata, generate CSS import URLs,
browse 10 font stacks, 15 curated pairings, and font utility functions.

Zero dependencies.

Usage::

    from fontfyi import get_font, search, google_fonts_url, css_family

    # Look up a font
    font = get_font("inter")
    print(font["family"])       # Inter
    print(font["category"])     # sans-serif
    print(font["variants"])     # ["regular", "500", "700", ...]

    # Generate CSS
    print(css_family("Inter", "sans-serif"))  # 'Inter', sans-serif
    print(google_fonts_url("Inter", [400, 700]))

    # Font stacks
    from fontfyi import get_stack
    stack = get_stack("system-ui")
    print(stack.stack)  # system-ui, -apple-system, ...

    # Font pairings
    from fontfyi import get_pairings_for
    for p in get_pairings_for("inter"):
        print(f"{p.heading} + {p.body} ({p.mood})")
"""

from fontfyi.data import (
    all_fonts,
    by_category,
    font_count,
    get_font,
    popular,
    search,
)
from fontfyi.pairings import (
    PAIRINGS,
    FontPairing,
    featured_pairings,
    get_pairings_for,
)
from fontfyi.stacks import (
    FONT_STACKS,
    FontStack,
    get_stack,
)
from fontfyi.utils import (
    CATEGORY_FALLBACKS,
    WEIGHT_NAMES,
    css_family,
    google_download_url,
    google_fonts_link,
    google_fonts_url,
    homebrew_install_cmd,
    parse_variants,
    weight_name,
)

__version__ = "0.1.0"

__all__ = [
    # Data access
    "get_font",
    "search",
    "by_category",
    "popular",
    "all_fonts",
    "font_count",
    # CSS utilities
    "css_family",
    "google_fonts_url",
    "google_fonts_link",
    "google_download_url",
    "homebrew_install_cmd",
    "parse_variants",
    "weight_name",
    # Font stacks
    "FontStack",
    "FONT_STACKS",
    "get_stack",
    # Pairings
    "FontPairing",
    "PAIRINGS",
    "get_pairings_for",
    "featured_pairings",
    # Data constants
    "WEIGHT_NAMES",
    "CATEGORY_FALLBACKS",
]
