from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId

from app.models.referencia_bibliografica import ReferenciaBibliografica
from app.schemas.referencia_bibliografica import ReferenciaIn, ReferenciaOut

router = APIRouter(prefix="/referencias", tags=["Referências Bibliográficas"])

@router.post("/", response_model=ReferenciaOut)
async def criar_referencia(dados: ReferenciaIn):
    try:
        r = ReferenciaBibliografica(**dados.dict())
        await r.insert()
        return ReferenciaOut(id=str(r.id), **dados.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar referência: {str(e)}")

@router.get("/", response_model=List[ReferenciaOut])
async def listar_referencias():
    docs = await ReferenciaBibliografica.find_all().to_list()
    return [ReferenciaOut(id=str(d.id), autor=d.autor, titulo=d.titulo, ano_publicacao=d.ano_publicacao, isbn=d.isbn) for d in docs]

@router.delete("/{id}")
async def deletar_referencia(id: str):
    doc = await ReferenciaBibliografica.get(ObjectId(id))
    if not doc:
        raise HTTPException(status_code=404, detail="Referência não encontrada")
    await doc.delete()
    return {"mensagem": "Referência deletada"}