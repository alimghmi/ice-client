from decouple import config

URL = config("URL")
LOG_LEVEL = config("LOG_LEVEL", default="INFO")
