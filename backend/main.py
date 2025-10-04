from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from methods.crear_tarea import crear

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
