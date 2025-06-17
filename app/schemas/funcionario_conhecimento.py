from pydantic import BaseModel
from typing import Optional

class FuncionarioConhecimentoIn(BaseModel):
    funcionario_id: str
    conhecimento_id: str
    referencia_id: Optional[str] = None

class FuncionarioConhecimentoOut(FuncionarioConhecimentoIn):
    id: str