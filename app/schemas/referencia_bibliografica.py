from pydantic import BaseModel

class ReferenciaIn(BaseModel):
    autor: str
    titulo: str
    ano_publicacao: int
    isbn: str

class ReferenciaOut(ReferenciaIn):
    id: str