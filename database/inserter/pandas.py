import time

import pandas as pd
from sqlalchemy import exc

from config import logger

from ..connection.base import DatabaseConnection
from .base import DataInserter


class PandasSQLDataInserter(DataInserter):
    """Concrete implementation of data insertion using Pandas to_sql."""

    def __init__(self, db_connection: DatabaseConnection, max_retries: int = 3) -> None:
        super().__init__(db_connection)
        self.max_retries = max_retries

    def insert(self, df: pd.DataFrame, table_name: str) -> None:
        self.delete_rows(table_name=table_name)
        schema, name = table_name.split(".")
        if self.db_connection.engine is None:
            self.db_connection.connect()

        for i in range(self.max_retries):
            try:
                df.to_sql(
                    schema=schema,
                    name=name,
                    con=self.db_connection.engine,
                    if_exists="append",
                    index=False,
                )
                logger.info(f"Inserted {len(df)} rows into {table_name} table")
                return
            except exc.SQLAlchemyError as e:
                logger.error(
                    f"Failed to insert data. Attempt {i + 1} of {self.max_retries}. Error: {e}"  # noqa: E501
                )
                if (i + 1) == self.max_retries:
                    raise

                time.sleep(i + 1)

    def delete_rows(self, table_name: str) -> None:
        if self.db_connection.engine is None:
            self.db_connection.connect()

        connection = self.db_connection.engine.raw_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(f"DELETE FROM {table_name}")
            connection.commit()
            logger.info(f"Deleted rows from {table_name} successfully.")
        except Exception as e:
            logger.error(f"Failed to delete rows from {table_name}. Error: {e}")
            connection.rollback()
        finally:
            connection.close()
            cursor.close()
