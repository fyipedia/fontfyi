"""Tests for fontfyi.api -- HTTP client for fontfyi.com."""

from __future__ import annotations

from fontfyi.api import FontFYI


class TestFontFYIClient:
    """Verify the client initializes and has all expected methods."""

    def test_init_default(self) -> None:
        client = FontFYI()
        assert str(client._client.base_url) == "https://fontfyi.com/api/"
        client.close()

    def test_init_custom_url(self) -> None:
        client = FontFYI(base_url="http://localhost:8000/api", timeout=5.0)
        assert "localhost" in str(client._client.base_url)
        client.close()

    def test_context_manager(self) -> None:
        with FontFYI() as client:
            assert client is not None

    def test_has_all_methods(self) -> None:
        client = FontFYI()
        methods = [
            "font",
            "css",
            "fonts",
            "search",
            "pairings",
            "tags",
            "stacks",
            "random",
        ]
        for method in methods:
            assert hasattr(client, method), f"Missing method: {method}"
            assert callable(getattr(client, method))
        client.close()
