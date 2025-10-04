from models.Tarea import Tarea

tareas = []

def crear(tarea:Tarea):
    nueva_tarea = dict(tarea)
    nueva_tarea["id"] = len(tareas) + 1
    tareas.append(nueva_tarea)

    return {"mensaje": "Tarea creada", "tarea": nueva_tarea}