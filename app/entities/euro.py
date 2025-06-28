from decimal import Decimal
from pydantic import BaseModel
from app.entities.quotation import Quotation


class Euro(BaseModel):
    """
    Representa a entidade Euro com informações sobre a cotação da moeda.
    """

    valor_comercial: Decimal
    sigla: str
    moeda: str

    def to_quotation(self) -> Quotation:
        """
        Converte os dados do Euro em um objeto Quotation.

        :return: Quotation com o nome da moeda e o valor comercial.
        """
        return Quotation(
            currency=self.moeda,
            value=self.valor_comercial
        )
