from injector import Injector, Module, provider, singleton

from app.clients.dollar_client import DollarClient
from app.clients.euro_client import EuroClient
from app.services.dollar_service import DollarService
from app.services.euro_service import EuroService
from app.services.quotation_service import QuotationService

class AppModule(Module):

    @singleton
    @provider
    def provide_dollar_client(self) -> DollarClient:
        return DollarClient()

    @singleton
    @provider
    def provide_euro_client(self) -> EuroClient:
        return EuroClient()

    @singleton
    @provider
    def provide_dollar_service(self, client: DollarClient) -> DollarService:
        return DollarService(client)

    @singleton
    @provider
    def provide_euro_service(self, client: EuroClient) -> EuroService:
        return EuroService(client)

    @singleton
    @provider
    def provide_quotation_service(
        self,
        dollar_service: DollarService,
        euro_service: EuroService
    ) -> QuotationService:
        return QuotationService(dollar_service, euro_service)

injector = Injector([AppModule()])
