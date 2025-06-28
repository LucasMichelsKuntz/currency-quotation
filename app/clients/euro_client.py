import httpx
from app.config.config import EURO_URL
from app.models.euro_model import EuroResponse
from app.entities.euro import Euro
from app.entities.quotation import Quotation
from app.utils.logs.service_logger import log_service_call


class EuroClient:
    """
    Cliente que busca a cotação do euro em um serviço externo.
    """

    def __init__(self, base_url: str = EURO_URL):
        """
        Inicializa o EuroClient com a URL base do serviço.

        :param base_url: URL do serviço de cotação do euro.
        """
        self.base_url = base_url

    @log_service_call
    async def fetch(self) -> Quotation:
        """
        Realiza a requisição ao serviço e retorna a cotação como Quotation.

        :return: Cotação do euro como um objeto Quotation.
        :raises httpx.HTTPStatusError: Caso a resposta do serviço seja inválida.
        """
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(self.base_url)
            response.raise_for_status()
            data = EuroResponse(**response.json())
            euro_entity = Euro(**data.cotacao.model_dump())
            return euro_entity.to_quotation()
