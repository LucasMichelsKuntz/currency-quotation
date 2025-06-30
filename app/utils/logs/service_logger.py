import time
import functools
import inspect
import traceback
from app.utils.logs.logger_factory import LoggerFactory

service_logger = LoggerFactory.create_logger("service_logger", "service_calls.log")

def log_service_call(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        stack = traceback.format_stack(limit=5)
        caller = stack[-3].strip() if len(stack) >= 3 else "Unknown caller"

        sig = inspect.signature(func)
        bound = sig.bind_partial(*args, **kwargs)
        bound.apply_defaults()
        params_str = ", ".join(f"{k}={v!r}" for k, v in bound.arguments.items())

        service_logger.info(f"Service call {func.__qualname__} called from: {caller} with args: {params_str}")
        
        start = time.time()
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start
            service_logger.info(f"Service call {func.__qualname__} completed in {duration:.3f}s")
            service_logger.debug(f"Result: {result!r}")
            return result
        except Exception as e:
            duration = time.time() - start
            service_logger.error(f"Exception in service call {func.__qualname__} after {duration:.3f}s: {e}", exc_info=True)
            raise

    return wrapper
