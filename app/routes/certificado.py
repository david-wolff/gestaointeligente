from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId

from app.models.certificado import Certificado
from app.schemas.certificado import CertificadoIn, CertificadoOut

router = APIRouter(prefix="/certificados", tags=["Certificados"])

@router.post("/", response_model=CertificadoOut)
async def criar_certificado(dados: CertificadoIn):
    try:
        cert = Certificado(
            curso_id=ObjectId(dados.curso_id),
            funcionario_id=ObjectId(dados.funcionario_id),
            url_certificado=dados.url_certificado,
            data_emissao=dados.data_emissao,
            completo=dados.completo
        )
        await cert.insert()
        return CertificadoOut(id=str(cert.id), **dados.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar certificado: {str(e)}")

@router.get("/", response_model=List[CertificadoOut])
async def listar_certificados():
    certs = await Certificado.find_all().to_list()
    return [
        CertificadoOut(
            id=str(c.id),
            curso_id=str(c.curso_id),
            funcionario_id=str(c.funcionario_id),
            url_certificado=c.url_certificado,
            data_emissao=c.data_emissao,
            completo=c.completo
        ) for c in certs
    ]

@router.delete("/{id}")
async def deletar_certificado(id: str):
    cert = await Certificado.get(ObjectId(id))
    if not cert:
        raise HTTPException(status_code=404, detail="Certificado não encontrado")
    await cert.delete()
    return {"mensagem": "Certificado removido"}