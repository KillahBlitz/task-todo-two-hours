<script setup>
import { ref } from 'vue';
import Header from './components/Header/Header.vue';
import Busqueda from './components/Busqueda/Busqueda.vue';
import Tareas from './components/Tareas/Tareas.vue';

const listaTareas = ref([]);

const actualizarTareas = (nuevasTareas) => {
  listaTareas.value = nuevasTareas;
};
</script>

<template>
  <div>
    <Header/>
    <Busqueda @actualizar-tareas="actualizarTareas"/>
    <Tareas v-model:tareas="listaTareas"/>
  </div>
</template>


<style scoped>

</style>
