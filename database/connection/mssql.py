from .base import DatabaseConnection


class MSSQLDatabaseConnection(DatabaseConnection):
    """Concrete implementation for MSSQL database connection."""

    def __init__(
        self, server: str, database: str, username: str, password: str
    ) -> None:
        cnx_string = (
            f"mssql+pyodbc://{username}:{password}@"
            f"{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
        )
        super().__init__(cnx_string)
