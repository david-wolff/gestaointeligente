from pydantic import BaseModel

class CargoIn(BaseModel):
    nome: str
    nivel: int

class CargoOut(BaseModel):
    id: str
    nome: str
    nivel: int