<template>
  <div>
      <b-card no-body>
      <b-card-header>Nombre Usuario: {{ userList.nombre_usuario }}</b-card-header>
      <b-card-body>
          <p>Nombre y Apellido: {{ userList.nombre }} {{ userList.apellido }}</p>
          <p>Rut: {{ userList.rut }}</p>
          <p>Edad: {{ userList.edad }}</p>
          <p>Emial: {{ userList.email }}</p>
          <p>Comuna: {{ userList.nombre_comuna }}</p>
          <p>Region: {{ userList.nombre_region }}</p>
          <p>Profesion: {{ userList.profesion }}</p>
      </b-card-body>
      </b-card>
  </div>
</template>

<script>
import userServices from '@/services/user/userService'

export default {
props: {
  userId: {
    type: Number,
    required: true
  }
},
data() {
  return {
    loading: false,
    userList: {}
  }
},
async mounted() {
  this.getUserById(this.userId)
},
methods: {
  async getUserById(id) {
    this.loading = true
      await userServices.userList(id)
      .then(({code , data}) => {
        if (code == 200){
          this.userList = data[0]
        }else{
          this.$toasted.error('Error en el servidor no se pudo obtener las notas')
        }
      })
      .catch(() => {
        this.$toasted.error('Error al obtener la informacion')
      })
      .finally(() => {
        this.loading = false;
      });
  }
}
}
</script>
<style scoped>
.card {
margin: 2rem;
}

.card-header-title {
font-size: 1.5rem;
font-weight: bold;
}

.card-footer {
background-color: #f5f5f5;
}
</style>