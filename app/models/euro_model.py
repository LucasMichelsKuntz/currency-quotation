from pydantic import BaseModel

class EuroCotacao(BaseModel):
    moeda: str
    sigla: str
    valor_comercial: float

class EuroResponse(BaseModel):
    cotacao: EuroCotacao
