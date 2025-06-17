from pydantic import BaseModel

class ConhecimentoIn(BaseModel):
    nome: str

class ConhecimentoOut(ConhecimentoIn):
    id: str