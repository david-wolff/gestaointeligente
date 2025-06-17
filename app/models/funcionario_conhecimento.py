from beanie import Document
from bson import ObjectId
from typing import Optional
from pydantic.config import ConfigDict

class FuncionarioConhecimento(Document):
    funcionario_id: ObjectId
    conhecimento_id: ObjectId
    referencia_id: Optional[ObjectId] = None

    class Settings:
        name = "funcionario_conhecimentos"

    model_config = ConfigDict(arbitrary_types_allowed=True)