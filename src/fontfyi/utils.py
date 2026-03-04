"""Font utility functions — CSS generation, weight parsing, URL building.

Pure Python, zero dependencies.
"""

from __future__ import annotations

# Weight name mapping (CSS standard)
WEIGHT_NAMES: dict[int, str] = {
    100: "Thin",
    200: "Extra Light",
    300: "Light",
    400: "Regular",
    500: "Medium",
    600: "Semi Bold",
    700: "Bold",
    800: "Extra Bold",
    900: "Black",
}

# Category fallbacks for CSS font-family
CATEGORY_FALLBACKS: dict[str, str] = {
    "sans-serif": "sans-serif",
    "serif": "serif",
    "display": "system-ui",
    "handwriting": "cursive",
    "monospace": "monospace",
}


def parse_variants(variants: list[str]) -> tuple[list[int], bool]:
    """Parse Google Fonts variant strings into numeric weights and italic flag.

    Returns (sorted weights, has_italic).

    >>> weights, has_italic = parse_variants(["100", "regular", "700", "italic", "700italic"])
    >>> weights
    [100, 400, 700]
    >>> has_italic
    True
    """
    weights: set[int] = set()
    has_italic = False

    for v in variants:
        if v == "regular":
            weights.add(400)
        elif v == "italic":
            weights.add(400)
            has_italic = True
        elif v.endswith("italic"):
            has_italic = True
            w = v.replace("italic", "")
            if w:
                weights.add(int(w))
        elif v.isdigit():
            weights.add(int(v))

    return sorted(weights), has_italic


def weight_name(weight: int) -> str:
    """Get CSS weight name for a numeric weight.

    >>> weight_name(400)
    'Regular'
    >>> weight_name(700)
    'Bold'
    """
    return WEIGHT_NAMES.get(weight, str(weight))


def css_family(family: str, category: str) -> str:
    """Generate CSS font-family declaration with fallback.

    >>> css_family("Inter", "sans-serif")
    "'Inter', sans-serif"
    >>> css_family("Roboto Mono", "monospace")
    "'Roboto Mono', monospace"
    """
    fallback = CATEGORY_FALLBACKS.get(category, "sans-serif")
    return f"'{family}', {fallback}"


def google_fonts_url(family: str, weights: list[int] | None = None) -> str:
    """Generate Google Fonts CSS import URL.

    >>> google_fonts_url("Inter", [400, 700])
    'https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap'
    >>> google_fonts_url("Roboto")
    'https://fonts.googleapis.com/css2?family=Roboto&display=swap'
    """
    encoded = family.replace(" ", "+")
    if weights:
        weight_str = ";".join(str(w) for w in sorted(weights))
        return f"https://fonts.googleapis.com/css2?family={encoded}:wght@{weight_str}&display=swap"
    return f"https://fonts.googleapis.com/css2?family={encoded}&display=swap"


def google_fonts_link(family: str, weights: list[int] | None = None) -> str:
    """Generate HTML link tag for Google Fonts.

    >>> '<link' in google_fonts_link("Inter", [400, 700])
    True
    """
    url = google_fonts_url(family, weights)
    return f'<link rel="stylesheet" href="{url}">'


def google_download_url(family: str) -> str:
    """Generate Google Fonts download URL.

    >>> google_download_url("Inter")
    'https://fonts.google.com/download?family=Inter'
    """
    return f"https://fonts.google.com/download?family={family}"


def homebrew_install_cmd(family: str) -> str:
    """Generate Homebrew cask install command for a font.

    >>> homebrew_install_cmd("JetBrains Mono")
    'brew install --cask font-jetbrains-mono'
    """
    slug = family.lower().replace(" ", "-")
    return f"brew install --cask font-{slug}"
