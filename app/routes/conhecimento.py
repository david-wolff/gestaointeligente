from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId

from app.models.conhecimento import Conhecimento
from app.schemas.conhecimento import ConhecimentoIn, ConhecimentoOut

router = APIRouter(prefix="/conhecimentos", tags=["Conhecimentos"])

@router.post("/", response_model=ConhecimentoOut)
async def criar_conhecimento(dados: ConhecimentoIn):
    try:
        c = Conhecimento(**dados.dict())
        await c.insert()
        return ConhecimentoOut(id=str(c.id), **dados.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar conhecimento: {str(e)}")

@router.get("/", response_model=List[ConhecimentoOut])
async def listar_conhecimentos():
    docs = await Conhecimento.find_all().to_list()
    return [ConhecimentoOut(id=str(c.id), nome=c.nome) for c in docs]

@router.delete("/{id}")
async def deletar_conhecimento(id: str):
    doc = await Conhecimento.get(ObjectId(id))
    if not doc:
        raise HTTPException(status_code=404, detail="Conhecimento não encontrado")
    await doc.delete()
    return {"mensagem": "Conhecimento removido"}