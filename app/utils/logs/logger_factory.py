import logging
from pathlib import Path

class LoggerFactory:
    LOG_DIR = Path("logs")
    LOG_DIR.mkdir(exist_ok=True)

    @staticmethod
    def create_logger(name: str, file_name: str, level=logging.INFO) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(level)

        if not any(isinstance(h, logging.FileHandler) and h.baseFilename == str(LoggerFactory.LOG_DIR / file_name) for h in logger.handlers):
            handler = logging.FileHandler(LoggerFactory.LOG_DIR / file_name)
            handler.setLevel(level)
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        logger.propagate = False
        return logger
