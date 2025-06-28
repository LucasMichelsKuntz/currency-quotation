from decimal import Decimal
from pydantic import BaseModel, field_validator


class DollarResponse(BaseModel):
    """
    Modelo de resposta para os dados da cotação do dólar.
    """

    currency_price: Decimal
    currency_name: str
    currency_kind: str
    currency_formatter: str

    @field_validator('currency_price', mode='before')
    def normalize_price(cls, v):
        """
        Valida e normaliza o valor da moeda antes de instanciar o modelo.

        - Converte para Decimal.
        - Ajusta o valor caso que vem por padrão como inteiro.

        :param v: Valor recebido para currency_price.
        :return: Valor normalizado como Decimal.
        :raises ValueError: Se o valor não puder ser convertido em Decimal.
        """
        try:
            val = Decimal(v)
        except Exception:
            raise ValueError("Invalid currency_price value")

        val = val / 100

        return val
