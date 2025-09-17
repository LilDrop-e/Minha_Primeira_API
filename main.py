# API Framework
from fastapi import FastAPI

# Manipulação de dados (se necessário)
import pandas as pd

# Para execução da API
import uvicorn

# Utilitários (se necessário)
import json

app = FastAPI(title="Minha Primeira API")

@app.get("/")
def home():
    """Endpoint básico que retorna informações sobre a API"""
    return {
        "projeto": "Minha API",
        "autor": "Pedro Duran",
        "descricao": "API para servir dados de video games",
        "total_registros": len(dataset.csv)
    }