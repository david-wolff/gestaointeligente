from beanie import Document
from pydantic.config import ConfigDict

class ReferenciaBibliografica(Document):
    autor: str
    titulo: str
    ano_publicacao: int
    isbn: str

    class Settings:
        name = "referencias_bibliograficas"

    model_config = ConfigDict(arbitrary_types_allowed=True)