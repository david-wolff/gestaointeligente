from beanie import Document
from typing import Optional
from bson import ObjectId

class Funcionario(Document):
    nome: str
    cpf: str
    departamento_id: ObjectId
    gestor_id: Optional[ObjectId] = None

    class Settings:
        name = "funcionarios"

    class Config:
        arbitrary_types_allowed = True