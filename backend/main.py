from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from methods.crear_tarea import crear, obtener_tareas
from methods.eliminar_tarea import tareas_limpias

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)


@app.get("/")
def read_root():
    return {"mensaje": "API de Tareas funcionando"}

@app.post("/crear_tarea")
def crear_tarea(data:dict):
    nueva_tarea = crear(data)
    return nueva_tarea

@app.delete("/eliminar_tarea/{task_id}")
def eliminar_tarea(task_id: int):
    list_tareas = obtener_tareas()
    tareas_finales = tareas_limpias(task_id, list_tareas)
    return {"status": "success", "tareas": tareas_finales}