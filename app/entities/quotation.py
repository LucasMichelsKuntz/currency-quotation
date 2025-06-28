from datetime import datetime
from pydantic import BaseModel

class Quotation(BaseModel):
    currency: str
    value: float
    date: datetime = datetime.now()
    
    def __lt__(self, other):
        if not isinstance(other, Quotation):
            return NotImplemented
        return self.value < other.value
