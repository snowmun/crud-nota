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
        <b-table striped hover stacked="md" :items="items" v-if="!loading" :fields="fieldsTable">
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
          <template>
            <div class="text-center text-primary my-2">
              <b-spinner align="middle"></b-spinner>
              <strong>Cargando</strong>
            </div>
          </template>
        </b-table>
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
        {
          key: 'id',
          label: 'Id',
          sortable: false
        },
        {
          key: 'titulo',
          label: 'Titulo',
          sortable: false
        },
        {
          key: 'usuario',
          label: 'Usuario',
          sortable: false
        },
        {
          key: 'estado',
          label: 'Estado',
          sortable: false
        },
        {
          key: 'action',
          label: 'Acciones',
          sortable: false
        },
        
      ],
      items: [
        { id: 40, titulo: 'Dickerson', usuario:'name',estado: 'active' },
        { id: 21, titulo: 'Larsen', usuario:'name',estado: 'active' },
        { id: 89, titulo: 'Geneva', usuario:'name',estado: 'inactive' },
        { id: 38, titulo: 'Jami', usuario:'name',estado: 'active' }
      ],
      search: ''
    }
  },
  methods: {
    searchData() {
      // Aquí puedes realizar la búsqueda en la lista de items utilizando el valor de search
      console.log('Search: ', this.search);
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
