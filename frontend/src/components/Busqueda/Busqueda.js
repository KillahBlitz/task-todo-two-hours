

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
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('There has been a problem with your fetch operation:', error);
  }
}