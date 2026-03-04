"""Font pairing recommendations — 15 curated heading + body combinations.

Each pairing includes a rationale, quality score, use cases, and mood
classification.
"""

from __future__ import annotations

from typing import NamedTuple


class FontPairing(NamedTuple):
    """A curated heading + body font pairing."""

    heading: str
    body: str
    rationale: str
    score: int
    use_cases: list[str]
    mood: str


PAIRINGS: list[FontPairing] = [
    FontPairing(
        heading="inter",
        body="merriweather",
        rationale="Inter's clean geometric forms create a modern heading that pairs beautifully with Merriweather's warm, readable serifs for body text.",
        score=9,
        use_cases=["blog", "portfolio", "documentation"],
        mood="professional-modern",
    ),
    FontPairing(
        heading="playfair-display",
        body="source-sans-3",
        rationale="Playfair Display's high-contrast elegance provides dramatic headlines, while Source Sans 3's neutral clarity ensures comfortable body reading.",
        score=9,
        use_cases=["blog", "magazine", "portfolio"],
        mood="editorial-elegant",
    ),
    FontPairing(
        heading="poppins",
        body="inter",
        rationale="Poppins' geometric roundness adds warmth to headlines, while Inter's clean precision handles body text effortlessly.",
        score=9,
        use_cases=["landing-page", "saas", "mobile-app"],
        mood="modern-friendly",
    ),
    FontPairing(
        heading="montserrat",
        body="roboto",
        rationale="Montserrat's bold geometric style makes striking headlines, while Roboto's mechanical yet friendly forms provide excellent body readability.",
        score=8,
        use_cases=["landing-page", "e-commerce", "startup"],
        mood="bold-professional",
    ),
    FontPairing(
        heading="oswald",
        body="open-sans",
        rationale="Oswald's condensed boldness grabs attention in headlines, and Open Sans provides a neutral, highly readable body companion.",
        score=8,
        use_cases=["news", "blog", "content-site"],
        mood="bold-clean",
    ),
    FontPairing(
        heading="space-grotesk",
        body="inter",
        rationale="Space Grotesk brings a distinctive tech-forward personality to headlines while Inter's neutrality lets body content breathe.",
        score=8,
        use_cases=["saas", "tech", "developer-tools"],
        mood="tech-modern",
    ),
    FontPairing(
        heading="dm-sans",
        body="dm-serif-display",
        rationale="From the same design family, DM Sans and DM Serif share proportional DNA, creating natural harmony.",
        score=8,
        use_cases=["portfolio", "agency", "editorial"],
        mood="harmonious-elegant",
    ),
    FontPairing(
        heading="raleway",
        body="lora",
        rationale="Raleway's thin elegance creates sophisticated headlines, while Lora's well-balanced serifs offer comfortable extended reading.",
        score=8,
        use_cases=["blog", "portfolio", "wedding"],
        mood="elegant-refined",
    ),
    FontPairing(
        heading="work-sans",
        body="source-serif-4",
        rationale="Work Sans provides friendly, approachable headlines with subtle quirks, while Source Serif 4 brings traditional readability to body text.",
        score=7,
        use_cases=["blog", "nonprofit", "education"],
        mood="warm-professional",
    ),
    FontPairing(
        heading="plus-jakarta-sans",
        body="inter",
        rationale="Plus Jakarta Sans offers a contemporary, slightly playful geometric headline, while Inter provides clean, efficient body text.",
        score=8,
        use_cases=["saas", "startup", "dashboard"],
        mood="modern-clean",
    ),
    FontPairing(
        heading="cormorant-garamond",
        body="lato",
        rationale="Cormorant Garamond's dramatic, high-contrast serifs create luxurious headlines, while Lato's humanist warmth offers modern body readability.",
        score=7,
        use_cases=["fashion", "luxury", "editorial"],
        mood="luxury-dramatic",
    ),
    FontPairing(
        heading="bebas-neue",
        body="roboto",
        rationale="Bebas Neue's all-caps condensed impact dominates headlines, while Roboto's versatile neutrality handles body content seamlessly.",
        score=7,
        use_cases=["poster", "landing-page", "sports"],
        mood="bold-impact",
    ),
    FontPairing(
        heading="ibm-plex-sans",
        body="ibm-plex-serif",
        rationale="IBM Plex Sans and Serif share the same design language — co-designed for perfect harmony.",
        score=9,
        use_cases=["documentation", "enterprise", "dashboard"],
        mood="systematic-professional",
    ),
    FontPairing(
        heading="nunito",
        body="nunito-sans",
        rationale="Nunito's rounded terminals make warm, friendly headlines, while Nunito Sans maintains the same proportions in a crisper sans form for body text.",
        score=7,
        use_cases=["education", "children", "friendly-brand"],
        mood="friendly-warm",
    ),
    FontPairing(
        heading="inter",
        body="source-serif-4",
        rationale="Inter's geometric precision creates clean, modern headlines while Source Serif 4's traditional serif forms bring warmth and readability to body text.",
        score=8,
        use_cases=["blog", "documentation", "news"],
        mood="modern-readable",
    ),
]


def get_pairings_for(font_slug: str) -> list[FontPairing]:
    """Get all pairings that include a given font (as heading or body).

    >>> pairings = get_pairings_for("inter")
    >>> len(pairings) >= 3
    True
    """
    return [p for p in PAIRINGS if p.heading == font_slug or p.body == font_slug]


def featured_pairings() -> list[FontPairing]:
    """Get pairings with score >= 8.

    >>> len(featured_pairings()) > 5
    True
    """
    return [p for p in PAIRINGS if p.score >= 8]
