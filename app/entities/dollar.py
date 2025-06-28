from decimal import Decimal
from pydantic import BaseModel
from app.entities.quotation import Quotation

class Dollar(BaseModel):
    currency_price: Decimal
    currency_name: str
    currency_kind: str
    currency_formatter: str

    def to_quotation(self) -> Quotation:
        return Quotation(currency=self.currency_name, value=float(self.currency_price))
