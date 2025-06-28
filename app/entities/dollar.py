from decimal import Decimal
from pydantic import BaseModel
from app.entities.quotation import Quotation


class Dollar(BaseModel):
    """
    Representa a entidade Dollar com informações sobre a moeda.
    """

    currency_price: Decimal
    currency_name: str
    currency_kind: str
    currency_formatter: str

    def to_quotation(self) -> Quotation:
        """
        Converte os dados do Dollar em um objeto Quotation.

        :return: Quotation com o nome da moeda e o valor convertido para float.
        """
        return Quotation(
            currency=self.currency_name,
            value=float(self.currency_price)
        )
