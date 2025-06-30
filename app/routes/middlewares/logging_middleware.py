import time
import logging
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.logs.logger_factory import LoggerFactory
import traceback

request_logger = LoggerFactory.create_logger("request_logger", "requests.log", logging.INFO)
response_logger = LoggerFactory.create_logger("response_logger", "responses.log", logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        client_host = request.client.host if request.client else "unknown"

        request_logger.info(f"Request from {client_host} - {request.method} {request.url}")

        try:
            response: Response = await call_next(request)
        except Exception as e:
            duration = time.time() - start_time
            raise

        duration = time.time() - start_time
        response_logger.info(f"Response to {client_host} - {request.method} {request.url} - Status: {response.status_code} - Time: {duration:.3f}s")

        return response
