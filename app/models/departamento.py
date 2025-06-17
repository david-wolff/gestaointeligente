from beanie import Document

class Departamento(Document):
    nome: str

    class Settings:
        name = "departamentos"

    class Config:
        arbitrary_types_allowed = True