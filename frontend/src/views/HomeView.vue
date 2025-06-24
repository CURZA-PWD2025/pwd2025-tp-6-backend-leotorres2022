<template>
  <div class="home-container">
    <h1>Bienvenidos a la página de Artículos e Insumos Informáticos</h1>
    <p class="subtitle">
      Gestioná marcas, categorías, proveedores y los artículos desde el menú de la izquierda.
    </p>
  </div>
</template>

<script setup lang="ts">

</script>
<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 60vh;
  background: #f8fafc;
  padding: 2rem;
  margin-top: 2rem;
  width: 100%;
  box-sizing: border-box;
}
h1 {
  color: #1976d2;
  font-size: 2rem;
  margin-bottom: 1rem;
  text-align: center;
}
.subtitle {
  color: #555;
  font-size: 1.1rem;
  text-align: center;
}
</style>
