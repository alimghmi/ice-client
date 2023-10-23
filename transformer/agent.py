import datetime

import pandas as pd

from config import logger


class Agent:
    COLUMNS_NAME = {
        "Clearing Date": "clearing_date",
        "Name": "name",
        "Instrument Name": "instrument_name",
        "Ticker": "ticker",
        "Tier": "tier",
        "Currency": "currency",
        "Doc Clause": "doc_clause",
        "Fixed Rate": "fixed_rate",
        "Maturity Date": "maturity_date",
        "EOD Price": "price"
    }

    def __init__(self, df: pd.DataFrame) -> None:
        self.dataframe = df

    def transform(self) -> pd.DataFrame:
        logger.info("Starting data transformation.")
        try:
            self.brakedown_instrument_name()
            logger.debug("Broke down instrument successfully.")
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
            self.dataframe["Maturity Date"] = pd.to_datetime(
                self.dataframe["Maturity Date"], format="%Y-%m-%d"
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
        
    def brakedown_instrument_name(self):
        try:
            df_split = self.dataframe['Instrument Name'].str.split('.', n=5, expand=True)
            print(df_split)
            df_split.columns = ['Ticker', 'Tier', 'Currency', 'Doc Clause', 'Fixed Rate', 'Maturity Date']
            self.dataframe = pd.concat([self.dataframe, df_split], axis=1)
        except Exception as e:
            logger.error(f"Failed to brake down instrument name. Error: {e}")
            raise
