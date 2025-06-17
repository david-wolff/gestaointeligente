from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
import traceback

from app.models.departamento import Departamento
from app.schemas.departamento import DepartamentoIn, DepartamentoOut

router = APIRouter(prefix="/departamentos", tags=["Departamentos"])

@router.post("/", response_model=DepartamentoOut)
async def criar_departamento(dados: DepartamentoIn):
    try:
        dep = Departamento(**dados.dict())
        await dep.insert()
        return DepartamentoOut(id=str(dep.id), **dados.dict())
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro ao criar departamento: {repr(e)}")
    
@router.get("/", response_model=List[DepartamentoOut])
async def listar_departamentos():
    deps = await Departamento.find_all().to_list()
    return [DepartamentoOut(id=str(d.id), nome=d.nome) for d in deps]

@router.get("/{id}", response_model=DepartamentoOut)
async def buscar_departamento(id: str):
    departamento = await Departamento.get(ObjectId(id))
    if not departamento:
        raise HTTPException(status_code=404, detail="Departamento não encontrado")
    return DepartamentoOut(id=str(departamento.id), nome=departamento.nome)

@router.delete("/{id}")
async def deletar_departamento(id: str):
    departamento = await Departamento.get(ObjectId(id))
    if not departamento:
        raise HTTPException(status_code=404, detail="Departamento não encontrado")
    await departamento.delete()
    return {"mensagem": "Departamento deletado"}