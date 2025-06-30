import time
import functools
import inspect
import traceback
from app.utils.logs.logger_factory import LoggerFactory

execution_logger = LoggerFactory.create_logger("execution_logger", "execution.log")

def log_execution(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        stack = traceback.format_stack(limit=5)
        caller = stack[-3].strip() if len(stack) >= 3 else "Unknown caller"

        execution_logger.info(f"Executing {func.__qualname__} called from: {caller}")
        
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        params_str = ", ".join(f"{k}={v!r}" for k, v in bound.arguments.items())
        execution_logger.debug(f"Parameters: {params_str}")

        start = time.time()
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start
            execution_logger.info(f"{func.__qualname__} completed in {duration:.3f}s")
            execution_logger.debug(f"Result: {result!r}")
            return result
        except Exception as e:
            duration = time.time() - start
            execution_logger.error(f"Exception in {func.__qualname__} after {duration:.3f}s: {e}", exc_info=True)
            raise

    return wrapper
