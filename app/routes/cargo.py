from fastapi import APIRouter, HTTPException
from typing import List
from app.models.cargo import Cargo
from app.schemas.cargo import CargoIn, CargoOut
from bson import ObjectId

router = APIRouter(prefix="/cargos", tags=["Cargos"])

@router.post("/", response_model=CargoOut)
async def criar_cargo(dados: CargoIn):
    cargo = Cargo(**dados.dict())
    await cargo.insert()
    return CargoOut(id=str(cargo.id), nome=cargo.nome, nivel=cargo.nivel)

@router.get("/", response_model=List[CargoOut])
async def listar_cargos():
    cargos = await Cargo.find_all().to_list()
    return [CargoOut(id=str(c.id), nome=c.nome, nivel=c.nivel) for c in cargos]

@router.get("/{id}", response_model=CargoOut)
async def obter_cargo(id: str):
    cargo = await Cargo.get(ObjectId(id))
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo não encontrado")
    return CargoOut(id=str(cargo.id), nome=cargo.nome, nivel=cargo.nivel)

@router.delete("/{id}")
async def deletar_cargo(id: str):
    cargo = await Cargo.get(ObjectId(id))
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo não encontrado")
    await cargo.delete()
    return {"mensagem": "Cargo deletado"}