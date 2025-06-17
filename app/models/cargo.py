from beanie import Document

class Cargo(Document):
    nome: str
    nivel: int

    class Settings:
        name = "cargos"