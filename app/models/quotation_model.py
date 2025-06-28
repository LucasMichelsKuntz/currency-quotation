from pydantic import BaseModel

class QuotationResult(BaseModel):
    currency: str
    value: float
