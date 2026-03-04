"""Google Fonts metadata — lazy-loaded from bundled JSON.

Provides access to 50 popular Google Fonts with full metadata including
family name, category, variants, subsets, designer, and popularity rank.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_DATA_DIR = Path(__file__).parent / "_data"

_Row = dict[str, Any]

# Module-level caches
_fonts: list[_Row] | None = None
_by_slug: dict[str, _Row] | None = None


def _load_fonts() -> list[_Row]:
    global _fonts
    if _fonts is None:
        with open(_DATA_DIR / "fonts.json", encoding="utf-8") as f:
            _fonts = json.load(f)
    return _fonts


def _load_by_slug() -> dict[str, _Row]:
    global _by_slug
    if _by_slug is None:
        _by_slug = {f["slug"]: f for f in _load_fonts()}
    return _by_slug


def get_font(slug: str) -> _Row | None:
    """Get font metadata by slug.

    >>> font = get_font("inter")
    >>> font["family"] if font else None
    'Inter'
    """
    return _load_by_slug().get(slug)


def search(query: str, limit: int = 20) -> list[_Row]:
    """Search fonts by family name (case-insensitive).

    >>> results = search("rob")
    >>> len(results) > 0
    True
    """
    q = query.lower()
    results: list[_Row] = []
    for font in _load_fonts():
        if q in font["family"].lower():
            results.append(font)
            if len(results) >= limit:
                break
    return results


def by_category(category: str) -> list[_Row]:
    """Get fonts by category (sans-serif, serif, display, handwriting, monospace).

    >>> len(by_category("sans-serif")) > 0
    True
    """
    return [f for f in _load_fonts() if f["category"] == category]


def popular(limit: int = 20) -> list[_Row]:
    """Get most popular fonts sorted by popularity rank.

    >>> fonts = popular(5)
    >>> fonts[0]["slug"]
    'roboto'
    """
    return sorted(_load_fonts(), key=lambda f: int(f["popularity_rank"]))[:limit]


def all_fonts() -> list[_Row]:
    """Get all bundled fonts.

    >>> len(all_fonts()) >= 50
    True
    """
    return list(_load_fonts())


def font_count() -> int:
    """Get total number of bundled fonts."""
    return len(_load_fonts())
