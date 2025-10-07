<script setup>
import eliminarTaskFinal from './Tareas';
import './Tareas.css';
const props = defineProps({
  tareas: {
    type: Object,
    required: true
  }
});

function eliminarTask(id){
  eliminarTaskFinal(id);
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
              <button @click=eliminarTask(tarea.id)>Eliminar</button>
            </div>
          </div>
        </div>
    </div>
</template>

<style scoped>
</style>