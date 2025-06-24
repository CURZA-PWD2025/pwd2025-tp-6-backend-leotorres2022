<template>
  <div class="layout">
    <nav class="sidebar">
       <img src="@/assets/logoLT2.png" alt="Logo" class="logo" />
      <ul>
        <li><router-link :to="{name:'home'}">Home</router-link></li>
        <li><router-link :to="{name:'marcas_list'}">Marcas</router-link></li>
        <li><router-link :to="{name:'categorias_list'}">Categorias</router-link></li>
        <li><router-link :to="{name:'proveedores_list'}">Proveedores</router-link></li>
        <li><router-link :to="{name:'articulos_list'}">Articulos</router-link></li>

      </ul>
    </nav>
    <main class="content">
     <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
.layout {
  display: flex;
  flex-direction: row;
  height: 100vh;
  background: #fff;
  min-height: 100vh;
}

/* Animación para el sidebar */
.sidebar {
  width: 120px;
  background: #f5f5f5;
  border-right: 1px solid #ddd;
  padding: 2rem 1rem;
  /* Efecto slide-in */
  transform: translateX(-150%);
  opacity: 0;
  animation: slideInSidebar 0.7s cubic-bezier(.77,0,.18,1) forwards;
}

@keyframes slideInSidebar {
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.sidebar li {
  margin: 0;
  opacity: 0;
  transform: translateX(-50px);
  animation: slideInLink 0.7s cubic-bezier(.77,0,.18,1) forwards;
}

.sidebar li:nth-child(1) { animation-delay: 0.5s; }
.sidebar li:nth-child(2) { animation-delay: 1s; }
.sidebar li:nth-child(3) { animation-delay: 1.5s; }
.sidebar li:nth-child(4) { animation-delay: 2s; }
.sidebar li:nth-child(5) { animation-delay: 2.5s; }

@keyframes slideInLink {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.sidebar a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.2s, background 0.2s, padding 0.2s;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  display: block;
}

.sidebar a:hover {
  background: #e3f2fd;
  color: #1976d2;
  padding-left: 1.5rem;
}

.sidebar a.router-link-active {
  color: #1976d2;
  font-weight: bold;
  padding-left: 1.5rem;
}
.content {
  flex: 1;
  padding: 2rem;
}
.logo {
  width: 90px;
  height: 100px;
}
.sidebar .logo {
  margin: 34px auto 20px;
}
</style>
