from config import settings
from database import MSSQLDatabaseConnection, PandasSQLDataInserter


def create_inserter_objects(*args, **kwargs) -> PandasSQLDataInserter:
    db_connection = MSSQLDatabaseConnection(*args, **kwargs)
    data_inserter = PandasSQLDataInserter(
        db_connection, max_retries=settings.INSERTER_MAX_RETRIES
    )

    return data_inserter
