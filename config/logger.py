import logging

from config.settings import LOG_LEVEL

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] [%(funcName)s()] - %(message)s",  # noqa: E501
)

logger = logging.getLogger()
