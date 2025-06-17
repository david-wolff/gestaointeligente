from beanie import Document
from bson import ObjectId
from datetime import date

class Certificado(Document):
    curso_id: ObjectId
    funcionario_id: ObjectId
    url_certificado: str
    data_emissao: date
    completo: bool

    class Settings:
        name = "certificados"

    class Config:
        arbitrary_types_allowed = True