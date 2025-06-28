from app.services.dollar_service import DollarService
from app.services.euro_service import EuroService
from app.entities.quotation import Quotation
from app.utils.logs.execution_logger import log_execution
import asyncio
from typing import Optional

class QuotationService:
    def __init__(self, dollar_service: DollarService, euro_service: EuroService):
        self.dollar_service = dollar_service
        self.euro_service = euro_service

    @log_execution
    async def get_best_quotation(self) -> Optional[Quotation]:
        dollar_task = asyncio.create_task(self.dollar_service.get_quotation())
        euro_task = asyncio.create_task(self.euro_service.get_quotation())

        results = await asyncio.gather(dollar_task, euro_task, return_exceptions=True)

        quotations = []
        for res in results:
            if isinstance(res, Exception):
                continue
            if res is not None:
                quotations.append(res)

        if not quotations:
            raise Exception("No valid quotation retrieved.")

        best = min(quotations, key=lambda q: q.value)
        return best
