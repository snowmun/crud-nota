<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/note">Notas</router-link>|
      <router-link to="/label">Etiquetas</router-link>|
      <router-link to="/user">Usuarios</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import '@/assets/css/app.css';
export default {
  name: 'App',
}
</script>