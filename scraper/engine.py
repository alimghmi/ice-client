import pandas as pd
import requests

from config import logger
from utils import Request


class Engine:
    def __init__(self, url, max_retries, backoff_factor) -> None:
        self.url = url
        self.request = Request(max_retries=max_retries, backoff_factor=backoff_factor)

    def fetch(self, content=None) -> pd.DataFrame:
        logger.debug(f"Attempting to fetch content from {self.url}.")
        if not content:
            content = self.get_content()
            logger.debug(
                f"Successfully fetched content from {self.url}. Now parsing the content."
            )
        else:
            logger.debug(
                f"Successfully loaded the content from the user provided argument. Now parsing the content."
            )

        df = self.parse_html(content)
        logger.debug(f"\n{df}")
        self.validate_data(df)
        logger.info(f"Parsed content from {self.url}. Extracted {len(df)} rows.")
        return df

    def get_content(self):
        try:
            r = self.request.request("GET", self.url)
            r.raise_for_status()
            return r.text
        except requests.RequestException as e:
            logger.error(f"Error fetching content from {self.url}. Error: {e}")
            raise ConnectionError(f"Failed to connect to {self.url}.") from e

    def parse_html(self, content: str) -> pd.DataFrame:
        try:
            dfs = pd.read_html(content)
        except Exception as e:
            logger.error(f"Error parsing HTML via pandas. Error: {e}")
            raise e

        if len(dfs):
            logger.debug(
                f"Successfully parsed content from {self.url}. Extracted {len(dfs[0])} rows."  # noqa: E501
            )
            return dfs[0]
        else:
            raise ValueError(f"No data found when parsing content from {self.url}.")

    def validate_data(self, df: pd.DataFrame) -> None:
        if df["Clearing Date"].str.contains("No data found").any() or not len(df):
            logger.error("Data validation failed")
            raise ValueError("No price data provided by the provider as of now.")

        logger.debug("Data validation succeeded.")
