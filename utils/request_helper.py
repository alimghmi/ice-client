import time

import requests

from config import logger


class Request:
    def __init__(self, max_retries: int, backoff_factor: int) -> None:
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def request(self, method: str, url: str, *args, **kwargs) -> requests.Request:
        for i in range(self.max_retries):
            try:
                return requests.request(method=method, url=url, *args, **kwargs)
            except requests.exceptions.RequestException as e:
                logger.error(
                    f"{method.upper()} request failed. Attempt {i + 1} of {self.max_retries}. Error: {e}"  # noqa: E501
                )
                if (i + 1) == self.max_retries:
                    raise

                time.sleep(i**self.backoff_factor)
