from config import logger
from scraper.engine import Engine


def main():
    logger.info("Initializing Application")
    engine = Engine()
    df = engine.fetch()
    print(df)
    return


if __name__ == "__main__":
    main()
