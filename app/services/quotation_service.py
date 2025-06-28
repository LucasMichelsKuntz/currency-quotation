from app.services.dollar_service import DollarService
from app.services.euro_service import EuroService
from app.entities.quotation import Quotation
from app.utils.logs.execution_logger import log_execution
import asyncio
from typing import Optional


class QuotationService:
    """
    Serviço que gerencia a obtenção das cotações e determina a melhor cotação disponível.
    """

    def __init__(self, dollar_service: DollarService, euro_service: EuroService):
        """
        Inicializa o QuotationService com instâncias dos serviços de dólar e euro.

        :param dollar_service: Serviço para obter cotação do dólar.
        :param euro_service: Serviço para obter cotação do euro.
        """
        self.dollar_service = dollar_service
        self.euro_service = euro_service

    @log_execution
    async def get_best_quotation(self) -> Optional[Quotation]:
        """
        Executa as requisições para obter as cotações de dólar e euro concorrentes,
        filtra resultados válidos e retorna a cotação com menor valor.

        :return: A melhor cotação encontrada (menor valor).
        :raises Exception: Se nenhuma cotação válida for obtida.
        """
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
