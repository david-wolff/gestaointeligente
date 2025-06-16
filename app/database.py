from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.funcionario import Funcionario  

import os
from fastapi import FastAPI

MONGO_URL = "mongodb://admin:gestaointeligente@localhost:27017/?authSource=gestao_db"

async def init_db(app: FastAPI):
    client = AsyncIOMotorClient(MONGO_URL)
    await init_beanie(
        database=client["gestao_db"],
        document_models=[Funcionario], 
    )