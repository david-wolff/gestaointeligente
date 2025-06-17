from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId

from app.models.curso import Curso
from app.schemas.curso import CursoIn, CursoOut

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.post("/", response_model=CursoOut)
async def criar_curso(dados: CursoIn):
    try:
        curso = Curso(**dados.dict())
        await curso.insert()
        return CursoOut(id=str(curso.id), **dados.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar curso: {str(e)}")

@router.get("/", response_model=List[CursoOut])
async def listar_cursos():
    cursos = await Curso.find_all().to_list()
    return [CursoOut(id=str(c.id), nome=c.nome, emissor=c.emissor, tipo=c.tipo) for c in cursos]

@router.delete("/{id}")
async def deletar_curso(id: str):
    curso = await Curso.get(ObjectId(id))
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    await curso.delete()
    return {"mensagem": "Curso deletado"}