"""Tests for fontfyi.cli -- command-line interface."""

from __future__ import annotations

from typer.testing import CliRunner

from fontfyi.cli import app

runner = CliRunner()


class TestCLIInfo:
    def test_info_inter(self) -> None:
        result = runner.invoke(app, ["info", "inter"])
        assert result.exit_code == 0
        assert "Inter" in result.output

    def test_info_roboto(self) -> None:
        result = runner.invoke(app, ["info", "roboto"])
        assert result.exit_code == 0
        assert "Roboto" in result.output

    def test_info_not_found(self) -> None:
        result = runner.invoke(app, ["info", "nonexistent-font"])
        assert result.exit_code == 1


class TestCLISearch:
    def test_search_mono(self) -> None:
        result = runner.invoke(app, ["search", "mono"])
        assert result.exit_code == 0
        # Should find at least one monospace font
        assert len(result.output.strip()) > 0

    def test_search_no_results(self) -> None:
        result = runner.invoke(app, ["search", "zzzznonexistent"])
        assert result.exit_code == 0


class TestCLICSS:
    def test_css_inter(self) -> None:
        result = runner.invoke(app, ["css", "inter"])
        assert result.exit_code == 0
        assert "font-family" in result.output

    def test_css_not_found(self) -> None:
        result = runner.invoke(app, ["css", "nonexistent-font"])
        assert result.exit_code == 1


class TestCLIPair:
    def test_pair_inter(self) -> None:
        result = runner.invoke(app, ["pair", "inter"])
        assert result.exit_code == 0
        # inter has multiple pairings
        assert len(result.output.strip()) > 0

    def test_pair_not_found(self) -> None:
        result = runner.invoke(app, ["pair", "nonexistent-font"])
        assert result.exit_code == 1


class TestCLIPopular:
    def test_popular(self) -> None:
        result = runner.invoke(app, ["popular"])
        assert result.exit_code == 0
        # Should show font names
        assert "Roboto" in result.output


class TestCLIStacks:
    def test_stacks(self) -> None:
        result = runner.invoke(app, ["stacks"])
        assert result.exit_code == 0
        assert "system-ui" in result.output


class TestCLINoArgs:
    def test_no_args_shows_help(self) -> None:
        result = runner.invoke(app, [])
        # Typer no_args_is_help=True returns exit code 0 or 2 depending on version
        assert result.exit_code in (0, 2)
        assert "Usage" in result.output or "fontfyi" in result.output.lower()
