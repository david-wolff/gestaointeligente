from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class FuncionarioIn(BaseModel):
    nome: str
    cpf: str
    departamento_id: str
    gestor_id: Optional[str] = None

class FuncionarioOut(BaseModel):
    id: str
    nome: str
    cpf: str
    departamento_id: str
    gestor_id: Optional[str] = None