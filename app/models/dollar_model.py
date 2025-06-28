from decimal import Decimal
from pydantic import BaseModel, field_validator

class DollarResponse(BaseModel):
    currency_price: Decimal
    currency_name: str
    currency_kind: str
    currency_formatter: str

    @field_validator('currency_price', mode='before')
    def normalize_price(cls, v):
        try:
            val = Decimal(v)
        except Exception:
            raise ValueError("Invalid currency_price value")
        
        if val > 100:
            val = val / 100
        
        return val
