from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId

from app.models.avaliacao import Avaliacao
from app.schemas.avaliacao import AvaliacaoIn, AvaliacaoOut

router = APIRouter(prefix="/avaliacoes", tags=["Avaliações"])

@router.post("/", response_model=AvaliacaoOut)
async def criar_avaliacao(dados: AvaliacaoIn):
    try:
        a = Avaliacao(
            funcionario_id=ObjectId(dados.funcionario_id),
            tipo=dados.tipo,
            nota=dados.nota,
            comentario=dados.comentario,
            data=dados.data
        )
        await a.insert()
        return AvaliacaoOut(id=str(a.id), **dados.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar avaliação: {str(e)}")

@router.get("/", response_model=List[AvaliacaoOut])
async def listar_avaliacoes():
    docs = await Avaliacao.find_all().to_list()
    return [AvaliacaoOut(
        id=str(d.id),
        funcionario_id=str(d.funcionario_id),
        tipo=d.tipo,
        nota=d.nota,
        comentario=d.comentario,
        data=d.data
    ) for d in docs]

@router.delete("/{id}")
async def deletar_avaliacao(id: str):
    a = await Avaliacao.get(ObjectId(id))
    if not a:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    await a.delete()
    return {"mensagem": "Avaliação removida"}