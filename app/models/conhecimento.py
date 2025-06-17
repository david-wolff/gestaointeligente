from beanie import Document

class Conhecimento(Document):
    nome: str

    class Settings:
        name = "conhecimentos"