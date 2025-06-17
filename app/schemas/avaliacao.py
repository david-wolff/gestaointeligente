from pydantic import BaseModel
from typing import Literal
from datetime import date

class AvaliacaoIn(BaseModel):
    funcionario_id: str
    tipo: Literal["AVALIACAO_360", "DE_SUPERIOR"]
    nota: float
    comentario: str
    data: date

class AvaliacaoOut(AvaliacaoIn):
    id: str