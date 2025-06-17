from beanie import Document
from bson import ObjectId
from typing import Literal
from datetime import date

class FuncionarioCargo(Document):
    funcionario_id: ObjectId
    cargo_id: ObjectId
    salario: float
    data_inicio: date
    motivo: Literal["PROMOCAO", "REAJUSTE", "OUTRO"]

    class Settings:
        name = "funcionarios_cargos"

    class Config:
        arbitrary_types_allowed = True