from pydantic import BaseModel

class Tarea(BaseModel):
    titulo: str
    descripcion: str = ""