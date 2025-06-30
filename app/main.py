from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.routes.quotation import router as quotation_router
from app.routes.middlewares.logging_middleware import LoggingMiddleware

from app.handlers.generic_handler import generic_exception_handler

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.include_router(quotation_router, prefix='/api/v1')

app.add_exception_handler(Exception, generic_exception_handler)
