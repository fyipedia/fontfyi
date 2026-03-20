"""HTTP API client for fontfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install fontfyi[api]``

Usage::

    from fontfyi.api import FontFYI

    with FontFYI() as api:
        items = api.list_blog_categories()
        detail = api.get_blog_category("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class FontFYI:
    """API client for the fontfyi.com REST API.

    Provides typed access to all fontfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://fontfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://fontfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_blog_categories(self, **params: Any) -> dict[str, Any]:
        """List all blog categories."""
        return self._get("/api/v1/blog-categories/", **params)

    def get_blog_category(self, slug: str) -> dict[str, Any]:
        """Get blog category by slug."""
        return self._get(f"/api/v1/blog-categories/" + slug + "/")

    def list_blog_posts(self, **params: Any) -> dict[str, Any]:
        """List all blog posts."""
        return self._get("/api/v1/blog-posts/", **params)

    def get_blog_post(self, slug: str) -> dict[str, Any]:
        """Get blog post by slug."""
        return self._get(f"/api/v1/blog-posts/" + slug + "/")

    def list_blog_series(self, **params: Any) -> dict[str, Any]:
        """List all blog series."""
        return self._get("/api/v1/blog-series/", **params)

    def get_blog_sery(self, slug: str) -> dict[str, Any]:
        """Get blog sery by slug."""
        return self._get(f"/api/v1/blog-series/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_fonts(self, **params: Any) -> dict[str, Any]:
        """List all fonts."""
        return self._get("/api/v1/fonts/", **params)

    def get_font(self, slug: str) -> dict[str, Any]:
        """Get font by slug."""
        return self._get(f"/api/v1/fonts/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_pairings(self, **params: Any) -> dict[str, Any]:
        """List all pairings."""
        return self._get("/api/v1/pairings/", **params)

    def get_pairing(self, slug: str) -> dict[str, Any]:
        """Get pairing by slug."""
        return self._get(f"/api/v1/pairings/" + slug + "/")

    def list_tags(self, **params: Any) -> dict[str, Any]:
        """List all tags."""
        return self._get("/api/v1/tags/", **params)

    def get_tag(self, slug: str) -> dict[str, Any]:
        """Get tag by slug."""
        return self._get(f"/api/v1/tags/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> FontFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
