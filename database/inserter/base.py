import pandas as pd

from ..connection.base import DatabaseConnection


class DataInserter:
    """Abstracts the data insertion to a database."""

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def insert(self, df: pd.DataFrame, table_name: str):
        raise NotImplementedError("Subclasses must implement this method.")
