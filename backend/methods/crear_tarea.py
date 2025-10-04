from models.Tarea import Tarea

tareas = []

def crear(tarea:Tarea):
    try:
        nueva_tarea = tarea.dict()
        nueva_tarea["id"] = len(tareas) + 1
        guardar_tarea(nueva_tarea)
        return {"mensaje": "Tarea creada", "tarea": nueva_tarea}
    except Exception as e:
        return {"status": "Error", "menssage": e}

def guardar_tarea(tarea):

    tareas.append(tarea)
    return True
