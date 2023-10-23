import pandas as pd
from sqlalchemy import create_engine


class DatabaseConnection:
    """Abstracts a database connection."""

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.engine = None

    def connect(self):
        """Establish a connection."""
        self.engine = create_engine(self.connection_string, fast_executemany=True)

    def disconnect(self):
        """Close the connection."""
        if self.engine:
            self.engine.dispose()
            self.engine = None


class DataInserter:
    """Abstracts the data insertion to a database."""

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def insert(self, df: pd.DataFrame, table_name: str):
        raise NotImplementedError("Subclasses must implement this method.")
