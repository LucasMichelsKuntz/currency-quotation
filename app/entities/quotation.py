from datetime import datetime
from pydantic import BaseModel


class Quotation(BaseModel):
    """
    Representa uma cotação de moeda, incluindo o valor e a data da cotação.
    """

    currency: str
    value: float
    date: datetime = datetime.now()

    def __lt__(self, other):
        """
        Permite comparar duas cotações com base no valor.

        :param other: Outro objeto Quotation para comparação.
        :return: True se o valor desta cotação for menor que o valor da outra.
        """
        if not isinstance(other, Quotation):
            return NotImplemented
        return self.value < other.value
