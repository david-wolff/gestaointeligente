from pydantic import BaseModel
from typing import Literal
from datetime import date

class FuncionarioCargoIn(BaseModel):
    funcionario_id: str
    cargo_id: str
    salario: float
    data_inicio: date
    motivo: Literal["PROMOCAO", "REAJUSTE", "OUTRO"]

class FuncionarioCargoOut(FuncionarioCargoIn):
    id: str