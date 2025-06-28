from app.clients.dollar_client import DollarClient
from app.entities.quotation import Quotation
from app.utils.logs.execution_logger import log_execution


class DollarService:
    """
    Serviço responsável por obter a cotação do dólar utilizando o DollarClient.
    """

    def __init__(self, client: DollarClient):
        """
        Inicializa o DollarService com uma instância do DollarClient.

        :param client: Instância do DollarClient para buscar a cotação.
        """
        self.client = client

    @log_execution
    async def get_quotation(self) -> Quotation:
        """
        Obtém a cotação do dólar chamando o método fetch do cliente.

        :return: Objeto Quotation com a cotação do dólar.
        """
        return await self.client.fetch()
