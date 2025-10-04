from models.Tarea import Tarea

tareas = []

def crear(tarea:dict):
    try:
        tarea["id"] = len(tareas) + 1
        tarea = Tarea(**tarea)
        if guardar_tarea(tarea):
            return {"status": "success", "tarea": tarea}
        else:
            return {"status": "Error", "menssage": "No se pudo guardar la tarea"}
    except Exception as e:
        return {"status": "Error", "menssage": "No se mandaron los datos esperados"}

def guardar_tarea(tarea):
    try:
        tareas.append(tarea)
        return True
    except Exception as e:
        return False
