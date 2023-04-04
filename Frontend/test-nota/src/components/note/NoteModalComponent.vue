<template>
    <div>
        <b-card no-body>
        <b-card-header>{{ noteList.titulo }}</b-card-header>
        <b-card-body>
            <p>Usuario: {{ noteList.nombre_usuario }}</p>
            <p>Estado: {{ noteList.activo == 1? 'Activo':'Inactivo' }}</p>
            <p>Contenido: {{ noteList.contenido }}</p>
            <p>Terminar antes de: {{ noteList.fecha_termino }}</p>
            <p>Clasificacion: {{ noteList.tipo_emergencia }}</p>
            <!-- aquí puedes mostrar el resto de la información de la nota -->
        </b-card-body>
        </b-card>
    </div>
  </template>
  
<script>
import noteServices from '@/services/note/noteService'

export default {
  props: {
    noteId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      loading: false,
      noteList: {}
    }
  },
  async mounted() {
    this.getNoteById(this.noteId)
  },
  methods: {
    async getNoteById(id) {
      this.loading = true
        await noteServices.noteList(id)
        .then(({code , data}) => {
          if (code == 200){
            // se agrega la propiedad index a cada objeto en notaList
            this.noteList = data.nota[0]
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