import os, logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger("week6")
    logger.setLevel(logging.INFO)

    log_to_file = os.getenv("LOG_TO_FILE","true").lower() == "true"
    if log_to_file:
        os.makedirs(os.path.dirname(os.getenv("LOG_FILE","logs/app.log")), exist_ok=True)
        handler = RotatingFileHandler(os.getenv("LOG_FILE","logs/app.log"), maxBytes=2_000_000, backupCount=3)
        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        logger.addHandler(handler)
    else:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        logger.addHandler(handler)

    return logger
