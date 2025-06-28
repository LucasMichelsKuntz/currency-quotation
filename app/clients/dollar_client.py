import httpx
from app.config.config import DOLLAR_URL
from app.models.dollar_model import DollarResponse
from app.entities.dollar import Dollar
from app.entities.quotation import Quotation
from app.utils.logs.service_logger import log_service_call

class DollarClient:
    def __init__(self, base_url: str = DOLLAR_URL):
        self.base_url = base_url

    @log_service_call
    async def fetch(self) -> Quotation:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url)
            response.raise_for_status()
            data = DollarResponse(**response.json())
            dollar_entity = Dollar(**data.model_dump())
            return dollar_entity.to_quotation()
