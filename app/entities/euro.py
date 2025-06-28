from decimal import Decimal
from pydantic import BaseModel
from app.entities.quotation import Quotation

class Euro(BaseModel):
    valor_comercial: Decimal
    sigla: str
    moeda: str

    def to_quotation(self) -> Quotation:
        return Quotation(currency=self.moeda, value=self.valor_comercial)
