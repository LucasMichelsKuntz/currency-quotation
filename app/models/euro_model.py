from pydantic import BaseModel


class EuroCotacao(BaseModel):
    """
    Representa a cotação do euro com detalhes da moeda.
    """

    moeda: str
    sigla: str
    valor_comercial: float


class EuroResponse(BaseModel):
    """
    Modelo de resposta que contém a cotação do euro.
    """

    cotacao: EuroCotacao
