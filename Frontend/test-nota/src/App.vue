<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/note">Notas</router-link> |
      <router-link to="/label">Etiquetas</router-link> |
      <router-link to="/user">Usuarios</router-link> |
      <router-link to="/note_user" v-if="isLoggedIn"  >Notas Usuario</router-link> |
      <router-link v-if="!isLoggedIn" to="/login" exact-active-class="active">{{ loginOrLogout }}</router-link>
      <router-link v-else to="/" exact-active-class="active" @click="handleLogout">{{ loginOrLogout }}</router-link>

    </nav>
    <router-view />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import '@/assets/css/app.css';

export default {
  name: 'App',
  computed: {
    ...mapState(['user', 'token']),
    isLoggedIn() {
      return this.token !== null;
    },
    loginOrLogout() {
      return this.isLoggedIn ? 'Logout' : 'Login';
    }
  },

  methods: {
    ...mapActions(['logoutUser']),
    handleLogout() {
      this.logoutUser();
      this.$router.push({ name: 'home' });
    }
  }
};
</script>
