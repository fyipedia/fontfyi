"""HTTP API client for fontfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install fontfyi[api]``

Usage::

    from fontfyi.api import FontFYI

    with FontFYI() as api:
        info = api.font("inter")
        print(info["family"])  # "Inter"

        results = api.search("mono")
        print(results)
"""

from __future__ import annotations

from typing import Any

import httpx


class FontFYI:
    """API client for the fontfyi.com REST API.

    Args:
        base_url: API base URL. Defaults to ``https://fontfyi.com/api``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://fontfyi.com/api",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    # -- HTTP helpers ----------------------------------------------------------

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -------------------------------------------------------------

    def font(self, slug: str) -> dict[str, Any]:
        """Get font metadata by slug.

        Args:
            slug: Font slug (e.g. ``"inter"``).

        Returns:
            Dict with family, category, variants, subsets, designer, etc.
        """
        return self._get(f"/font/{slug}/")

    def css(self, slug: str) -> dict[str, Any]:
        """Get CSS import snippet for a font.

        Args:
            slug: Font slug (e.g. ``"inter"``).

        Returns:
            Dict with CSS import URL, font-family declaration, etc.
        """
        return self._get(f"/font/{slug}/css/")

    def fonts(self, **filters: Any) -> dict[str, Any]:
        """Browse all fonts with optional filters.

        Args:
            **filters: Optional query params (category, tag, page).

        Returns:
            Dict with fonts list and pagination info.
        """
        return self._get("/fonts/", **filters)

    def search(self, query: str) -> dict[str, Any]:
        """Search fonts by name.

        Args:
            query: Search term (e.g. ``"mono"``, ``"sans"``).
        """
        return self._get("/search/", q=query)

    def pairings(self, slug: str) -> dict[str, Any]:
        """Get font pairing recommendations.

        Args:
            slug: Font slug (e.g. ``"inter"``).

        Returns:
            Dict with pairing suggestions including heading/body combos.
        """
        return self._get(f"/pairings/{slug}/")

    def tags(self) -> dict[str, Any]:
        """Get all available font tags."""
        return self._get("/tags/")

    def stacks(self) -> dict[str, Any]:
        """Get all CSS font stack presets."""
        return self._get("/font-stacks/")

    def random(self) -> dict[str, Any]:
        """Get a random font."""
        return self._get("/random/")

    # -- Context manager -------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP connection."""
        self._client.close()

    def __enter__(self) -> FontFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
