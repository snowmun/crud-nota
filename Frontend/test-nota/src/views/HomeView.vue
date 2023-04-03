<template>
  <b-card>
    <h3 class="text-center">Todas las Notas</h3>
    <div class="table-responsive">
      <b-table striped hover stacked="md" :items="notaList" v-if="!loading" :fields="fieldsTable" class="margin-top__20">
        <template v-slot:cell(contenido)="data">
          <div>{{ data.value.slice(0, 20) }}{{ data.value.length > 20 ? '...' : '' }}</div>
        </template>
      </b-table>
      <template>
        <div v-if="loading" class="text-center text-primary my-2 text-warning">
          <b-spinner align="middle"></b-spinner>
          <span>Cargando</span>
        </div>
      </template>
    </div>
  </b-card>
</template>

<script>
import noteServices from '@/services/note/noteService'

export default {
  name: 'HomeView',
  data() {
    return {
      loading: false,
      notaList: null,
      fieldsTable: [
        { key: 'index', label: '#', sortable: false },
        { key: 'titulo', label: 'Titulo', sortable: false },
        { key: 'contenido', label: 'Contenido', sortable: false},
        { key: 'nombre_usuario', label: 'Usuario', sortable: false },
        { key: 'estado', label: 'Estado', sortable: false },
        { key: 'tipo_emergencia', label: 'Tipo de Emergencia', sortable: false },
        { key: 'end_date', label: 'Fecha Termino', sortable: false },
      ],
    }
  },
  async mounted() {
    this.init()
  },

  methods:{
    async init(){
      await this.getNotes()
    },

    async getNotes(){
      this.loading = true
      await noteServices.notesList()
        .then(({code , data, detail= null}) => {
          if (code == 200){
            // se agrega la propiedad index a cada objeto en notaList
            this.notaList = data.notas.map((nota, index) => ({...nota, index: index + 1}))
            this.$toasted.success('Notas cargadas correctamente')

          }else{
            this.$toasted.error('Error en el servidor del servidor')
          }
        })
        .catch(() => {
          this.$toasted.error('Error al obtener la informacion')
        })
        .finally(() => {
          this.loading = false;
        });
    },
  }
};
</script>

<style scoped>
.custom-button {
  border: 1px solid #dee2e6;
  border-radius: 5px;
  padding: 0.5rem 1rem;
}

.table-responsive {
  overflow-x: auto;
}
</style>
