from config import settings
from database.mssql import MSSQLDatabaseConnection, PandasSQLDataInserter


def create_inserter_objects() -> PandasSQLDataInserter:
    db_connection = MSSQLDatabaseConnection(
        settings.MSSQL_SERVER,
        settings.MSSQL_DATABASE,
        settings.MSSQL_USERNAME,
        settings.MSSQL_PASSWORD,
    )

    data_inserter = PandasSQLDataInserter(
        db_connection, max_retries=settings.INSERTER_MAX_RETRIES
    )

    return data_inserter
