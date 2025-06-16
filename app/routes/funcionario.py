from fastapi import APIRouter, HTTPException
from app.models.funcionario import Funcionario
from app.schemas.funcionario import FuncionarioIn, FuncionarioOut
from typing import List
from bson import ObjectId

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])

@router.post("/", response_model=FuncionarioOut)
async def criar_funcionario(dados: FuncionarioIn):
    funcionario = Funcionario(
        nome=dados.nome,
        cpf=dados.cpf,
        departamento_id=ObjectId(dados.departamento_id),
        gestor_id=ObjectId(dados.gestor_id) if dados.gestor_id else None
    )
    await funcionario.insert()
    return FuncionarioOut(
        id=str(funcionario.id),
        nome=funcionario.nome,
        cpf=funcionario.cpf,
        departamento_id=str(funcionario.departamento_id),
        gestor_id=str(funcionario.gestor_id) if funcionario.gestor_id else None
    )

@router.get("/", response_model=List[FuncionarioOut])
async def listar_funcionarios():
    funcionarios = await Funcionario.find_all().to_list()
    return [
        FuncionarioOut(
            id=str(f.id),
            nome=f.nome,
            cpf=f.cpf,
            departamento_id=str(f.departamento_id),
            gestor_id=str(f.gestor_id) if f.gestor_id else None
        ) for f in funcionarios
    ]

@router.get("/{id}", response_model=FuncionarioOut)
async def obter_funcionario(id: str):
    funcionario = await Funcionario.get(ObjectId(id))
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return FuncionarioOut(
        id=str(funcionario.id),
        nome=funcionario.nome,
        cpf=funcionario.cpf,
        departamento_id=str(funcionario.departamento_id),
        gestor_id=str(funcionario.gestor_id) if funcionario.gestor_id else None
    )

@router.delete("/{id}")
async def deletar_funcionario(id: str):
    funcionario = await Funcionario.get(ObjectId(id))
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    await funcionario.delete()
    return {"mensagem": "Funcionário deletado"}