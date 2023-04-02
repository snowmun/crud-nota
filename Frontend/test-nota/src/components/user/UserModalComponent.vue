<template>
    <div>
        <b-card no-body>
        <b-card-header>{{ user.nombre }} {{ user.nombre }}</b-card-header>
        <b-card-body>
            <p>Rut: {{ user.rut }}</p>
            <p>edad: {{ user.edad }}</p>
            <p>profesion: {{ user.profesion }}</p>
            <p>Email: {{ user.email }}</p>
            <p>Comuna: {{ user.comuna }}</p>
            <p>Region: {{ user.region }}</p>
            <p>Cantidad de Tareas: 5</p>

        </b-card-body>
        </b-card>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      userId: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        user: {}
      }
    },
    created() {
      // Aquí puedes hacer una petición a tu API para obtener la nota correspondiente al ID que se te pasó como parámetro
      // Por ejemplo, supongamos que tienes una función llamada getNoteById que devuelve la nota correspondiente al ID que le pasas
      this.user = this.getNoteById(this.userId)
    },
    methods: {
      getNoteById(id) {
        // aquí puedes hacer la petición a tu API
        // y devolver la nota correspondiente al ID
        // en este ejemplo, devolvemos una nota de prueba
        return { id: id, nombre: 'orlando', apellido: 'munoz', rut: '17790074-5', edad:31,profesion:'Programador',email:'smashdojo@gmail.com',comuna:'viña del mar', region:'valparaiso' }
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