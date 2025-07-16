from loguru import logger
import sys
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger.remove()

logger.add(sys.stdout, colorize=True, level="INFO",
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>")
logger.add(os.path.join(LOG_DIR, "app.log"), level="INFO", rotation="500 KB", retention="5 days", compression="zip")

def get_logger():
    return logger
