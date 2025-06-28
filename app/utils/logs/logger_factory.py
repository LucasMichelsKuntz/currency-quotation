import logging
from pathlib import Path

class LoggerFactory:
    LOG_DIR = Path("logs")
    LOG_DIR.mkdir(exist_ok=True)

    @staticmethod
    def create_logger(name: str, file_name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(LoggerFactory.LOG_DIR / file_name)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )
        handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(handler)
        
        logger.propagate = False
        return logger
