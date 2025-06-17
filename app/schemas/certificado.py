from pydantic import BaseModel
from datetime import date

class CertificadoIn(BaseModel):
    curso_id: str
    funcionario_id: str
    url_certificado: str
    data_emissao: date
    completo: bool

class CertificadoOut(CertificadoIn):
    id: str