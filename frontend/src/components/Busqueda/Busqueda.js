

export default async function fetchData(tarea, descripcion) {
  try {
    const body = JSON.stringify({
      titulo: tarea,
      descripcion: descripcion
    });

    const response = await fetch('http://127.0.0.1:8000/crear_tarea', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: body
    });
    if (response.status === "error") {
      alert("Error al crear la tarea");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('error grave al crear tarea', error);
    alert("Error al crear la tarea");
  }
}