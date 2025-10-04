from fastapi import FastAPI
from methods.crear_tarea import crear

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API de Tareas funcionando"}

@app.post("/instertar_tarea")
def instertar_tarea(data: dict):
    crear(data)
