from fastapi import FastAPI
from app.database import init_db
from app.routes import funcionario


app = FastAPI(title="Sistema de Gestão")

@app.on_event("startup")
async def startup_event():
    await init_db(app)

@app.get("/")
async def root():
    return {"msg": "Sistema de Gestão ativo"}


app.include_router(funcionario.router)