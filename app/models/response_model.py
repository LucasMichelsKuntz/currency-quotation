from typing import Generic, Optional, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class APIResponse(GenericModel, Generic[T]):
    """
    Modelo genérico para resposta de API.

    :param status: Status da resposta (ex: "success", "error").
    :param message: Mensagem adicional opcional.
    :param data: Dados opcionais da resposta, do tipo genérico T.
    """

    status: str
    message: Optional[str] = None
    data: Optional[T]
