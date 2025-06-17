from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId

from app.models.funcionario_conhecimento import FuncionarioConhecimento
from app.schemas.funcionario_conhecimento import FuncionarioConhecimentoIn, FuncionarioConhecimentoOut

router = APIRouter(prefix="/funcionario-conhecimentos", tags=["FuncionarioConhecimento"])

@router.post("/", response_model=FuncionarioConhecimentoOut)
async def vincular_conhecimento(dados: FuncionarioConhecimentoIn):
    try:
        doc = FuncionarioConhecimento(
            funcionario_id=ObjectId(dados.funcionario_id),
            conhecimento_id=ObjectId(dados.conhecimento_id),
            referencia_id=ObjectId(dados.referencia_id) if dados.referencia_id else None
        )
        await doc.insert()
        return FuncionarioConhecimentoOut(
            id=str(doc.id),
            funcionario_id=dados.funcionario_id,
            conhecimento_id=dados.conhecimento_id,
            referencia_id=dados.referencia_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao vincular: {str(e)}")
@router.get("/", response_model=List[FuncionarioConhecimentoOut])
async def listar_vinculos():
    docs = await FuncionarioConhecimento.find_all().to_list()
    return [
        FuncionarioConhecimentoOut(
            id=str(d.id),
            funcionario_id=str(d.funcionario_id),
            conhecimento_id=str(d.conhecimento_id)
        ) for d in docs
    ]