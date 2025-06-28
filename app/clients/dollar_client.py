import httpx
from app.config.config import DOLLAR_URL
from app.models.dollar_model import DollarResponse
from app.entities.dollar import Dollar
from app.entities.quotation import Quotation
from app.utils.logs.service_logger import log_service_call


class DollarClient:
    """
    Cliente responsável por buscar a cotação do dólar em um serviço externo.
    """

    def __init__(self, base_url: str = DOLLAR_URL):
        """
        Cria uma nova instância do DollarClient.

        :param base_url: URL do serviço que fornece a cotação do dólar.
        """
        self.base_url = base_url

    @log_service_call
    async def fetch(self) -> Quotation:
        """
        Faz uma requisição assíncrona ao serviço e retorna a cotação do dólar.

        :return: Cotação do dólar como um objeto Quotation.
        :raises httpx.HTTPStatusError: Se a resposta do serviço for inválida.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url)
            response.raise_for_status()

            data = DollarResponse(**response.json())
            dollar_entity = Dollar(**data.model_dump())

            return dollar_entity.to_quotation()
