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
