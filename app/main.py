from fastapi import FastAPI
from app.database import init_db
from app.routes import funcionario, departamento, cargo, funcionario_cargo, curso, certificado, conhecimento, funcionario_conhecimento, referencia_bibliografica, avaliacao


app = FastAPI(title="Sistema de Gestão")

@app.on_event("startup")
async def startup_event():
    await init_db(app)

@app.get("/")
async def root():
    return {"msg": "Sistema de Gestão ativo"}


app.include_router(funcionario.router)
app.include_router(departamento.router)
app.include_router(cargo.router)
app.include_router(funcionario_cargo.router)
app.include_router(curso.router)
app.include_router(certificado.router) 
app.include_router(conhecimento.router)
app.include_router(funcionario_conhecimento.router)
app.include_router(referencia_bibliografica.router)
app.include_router(avaliacao.router)

