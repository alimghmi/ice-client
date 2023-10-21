import datetime

import pandas as pd

from config import logger


class Agent:
    COLUMNS_NAME = {
        "Clearing Date": "clearing_date",
        "Name": "name",
        "Instrument Name": "instrument_name",
        "EOD Price": "price",
    }

    def __init__(self, df: pd.DataFrame) -> None:
        self.dataframe = df

    def transform(self) -> pd.DataFrame:
        logger.info("Starting data transformation.")
        try:
            self.parse_date()
            logger.debug("Parsed dates successfully.")
            self.add_timestamp()
            logger.debug("Added timestamps successfully.")
            self.rename_columns()
            logger.debug("Renamed columns successfully.")
        except Exception as e:
            logger.error(f"Data transformation failed. Error: {e}")
            raise

        logger.info("Data transformation completed successfully.")
        logger.debug(f"\n{self.dataframe}")
        return self.dataframe

    def parse_date(self):
        try:
            self.dataframe["Clearing Date"] = pd.to_datetime(
                self.dataframe["Clearing Date"], format="%Y-%m-%d"
            )
        except Exception as e:
            logger.error(f"Failed to parse dates. Error: {e}")
            raise

    def add_timestamp(self):
        try:
            self.dataframe["timestamp_created_utc"] = datetime.datetime.utcnow()
        except Exception as e:
            logger.error(f"Failed to add timestamps. Error: {e}")
            raise

    def rename_columns(self):
        try:
            self.dataframe.rename(columns=self.COLUMNS_NAME, inplace=True)
        except Exception as e:
            logger.error(f"Failed to rename columns. Error: {e}")
            raise
