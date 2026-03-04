"""Tests for fontfyi.mcp_server -- MCP tools."""

from __future__ import annotations

from fontfyi.mcp_server import (
    font_css,
    font_info,
    font_pairings,
    font_search,
    font_stacks,
    popular_fonts,
)


class TestMCPFontInfo:
    def test_returns_markdown_table(self) -> None:
        result = font_info("inter")
        assert "## Inter" in result
        assert "Category" in result
        assert "sans-serif" in result

    def test_includes_weights(self) -> None:
        result = font_info("roboto")
        assert "Weights" in result
        assert "400" in result

    def test_not_found(self) -> None:
        result = font_info("nonexistent-font")
        assert "not found" in result.lower()


class TestMCPFontSearch:
    def test_search_results(self) -> None:
        result = font_search("mono")
        assert "Search" in result
        assert "Family" in result

    def test_search_no_results(self) -> None:
        result = font_search("zzzznonexistent")
        assert "No fonts found" in result

    def test_search_with_limit(self) -> None:
        result = font_search("o", limit=3)
        assert "Search" in result


class TestMCPFontCSS:
    def test_returns_css_block(self) -> None:
        result = font_css("inter")
        assert "CSS for Inter" in result
        assert "font-family" in result
        assert "fonts.googleapis.com" in result

    def test_not_found(self) -> None:
        result = font_css("nonexistent-font")
        assert "not found" in result.lower()


class TestMCPFontPairings:
    def test_returns_pairings(self) -> None:
        result = font_pairings("inter")
        assert "Pairings for Inter" in result
        assert "score" in result
        assert "Mood" in result

    def test_not_found(self) -> None:
        result = font_pairings("nonexistent-font")
        assert "not found" in result.lower()


class TestMCPFontStacks:
    def test_returns_all_stacks(self) -> None:
        result = font_stacks()
        assert "Font Stacks" in result
        assert "System UI" in result
        assert "system-ui" in result
        assert "Monospace Code" in result


class TestMCPPopularFonts:
    def test_returns_popular(self) -> None:
        result = popular_fonts(limit=5)
        assert "Top 5" in result
        assert "Roboto" in result

    def test_default_limit(self) -> None:
        result = popular_fonts()
        assert "Top 10" in result
