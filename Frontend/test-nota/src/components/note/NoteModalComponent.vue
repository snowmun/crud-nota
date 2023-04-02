<template>
    <div>
        <b-card no-body>
        <b-card-header>{{ note.titulo }}</b-card-header>
        <b-card-body>
            <p>Usuario: {{ note.usuario }}</p>
            <p>Estado: {{ note.estado }}</p>
            <p>Contenido: esta es una descripción larga</p>
            <p>Tipo de etiqueta: pan</p>
            <p>Terminar antes de: 20 de enero del 2024</p>
            <!-- aquí puedes mostrar el resto de la información de la nota -->
        </b-card-body>
        </b-card>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      noteId: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        note: {}
      }
    },
    created() {
      // Aquí puedes hacer una petición a tu API para obtener la nota correspondiente al ID que se te pasó como parámetro
      // Por ejemplo, supongamos que tienes una función llamada getNoteById que devuelve la nota correspondiente al ID que le pasas
      this.note = this.getNoteById(this.noteId)
    },
    methods: {
      getNoteById(id) {
        // aquí puedes hacer la petición a tu API
        // y devolver la nota correspondiente al ID
        // en este ejemplo, devolvemos una nota de prueba
        return { id: id, titulo: 'Arreglar Pc', usuario: 'Usuario de prueba', estado: 'Activa' }
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