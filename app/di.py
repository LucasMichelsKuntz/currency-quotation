from fastapi import Depends
from app.container import injector
from app.services.quotation_service import QuotationService

def quotation_service_dep() -> QuotationService:
    return injector.get(QuotationService)
