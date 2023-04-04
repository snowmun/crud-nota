<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <h3 class="text-center">Iniciar Sesion</h3>
          </div>
          <div class="card-body">
            <form @submit.prevent="submitForm">
              <div class="form-group">
                <label for="username">Nombre de usuario</label>
                <input type="text" class="form-control" v-model="username" required>
              </div>
              <b-button type="submit" variant="success" class="mt-3 btn-guardar">
                  <b-spinner small v-if="loading"></b-spinner>
                  <span v-else>Login</span>
                </b-button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';
import loginServices from '@/services/user/loginService';

export default {
  data() {
    return {
      username: null,
      password: null,
      loading: false,
    };
  },
  methods: {
    ...mapMutations(['setUser', 'setToken']),
    async submitForm() {
      this.loading = true;
      await loginServices.userLogin(this.username)
        .then(({code,data}) => {
          if (code == 200 && data.length > 0){
            this.$toasted.success('Logeado con exito');
            this.$store.commit('setUsername', this.username);
            this.$store.commit('setUserId', data[0].id);
            this.$store.commit('setToken', data.token);
            this.back()

          }else{
            this.$toasted.error('El usuario no existe');
          }
        })
        .catch(() => {
          this.$toasted.error('Error al logearse');
        })
        .finally(() => {
          this.loading = false;
        });
    },
    back() {
      this.$router.push({
          name: 'home',
      })
    },
  },
};
</script>
