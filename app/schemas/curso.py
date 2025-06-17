from pydantic import BaseModel
from typing import Literal

class CursoIn(BaseModel):
    nome: str
    emissor: Literal["PUC-RIO", "UFRJ", "IFRJ", "SENAI"]
    tipo: Literal["BACHARELADO", "TECNICO", "CERTIFICACAO", "ESPECIALIZACAO"]

class CursoOut(CursoIn):
    id: str