<script setup>
import './Busqueda.css';
import fetchData from './Busqueda.js';
import { ref } from 'vue';

const task = ref('');
const description = ref('');

const emit = defineEmits(['actualizar-tareas']);

const handleClick = async () => {
  try {
    if (!task.value || !description.value) {
      alert('Por favor, completa ambos campos antes de agregar una tarea.');
      return;
    }
    const tareas = await fetchData(task.value, description.value);
    emit('actualizar-tareas', tareas.tareas);
    task.value = '';
    description.value = '';
  } catch (error) {
    console.error('Error al crear la tarea:', error);
  }
};
</script>

<template>
  <div class="search-bar">
    <input v-model="task" class="Task" type="text" placeholder="Crear tarea..." />
    <input v-model="description" class="descripcion" type="text" placeholder="Descripcion..." />
    <button class="boton" @click="handleClick">Agregar</button>
  </div>
</template>

<style scoped>
</style>