from fastapi import APIRouter
from pydantic import BaseModel

ruta_crear_tareas = APIRouter()

tareas = []

class Tarea(BaseModel):
    titulo: str
    descripcion: str = ""

@ruta_crear_tareas.post("/crear_tarea/")
def crear(tarea:Tarea):
    nueva_tarea = dict(tarea)
    nueva_tarea["id"] = len(tareas) + 1
    tareas.append(nueva_tarea)

    return {"mensaje": "Tarea creada", "tarea": nueva_tarea}