"""Interacting with S&S' API."""

from typing import Any, Self

from httpx import Client

from .models import Product


class SandSServices:
    """A class wrapping S&S' API."""

    def __init__(
        self: Self,
        base_url: str,
        account_number: str,
        token: str,
    ) -> None:
        self.client = Client(auth=(account_number, token))
        self.base_url = base_url

    def make_request(  # noqa: PLR0913
        self: Self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> dict:
        """Make a request to S&S' API."""
        args = {
            "method": method,
            "url": self.base_url + path,
        }

        if params is not None:
            args["params"] = params

        if json is not None:
            args["json"] = json

        if timeout is not None:
            args["timeout"] = timeout

        response = self.client.request(**args)
        return response.json()

    def get_products(
        self: Self,
    ) -> list[Product]:
        """Get all products."""
        product_data = self.make_request("GET", "/products", timeout=500)
        return [Product.from_api_data(data) for data in product_data]
