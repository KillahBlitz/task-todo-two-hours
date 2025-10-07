export default async function eliminarTaskFinal(id) {
    const response = await fetch(`http://127.0.0.1:8000/eliminar_tarea/${id}`, {
        method: 'DELETE',
    });
    const data = await response.json();
    console.log(data);
}