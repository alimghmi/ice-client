from config import logger, settings
from scraper import Engine
from transformer import Agent
from utils import create_inserter_objects


def main():
    logger.info("Initializing Application")
    engine = Engine()
    df = engine.fetch()
    df_transformed = Agent(df).transform()
    inserter = create_inserter_objects()
    result = inserter.insert(df_transformed, settings.OUTPUT_TABLE)
    print(result)
    return


if __name__ == "__main__":
    main()
