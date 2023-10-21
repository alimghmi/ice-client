import time
import pandas as pd
from sqlalchemy import exc

from config import logger

from .base import DatabaseConnection, DataInserter


class MSSQLDatabaseConnection(DatabaseConnection):
    """Concrete implementation for MSSQL database connection."""

    def __init__(self, server, database, username, password):
        cnx_string = (
            f"mssql+pyodbc://{username}:{password}@"
            f"{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
        )
        super().__init__(cnx_string)


class PandasSQLDataInserter(DataInserter):
    """Concrete implementation of data insertion using Pandas to_sql."""

    def __init__(self, db_connection: DatabaseConnection, max_retries=3):
        super().__init__(db_connection)
        self.max_retries = max_retries

    def insert(self, df: pd.DataFrame, table_name: str):
        schema, name = table_name.split(".")
        if self.db_connection.engine is None:
            self.db_connection.connect()

        for i in range(self.max_retries):
            try:
                result = df.to_sql(
                    schema=schema,
                    name=name,
                    con=self.db_connection.engine,
                    if_exists="replace",
                    index=False,
                )
                logger.info(f"Inserted {len(df)} rows into {table_name} table")
                return result
            except exc.SQLAlchemyError as e:
                logger.error(
                    f"Failed to insert data. Attempt {i + 1} of {self.max_retries}. Error: {e}"  # noqa: E501
                )
                time.sleep(i + 1)

        logger.error("Max retries reached. Data insertion failed.")
        raise exc.SQLAlchemyError("Data insertion failed.")
