from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from fastapi import FastAPI

from app.models.funcionario import Funcionario  
from app.models.departamento import Departamento

MONGO_URL = "mongodb://admin:gestaointeligente@localhost:27017/?authSource=gestao_db"

async def init_db(app: FastAPI):
    client = AsyncIOMotorClient(MONGO_URL)
    await init_beanie(
        database=client["gestao_db"],
        document_models=[
            Funcionario,
            Departamento  # ✅ Agora está registrado corretamente
        ]
    )