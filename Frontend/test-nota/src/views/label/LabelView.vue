<template>
  <b-card>
    <div class="d-flex justify-content-between align-items-center">
      <b-button variant="primary" class="mb-3 col-sm-auto mxel-sm-2 " @click="createLabel" >Crear Etiqueta</b-button>
        <div class="d-flex">
          <b-input-group class="mb-3 ">
            <b-form-input v-model="search" placeholder="Buscar por nombre"/>
            <b-input-group-append>
              <b-button @click="searchData" variant="primary">Buscar</b-button>
            </b-input-group-append>
          </b-input-group>
    </div>
    </div>
      <b-table striped hover stacked="md" :items="items" v-if="!loading" :fields="fieldsTable">
        <template #cell(action)="row">
          <div>
            <b-button size="sm" variant="warning" class="mx-1 my-1" @click="updateLabel(row.item.id)">
              <b-icon-pencil></b-icon-pencil>
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
  </b-card>
</template>

<script>
export default {
  name: 'NoteView',
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
          key: 'nombre',
          label: 'Nombre',
          sortable: false
        },
        {
          key: 'action',
          label: 'Acciones',
          sortable: false
        },
        
      ],
      items: [
        { id: 40, nombre: 'Dickerson' },
        { id: 21, nombre: 'Larsen'},
        { id: 89, nombre: 'Geneva' },
        { id: 38, nombre: 'Jami'}
      ],
      search: ''
    }
  },
  methods: {
    searchData() {
      // Aquí puedes realizar la búsqueda en la lista de items utilizando el valor de search
      console.log('Search: ', this.search);
    },
    createLabel() {
      this.$router.push({
        name: 'labelform',
        params: { id: '0', action: 'create' }
      })
    },

    updateLabel(id) {
      this.$router.push({
        name: 'labelform',
        params: { id, action: 'update' }
      })
    },
  }
};
</script>
