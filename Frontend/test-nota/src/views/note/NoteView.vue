<template>
  <b-card>
    <div class="d-flex justify-content-between align-items-center">
      <b-button variant="primary" class="mb-3 col-sm-auto mx-sm-2 " @click="createNote" >Crear Nota</b-button>
        <div class="d-flex">
          <b-input-group class="mb-3 ">
            <b-form-input v-model="search" placeholder="Buscar por titulo"/>
            <b-input-group-append>
              <b-button @click="searchData" variant="primary">Buscar</b-button>
            </b-input-group-append>
          </b-input-group>
      </div>
    </div>
    <b-tabs>
      <b-tab title="Todas">
        <b-table striped hover stacked="md" :items="noteList" v-if="!loading" :fields="fieldsTable">
          <template v-slot:cell(contenido)="data">
            <div>{{ data.value.slice(0, 20) }}{{ data.value.length > 20 ? '...' : '' }}</div>
          </template>
          <template #cell(action)="row">
            <div>
              <b-button size="sm" variant="warning" class="mx-1 my-1" @click="updateNote(row.item.id)">
                <b-icon-pencil></b-icon-pencil>
              </b-button>
              <b-button size="sm" variant="secondary" class="mx-1 my-1" @click="openModal(row.item.id)">
                <b-icon-eye></b-icon-eye> 
              </b-button>
              <b-button size="sm" variant="danger" class="mx-1 my-1 " >
                <b-icon-x></b-icon-x>
              </b-button>
            </div>
          </template>
        </b-table>
        <template>
        <div v-if="loading" class="text-center text-primary my-2 text-warning">
          <b-spinner align="middle"></b-spinner>
          <span>Cargando</span>
        </div>
      </template>
      </b-tab>
      <b-tab title="Pan"></b-tab>
      <b-tab title="Verdura"></b-tab>
      <b-tab title="Comida"></b-tab>
    </b-tabs>
    <b-modal ref="noteModal" @hidden="onModalClose">
      <NoteModalComponent :note-id="noteId"/>
    </b-modal>

  </b-card>
</template>

<script>
import NoteModalComponent from'@/components/note/NoteModalComponent.vue';
import noteServices from '@/services/note/noteService'

export default {
  name: 'NoteView',
  components: {
    NoteModalComponent
  },
  data() {
    return {
      loading: false,
      noteId: null,
      fieldsTable: [
        { key: 'index', label: '#', sortable: false },
        { key: 'titulo', label: 'Titulo', sortable: false },
        { key: 'contenido', label: 'Contenido', sortable: false},
        { key: 'nombre_usuario', label: 'Usuario', sortable: false },
        { key: 'estado', label: 'Estado', sortable: false },
        { key: 'tipo_emergencia', label: 'Tipo de Emergencia', sortable: false },
        { key: 'end_date', label: 'Fecha Termino', sortable: false },
        { key: 'action', label: 'Acciones', sortable: false
        },
      ],

      noteList: null,
      search: ''
    }
  },
  async mounted() {
    this.init()
  },
  methods: {
    searchData() {
      // Aquí puedes realizar la búsqueda en la lista de items utilizando el valor de search
      console.log('Search: ', this.search);
    },

    async init(){
      await this.getNotes()
    },

    async getNotes(){
      this.loading = true
      await noteServices.notesList()
        .then(({code , data}) => {
          if (code == 200){
            // se agrega la propiedad index a cada objeto en notaList
            this.noteList = data.notas.map((nota, index) => ({...nota, index: index + 1}))
            this.$toasted.success('vista de la nota cargada')

          }else{
            this.$toasted.error('Error en el servidor no se pudo cargar la nota')
          }
        })
        .catch(() => {
          this.$toasted.error('Error al obtener la informacion')
        })
        .finally(() => {
          this.loading = false;
        });
    },

    createNote() {
      this.$router.push({
        name: 'noteform',
        params: { id: '0', action: 'create' }
      })
    },

    updateNote(id) {
      this.$router.push({
        name: 'noteform',
        params: { id, action: 'update' }
      })
    },
    openModal(id) {
      this.noteId = id;
      this.$refs.noteModal.show();
    },
    onModalClose() {
        this.noteId = null;
    }
  }
};
</script>
