from pydantic import BaseModel

class Tarea(BaseModel):
    id: int = 0
    titulo: str
    descripcion: str = ""