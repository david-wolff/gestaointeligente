from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
from app.models.funcionario_cargo import FuncionarioCargo
from app.schemas.funcionario_cargo import FuncionarioCargoIn, FuncionarioCargoOut

router = APIRouter(prefix="/funcionarios-cargos", tags=["FuncionárioCargo"])

@router.post("/", response_model=FuncionarioCargoOut)
async def criar_funcionario_cargo(dados: FuncionarioCargoIn):
    try:
        fc = FuncionarioCargo(
            funcionario_id=ObjectId(dados.funcionario_id),
            cargo_id=ObjectId(dados.cargo_id),
            salario=dados.salario,
            data_inicio=dados.data_inicio,
            motivo=dados.motivo
        )
        await fc.insert()
        return FuncionarioCargoOut(id=str(fc.id), **dados.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar vínculo: {str(e)}")

@router.get("/", response_model=List[FuncionarioCargoOut])
async def listar_funcionarios_cargos():
    docs = await FuncionarioCargo.find_all().to_list()
    return [
        FuncionarioCargoOut(
            id=str(d.id),
            funcionario_id=str(d.funcionario_id),
            cargo_id=str(d.cargo_id),
            salario=d.salario,
            data_inicio=d.data_inicio,
            motivo=d.motivo
        ) for d in docs
    ]

@router.delete("/{id}")
async def deletar_vinculo(id: str):
    doc = await FuncionarioCargo.get(ObjectId(id))
    if not doc:
        raise HTTPException(status_code=404, detail="Vínculo não encontrado")
    await doc.delete()
    return {"mensagem": "Vínculo removido"}