import time
import functools
from app.utils.logs.logger_factory import LoggerFactory

execution_logger = LoggerFactory.create_logger("execution_logger", "execution.log")

def log_execution(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        execution_logger.info(f"Executing {func.__name__}")
        start = time.time()
        result = await func(*args, **kwargs)
        duration = time.time() - start
        execution_logger.info(f"{func.__name__} completed in {duration:.3f}s")
        return result
    return wrapper
