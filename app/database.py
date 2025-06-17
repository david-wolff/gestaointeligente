from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from fastapi import FastAPI

from app.models.cargo import Cargo 
from app.models.funcionario import Funcionario  
from app.models.departamento import Departamento
from app.models.funcionario_cargo import FuncionarioCargo


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
        ]
    )