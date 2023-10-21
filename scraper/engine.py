import pandas as pd
import requests

from config import logger, settings


class Engine:
    URL = settings.URL

    def fetch(self) -> pd.DataFrame:
        logger.debug(f"Attempting to fetch content from {self.URL}.")
        content = self.get_content()
        logger.debug(f"Successfully fetched content from {self.URL}. Now parsing the content.")
        df = self.parse_html(content)
        logger.info(f"Parsed content from {self.URL}. Extracted {len(df)} rows.")
        return df

    def get_content(self):
        try:
            r = requests.get(self.URL)
            r.raise_for_status()
            return r.text
        except requests.RequestException as e:
            logger.error(f"Error fetching content from {self.URL}. Error: {e}")
            raise ConnectionError(f"Failed to connect to {self.URL}.") from e

    def parse_html(self, content: str) -> pd.DataFrame:
        try:
            dfs = pd.read_html(content)
        except Exception as e:
            logger.error(e)
            raise e
        
        if len(dfs):
            logger.debug(f"Successfully parsed content from {self.URL}. Extracted {len(dfs[0])} rows.")
            return dfs[0]
        else:
            raise ValueError(f"No data found when parsing content from {self.URL}.")
