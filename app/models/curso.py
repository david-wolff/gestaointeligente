from beanie import Document
from typing import Literal

class Curso(Document):
    nome: str
    emissor: Literal["PUC-RIO", "UFRJ", "IFRJ", "SENAI"]
    tipo: Literal["BACHARELADO", "TECNICO", "CERTIFICACAO", "ESPECIALIZACAO"]

    class Settings:
        name = "cursos"

    class Config:
        arbitrary_types_allowed = True