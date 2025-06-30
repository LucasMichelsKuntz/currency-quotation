from fastapi import APIRouter, Depends
from app.di import quotation_service_dep
from app.models.response_model import APIResponse
from app.services.quotation_service import QuotationService
from app.utils.logs.execution_logger import log_execution

router = APIRouter()

@router.get(
    "/quotation/best",
    summary="Obter a melhor cotação",
    description="Retorna a melhor cotação de moeda disponível pelo serviço de cotações.",
    responses={
        200: {
            "description": "Cotação obtida com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "message": "Cotação obtida com sucesso",
                        "data": {
                            "currency": "dollar",
                            "value": 5.12,
                            "date": "2025-06-28T19:24:40.357815"                        
                        }
                    }
                }
            }
        }
    }
)
@log_execution
async def best_quotation(
    service: QuotationService = Depends(quotation_service_dep)
):
    result = await service.get_best_quotation()
    return APIResponse(
        status="success",
        message="Cotação obtida com sucesso",
        data=result
    )
