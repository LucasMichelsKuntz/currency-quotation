from app.clients.euro_client import EuroClient
from app.entities.quotation import Quotation
from app.utils.logs.execution_logger import log_execution

class EuroService:
    def __init__(self, client: EuroClient):
        self.client = client

    @log_execution
    async def get_quotation(self) -> Quotation:
        return await self.client.fetch()
