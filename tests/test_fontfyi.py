"""Tests for fontfyi package."""

from __future__ import annotations

from fontfyi import (
    FONT_STACKS,
    PAIRINGS,
    WEIGHT_NAMES,
    FontPairing,
    FontStack,
    all_fonts,
    by_category,
    css_family,
    featured_pairings,
    font_count,
    get_font,
    get_pairings_for,
    get_stack,
    google_download_url,
    google_fonts_link,
    google_fonts_url,
    homebrew_install_cmd,
    parse_variants,
    popular,
    search,
    weight_name,
)


# =============================================================================
# Font data
# =============================================================================
class TestFontData:
    def test_get_font(self) -> None:
        font = get_font("roboto")
        assert font is not None
        assert font["family"] == "Roboto"
        assert font["category"] == "sans-serif"

    def test_get_font_not_found(self) -> None:
        assert get_font("nonexistent-font") is None

    def test_search(self) -> None:
        results = search("rob")
        assert len(results) > 0
        assert any(r["slug"] == "roboto" for r in results)

    def test_search_case_insensitive(self) -> None:
        results = search("ROBOTO")
        assert len(results) > 0

    def test_search_limit(self) -> None:
        results = search("o", limit=3)
        assert len(results) <= 3

    def test_by_category(self) -> None:
        sans = by_category("sans-serif")
        assert len(sans) > 0
        assert all(f["category"] == "sans-serif" for f in sans)

    def test_popular(self) -> None:
        top = popular(5)
        assert len(top) == 5
        assert top[0]["slug"] == "roboto"

    def test_all_fonts(self) -> None:
        fonts = all_fonts()
        assert len(fonts) >= 50

    def test_font_count(self) -> None:
        assert font_count() >= 50


# =============================================================================
# CSS utilities
# =============================================================================
class TestUtils:
    def test_parse_variants(self) -> None:
        weights, has_italic = parse_variants(["100", "regular", "700", "italic", "700italic"])
        assert weights == [100, 400, 700]
        assert has_italic is True

    def test_parse_variants_no_italic(self) -> None:
        weights, has_italic = parse_variants(["300", "regular", "700"])
        assert weights == [300, 400, 700]
        assert has_italic is False

    def test_weight_name(self) -> None:
        assert weight_name(400) == "Regular"
        assert weight_name(700) == "Bold"
        assert weight_name(100) == "Thin"

    def test_css_family(self) -> None:
        assert css_family("Inter", "sans-serif") == "'Inter', sans-serif"
        assert css_family("Roboto Mono", "monospace") == "'Roboto Mono', monospace"

    def test_google_fonts_url(self) -> None:
        url = google_fonts_url("Inter", [400, 700])
        assert "family=Inter:wght@400;700" in url
        assert "display=swap" in url

    def test_google_fonts_url_no_weights(self) -> None:
        url = google_fonts_url("Roboto")
        assert "family=Roboto&" in url

    def test_google_fonts_url_spaces(self) -> None:
        url = google_fonts_url("Open Sans", [400])
        assert "family=Open+Sans" in url

    def test_google_fonts_link(self) -> None:
        html = google_fonts_link("Inter", [400])
        assert html.startswith("<link")
        assert "fonts.googleapis.com" in html

    def test_google_download_url(self) -> None:
        url = google_download_url("Inter")
        assert url == "https://fonts.google.com/download?family=Inter"

    def test_homebrew_install_cmd(self) -> None:
        cmd = homebrew_install_cmd("JetBrains Mono")
        assert cmd == "brew install --cask font-jetbrains-mono"

    def test_weight_names_constant(self) -> None:
        assert len(WEIGHT_NAMES) == 9
        assert 400 in WEIGHT_NAMES


# =============================================================================
# Font stacks
# =============================================================================
class TestFontStacks:
    def test_stacks_count(self) -> None:
        assert len(FONT_STACKS) == 10

    def test_stack_type(self) -> None:
        assert isinstance(FONT_STACKS[0], FontStack)

    def test_get_stack(self) -> None:
        stack = get_stack("system-ui")
        assert stack is not None
        assert stack.name == "System UI"
        assert "system-ui" in stack.stack

    def test_get_stack_not_found(self) -> None:
        assert get_stack("nonexistent") is None

    def test_monospace_code(self) -> None:
        stack = get_stack("monospace-code")
        assert stack is not None
        assert "monospace" in stack.stack


# =============================================================================
# Pairings
# =============================================================================
class TestPairings:
    def test_pairings_count(self) -> None:
        assert len(PAIRINGS) == 15

    def test_pairing_type(self) -> None:
        assert isinstance(PAIRINGS[0], FontPairing)

    def test_get_pairings_for(self) -> None:
        pairings = get_pairings_for("inter")
        assert len(pairings) >= 3
        for p in pairings:
            assert p.heading == "inter" or p.body == "inter"

    def test_get_pairings_for_not_found(self) -> None:
        assert len(get_pairings_for("nonexistent")) == 0

    def test_featured_pairings(self) -> None:
        featured = featured_pairings()
        assert len(featured) > 5
        assert all(p.score >= 8 for p in featured)


# =============================================================================
# Exports
# =============================================================================
class TestExports:
    def test_all_types(self) -> None:
        assert FontStack is not None
        assert FontPairing is not None


# =============================================================================
# Edge cases
# =============================================================================
class TestEdgeCases:
    def test_get_font_not_found(self) -> None:
        assert get_font("this-font-does-not-exist") is None

    def test_search_empty(self) -> None:
        results = search("", limit=5)
        assert len(results) == 5  # matches everything

    def test_search_limit_large(self) -> None:
        results = search("o", limit=1000)
        assert len(results) <= 50  # can't exceed total fonts

    def test_popular_zero(self) -> None:
        results = popular(0)
        assert len(results) == 0

    def test_by_category_invalid(self) -> None:
        results = by_category("nonexistent")
        assert len(results) == 0

    def test_get_stack_not_found(self) -> None:
        assert get_stack("nonexistent-stack") is None

    def test_pairings_no_match(self) -> None:
        assert len(get_pairings_for("nonexistent")) == 0

    def test_parse_variants_empty(self) -> None:
        weights, has_italic = parse_variants([])
        assert weights == []
        assert has_italic is False

    def test_all_pairing_fonts_exist(self) -> None:
        """Ensure every font referenced in pairings exists in data."""
        for p in PAIRINGS:
            assert get_font(p.heading) is not None, f"Missing heading font: {p.heading}"
            assert get_font(p.body) is not None, f"Missing body font: {p.body}"

    def test_weight_name_unknown(self) -> None:
        assert weight_name(450) == "450"  # non-standard weight
