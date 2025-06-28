from pydantic import BaseModel


class QuotationResult(BaseModel):
    """
    Representa o resultado de uma cotação com a moeda e seu valor.
    """

    currency: str
    value: float
