from fastapi import Request
from fastapi.responses import JSONResponse
from app.models.response_model import APIResponse

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=APIResponse(
            status="error",
            message="Erro interno no servidor. Por favor, tente novamente mais tarde.",
            data=None
        ).dict()
    )
