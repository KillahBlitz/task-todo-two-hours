from fastapi import FastAPI
from methods.crear_tarea import crear
<<<<<<< HEAD
=======
from models.Tarea import Tarea
>>>>>>> ba08c89e82ebfd7af44613817b3f09bb626a57b8

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API de Tareas funcionando"}

<<<<<<< HEAD
@app.post("/instertar_tarea")
def instertar_tarea(data: dict):
    crear(data)
=======
@app.post("/crear_tarea")
def crear_tarea(data:dict):
    nueva_tarea = crear(data)
    
    return nueva_tarea
>>>>>>> ba08c89e82ebfd7af44613817b3f09bb626a57b8
