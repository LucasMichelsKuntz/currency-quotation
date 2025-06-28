import time
import functools
from inspect import signature
from app.utils.logs.logger_factory import LoggerFactory

service_logger = LoggerFactory.create_logger("service_logger", "service_calls.log")

def log_service_call(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        bound = signature(func).bind_partial(*args, **kwargs)
        bound.apply_defaults()
        service_logger.info(f"Service call {func.__name__} with args: {bound.arguments}")
        start = time.time()
        result = await func(*args, **kwargs)
        duration = time.time() - start
        service_logger.info(f"Service call {func.__name__} completed in {duration:.3f}s with result: {result}")
        return result
    return wrapper
