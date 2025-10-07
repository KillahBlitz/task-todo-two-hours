<script setup>
import eliminarTaskFinal from './Tareas';
import './Tareas.css';

defineProps({
  tareas: {
    type: Array,
    required: true,
    default: () => []
  }
});

const emit = defineEmits(['update:tareas']);

async function eliminarTask(event, id) {
  try {
    const tareasActualizadas = await eliminarTaskFinal(id);
    emit('update:tareas', tareasActualizadas);
  } catch (error) {
    console.error('Error al eliminar tarea:', error);
  }
}
</script>

<template>
    <div>
        <div class="tareas-grid">
          <div v-for="tarea in tareas" :key="tarea.id" class="tarea-box">
            <div class="tarea-id">ID: {{ tarea.id }}</div>
            <div class="tarea-titulo">
              {{ tarea.titulo }}
            </div>
            <div class="tarea-descripcion">
              {{ tarea.descripcion }}
            </div>
            <div class="boton-eliminar">
              <button @click="(event) => eliminarTask(event, tarea.id)">Eliminar</button>
            </div>
          </div>
        </div>
    </div>
</template>

<style scoped>
</style>