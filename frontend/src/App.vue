<template>
  <div class="layout">
    <nav class="sidebar">
       <img src="@/assets/logoLT2.png" alt="Logo" class="logo" />
      <ul>
        <li><router-link :to="{name:'home'}">Home</router-link></li>
        <li><router-link :to="{name:'marcas_list'}">Marcas</router-link></li>
        <li><router-link :to="{name:'categorias_list'}">Categorias</router-link></li>

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
.sidebar {
  width: 120px;
  background: #f5f5f5;
  border-right: 1px solid #ddd;
  padding: 2rem 1rem;
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
}
.sidebar router-link {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.2s;
}
.sidebar router-link.active {
  color: #1976d2;
  font-weight: bold;
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
