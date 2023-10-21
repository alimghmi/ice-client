from config import logger, settings
from scraper import Engine
from transformer import Agent
from utils import create_inserter_objects


def main():
    logger.info("Initializing Scraper Engine")
    engine = Engine()
    df = engine.fetch()
    logger.info("Transforming Data")
    df_transformed = Agent(df).transform()
    logger.info("Preparing Database Inserter")
    inserter = create_inserter_objects()
    logger.info(f"Inserting Data into {settings.OUTPUT_TABLE}")
    inserter.insert(df_transformed, settings.OUTPUT_TABLE)
    logger.info("Application completed successfully")
    return


if __name__ == "__main__":
    main()
