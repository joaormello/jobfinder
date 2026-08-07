from fastapi import FastAPI
from app.services.vaga_service import (listar_vagas, buscar_vaga_por_id, buscar_vaga_por_titulo)

app = FastAPI()

@app.get("/")
def home():
    return{
        "mensagem": "JobFinder API Online"
    }

@app.get("/health")
def health():
    return{
        "status":"ok"
    }

@app.get("/vagas")
def buscar_vagas():
    vagas = listar_vagas()

    return vagas

@app.get("/vagas/{id_vaga}")
def buscar_vaga(id_vaga: int):
    vaga = buscar_vaga_por_id(id_vaga)

    return vaga

@app.get("/vagas")
def buscar_vagas(titulo: str | None = None):
    if titulo :
        return buscar_vaga_por_titulo(titulo)

    return listar_vagas