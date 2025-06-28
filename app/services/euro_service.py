from app.clients.euro_client import EuroClient
from app.entities.quotation import Quotation
from app.utils.logs.execution_logger import log_execution


class EuroService:
    """
    Serviço responsável por obter a cotação do euro utilizando o EuroClient.
    """

    def __init__(self, client: EuroClient):
        """
        Inicializa o EuroService com uma instância do EuroClient.

        :param client: Instância do EuroClient para buscar a cotação.
        """
        self.client = client

    @log_execution
    async def get_quotation(self) -> Quotation:
        """
        Obtém a cotação do euro chamando o método fetch do cliente.

        :return: Objeto Quotation com a cotação do euro.
        """
        return await self.client.fetch()
