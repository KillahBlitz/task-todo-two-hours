from fastapi import FastAPI
from methods.crear_tarea import ruta_crear_tareas

app = FastAPI()

app.include_router(ruta_crear_tareas)