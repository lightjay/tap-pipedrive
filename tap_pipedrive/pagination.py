import logging

from requests import Response
from singer_sdk.pagination import JSONPathPaginator


class PipedrivePaginator(JSONPathPaginator):

    def advance(self, response: Response) -> None:
        """Get a new page value and advance the current one.

        Args:
            response: API response object.

        Raises:
            RuntimeError: If a loop in pagination is detected. That is, when two
                consecutive pagination tokens are identical.
        """
        self._page_count += 1

        if not self.has_more(response):
            self._finished = True
            return

        new_value = self.get_next(response)

        # if new_value and new_value == self._value:
        #     msg = (
        #         f"Loop detected in pagination. Pagination token {new_value} is "
        #         "identical to prior token."
        #     )
        #     self._finished = True
        #     raise RuntimeError(msg)

        # Stop if new value None, empty string, 0, etc.
        if not new_value or (new_value and new_value == self._value):
            self._finished = True
        else:
            self._value = new_value
