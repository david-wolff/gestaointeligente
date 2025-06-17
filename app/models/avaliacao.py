from beanie import Document
from bson import ObjectId
from datetime import date
from pydantic.config import ConfigDict
from typing import Literal

class Avaliacao(Document):
    funcionario_id: ObjectId
    tipo: Literal["AVALIACAO_360", "DE_SUPERIOR"]
    nota: float
    comentario: str
    data: date

    class Settings:
        name = "avaliacoes"

    model_config = ConfigDict(arbitrary_types_allowed=True)