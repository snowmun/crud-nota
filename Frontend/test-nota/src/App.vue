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

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}

nav {
  padding: 30px;
  text-align: center;

}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #ffae00;
}
</style>
