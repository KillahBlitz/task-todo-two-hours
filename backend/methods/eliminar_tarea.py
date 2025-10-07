def tareas_limpias(task_id, lista):
    lista = [tarea for tarea in lista if tarea['id'] != task_id]
    return lista