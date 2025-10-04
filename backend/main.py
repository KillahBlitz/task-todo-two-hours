from fastapi import FastAPI
from methods.crear_tarea import crear
from models.Tarea import Tarea

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API de Tareas funcionando"}

@app.post("/crear_tarea")
def crear_tarea(data:dict):
    nueva_tarea = crear(data)
    
    return nueva_tarea
