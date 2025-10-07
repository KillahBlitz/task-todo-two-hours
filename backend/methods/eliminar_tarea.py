def tareas_limpias(task_id, lista):
    for tarea in lista:
        if tarea.id == task_id:
            lista.remove(tarea)
            break
    return lista