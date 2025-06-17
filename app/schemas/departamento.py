from pydantic import BaseModel

class DepartamentoIn(BaseModel):
    nome: str

class DepartamentoOut(DepartamentoIn):
    id: str