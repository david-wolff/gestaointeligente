from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from fastapi import FastAPI

from app.models.cargo import Cargo 
from app.models.funcionario import Funcionario  
from app.models.departamento import Departamento
from app.models.funcionario_cargo import FuncionarioCargo
from app.models.curso import Curso
from app.models.certificado import Certificado
from app.models.conhecimento import Conhecimento
from app.models.funcionario_conhecimento import FuncionarioConhecimento
from app.models.referencia_bibliografica import ReferenciaBibliografica
from app.models.avaliacao import Avaliacao

MONGO_URL = "mongodb://admin:gestaointeligente@localhost:27017/?authSource=gestao_db"

async def init_db(app: FastAPI):
    client = AsyncIOMotorClient(MONGO_URL)
    await init_beanie(
        database=client["gestao_db"],
        document_models=[
            Funcionario,
            Departamento,
            Cargo,
            FuncionarioCargo,
            Curso, 
            Certificado, 
            Conhecimento,
            FuncionarioConhecimento, 
            ReferenciaBibliografica, 
            Avaliacao
        ]
    )