<script setup>
import './Busqueda.css';
import fetchData from './Busqueda.js';

const handleClick = () => {
  // recuperar los valores de los inputs
  const task = document.querySelector('.Task').value;
  const description = document.querySelector('.descripcion').value;
  fetchData(task, description);
  document.querySelector('.Task').value = '';
  document.querySelector('.descripcion').value = '';
};
</script>

<template>
  <div class="search-bar">
    <input class="Task" type="text" placeholder="Crear tarea..." />
    <input class="descripcion" type="text" placeholder="Descripcion..." />
    <button class="boton" @click="handleClick">Buscar</button>
  </div>
</template>

<style scoped>
</style>