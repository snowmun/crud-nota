<template>
  <b-card>
    <div class="d-flex justify-content-between align-items-center">
      <b-button variant="primary" class="mb-3 col-sm-auto mx-sm-2 " @click="createNote" >Crear Nota</b-button>
        <div class="d-flex col-3">
          <b-input-group class="mb-3 ">
            <b-form-input v-model="search" placeholder="Buscar por titulo"/>
          </b-input-group>
      </div>
    </div>
    <b-tabs>
      <b-tab title="Todas">
        <b-table striped hover stacked="md" :items="filteredNoteListByTitle()" v-if="!loading" :fields="fieldsTable">
          <template v-slot:cell(contenido)="data">
            <div>{{ data.value.slice(0, 20) }}{{ data.value.length > 20 ? '...' : '' }}</div>
          </template>
          <template v-slot:cell(activo)="data">
            <div>{{ data.value == 1?'Activo':'Inactivo' }}</div>
          </template>
          <template #cell(action)="row">
            <div>
              <b-button size="sm" variant="warning" class="mx-1 my-1" @click="updateNote(row.item.id)">
                <b-icon-pencil></b-icon-pencil>
              </b-button>
              <b-button size="sm" variant="secondary" class="mx-1 my-1" @click="openModal(row.item.id)">
                <b-icon-eye></b-icon-eye> 
              </b-button>
              <b-button size="sm" variant="danger" class="mx-1 my-1 " @click="destroy(row.item.id)" >
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
      <b-tab v-for="(label) in lebelList" :key="label.id" :title="label.nombre">
        <b-table striped hover stacked="md" :items="filteredNoteList(label.id)" :fields="fieldsTable" :filter="search">
          <template v-slot:cell(contenido)="data">
            <div>{{ data.value.slice(0, 20) }}{{ data.value.length > 20 ? '...' : '' }}</div>
          </template>
          <template v-slot:cell(activo)="data">
            <div>{{ data.value == 1?'Activo':'Inactivo' }}</div>
          </template>
          <template #cell(action)="row">
            <div>
              <b-button size="sm" variant="warning" class="mx-1 my-1" @click="updateNote(row.item.id)">
                <b-icon-pencil></b-icon-pencil>
              </b-button>
              <b-button size="sm" variant="secondary" class="mx-1 my-1" @click="openModal(row.item.id)">
                <b-icon-eye></b-icon-eye> 
              </b-button>
              <b-button size="sm" variant="danger" class="mx-1 my-1 " @click="destroy(row.item.id)" >
                <b-icon-x></b-icon-x>
              </b-button>
            </div>
          </template>
        </b-table>
      </b-tab>
    </b-tabs>
    <b-modal ref="noteModal" @hidden="onModalClose">
      <NoteModalComponent :note-id="noteId"/>
    </b-modal>
  </b-card>
</template>

<script>
import NoteModalComponent from'@/components/note/NoteModalComponent.vue'
import noteServices from '@/services/note/noteService'
import labelService from '@/services/label/labelService'

export default {
  name: 'NoteView',
  components: {
    NoteModalComponent
  },
  
  data() {
    return {
      loading: false,
      noteId: null,
      lebelList: null,
      fieldsTable: [
        { key: 'index', label: '#', sortable: false },
        { key: 'titulo', label: 'Titulo', sortable: false },
        { key: 'contenido', label: 'Contenido', sortable: false},
        { key: 'nombre_usuario', label: 'Usuario', sortable: false },
        { key: 'activo', label: 'Estado', sortable: false },
        { key: 'tipo_emergencia', label: 'Tipo de Emergencia', sortable: false },
        { key: 'fecha_termino', label: 'Fecha Termino', sortable: false },
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
  computed: {
    filteredNoteList() {
      return (labelId) => {
        return this.noteList.filter(note => note.id_etiqueta === labelId)
      }
    },
    filteredNoteListByTitle() {
      return () => {
        const search = this.search.trim().toLowerCase();
        if (!search) {
          return this.noteList;
        }
        return this.noteList.filter(note => note.titulo.toLowerCase().includes(search));
      }
    }
  },
  methods: {
    searchData() {
      if (!this.search) {
        // Si no se ingresó ningún término de búsqueda, mostrar todas las notas
        this.filteredNoteList = this.noteList;
      } else {
        // Filtrar las notas por título
        this.filteredNoteList = this.noteList.filter(note => note.titulo.includes(this.search));
      }
    },
    async init(){
      await this.getNotes()
      await this.getLabels()
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
    async getLabels(){
      await labelService.labelsList()
        .then(({code , data}) => {
          if (code == 200){
            this.lebelList = data
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

    destroy(id) {
      this.$swal({
        title: 'Estás seguro?',
        text: 'Esta acción no se puede deshacer',
        icon: 'warning',
        showDenyButton: true,
        buttons: false,
        buttons: {
          confirm: {
            text: 'Si, eliminar',
            value: true,
            visible: true,
            className: 'bg-danger',
            closeModal: true,
          },
          deny: {
            text: 'No, cancelar',
            value: false,
            visible: true,
            className: 'bg-primary',
            closeModal: true,
          },
        },
      }).then((result) => {
        if (result) {
          noteServices.deleteNoteById(id)
            .then(({code}) => {
              if (code == 200){
                this.$toast.success(message)
              } else {
                this.$toast.warning('error en el servidor al eliminar ');
              }
            })
            .catch(() => {
              this.$toast.error('Error al eliminar');
            })
            .finally(() => {
              this.getNotes();
            });
        }
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
