"""REST client handling, including PipedriveStream base class."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Iterable

from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

from http import HTTPStatus
from singer_sdk.exceptions import FatalAPIError, RetriableAPIError

from tap_pipedrive.pagination import PipedrivePaginator

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

if TYPE_CHECKING:
    import requests
    from singer_sdk.helpers.types import Context


class PipedriveStream(RESTStream):
    """Pipedrive stream class."""

    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.additional_data.next_cursor"  # noqa: S105
    replication_param = "since"

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://api.pipedrive.com"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="api_token",
            value=self.config.get("api_token", ""),
            location="params",
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")  # noqa: ERA001
        return headers

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        return PipedrivePaginator(jsonpath=self.next_page_token_jsonpath)

    def get_url_params(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}
        params["limit"] = 500  # 100 is default. 500 is max
        if next_page_token:
            params["cursor"] = next_page_token
        if self.replication_key:
            params[self.replication_param] = self.config.get("start_date")
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())


    def validate_response(self, response: requests.Response) -> None:
        if (
                response.status_code in self.extra_retry_statuses
                or response.status_code >= HTTPStatus.INTERNAL_SERVER_ERROR
        ):
            msg = self.response_error_message(response)
            raise RetriableAPIError(msg, response)

        if (
                HTTPStatus.BAD_REQUEST
                <= response.status_code
                < HTTPStatus.INTERNAL_SERVER_ERROR
        ):
            raise Exception(f"HERE: {response.url}")
            msg = self.response_error_message(response)
            raise FatalAPIError(msg)


class PipedriveStreamV1(PipedriveStream):

    next_page_token_jsonpath = "$.additional_data.pagination.next_start"  # noqa: S105

    def get_url_params(
            self,
            context: Context | None,  # noqa: ARG002
            next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}
        params["limit"] = 500  # 100 is default. 500 is max
        if next_page_token:
            params["start"] = next_page_token
        return params
