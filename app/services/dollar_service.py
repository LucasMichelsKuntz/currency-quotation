from app.clients.dollar_client import DollarClient
from app.entities.quotation import Quotation
from app.utils.logs.execution_logger import log_execution

class DollarService:
    def __init__(self, client: DollarClient):
        self.client = client

    @log_execution
    async def get_quotation(self) -> Quotation:
        return await self.client.fetch()
