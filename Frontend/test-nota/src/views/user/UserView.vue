<template>
  <b-card>
    <div class="d-flex justify-content-between align-items-center">
      <b-button variant="primary" class="mb-3 col-sm-auto mx-sm-2 " @click="createUser" >Crear Usuario</b-button>
        <div class="d-flex">
          <b-input-group class="mb-3 ">
            <b-form-input v-model="search" placeholder="Buscar por rut"/>
            <b-input-group-append>
              <b-button @click="searchData" variant="primary">Buscar</b-button>
            </b-input-group-append>
          </b-input-group>
      </div>
    </div>
    <b-table striped hover stacked="md" :items="items" v-if="!loading" :fields="fieldsTable">
      <template #cell(action)="row">
        <div>
          <b-button size="sm" variant="warning" class="mx-1 my-1" @click="updateUser(row.item.id)">
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
    <b-modal ref="userModal" @hidden="onModalClose">
      <UserModalComponent :user-id="userId"/>
    </b-modal>

  </b-card>
</template>

<script>
import UserModalComponent from'@/components/user/UserModalComponent.vue';
export default {
  name: 'NoteView',
  components: {
    UserModalComponent
  },
  data() {
    return {
      loading: false,
      userId: null,
      fieldsTable: [
        {
          key: 'id',
          label: 'Id',
          sortable: false
        },
        {
          key: 'nombre',
          label: 'nombre',
          sortable: false
        },
        {
          key: 'rut',
          label: 'Rut',
          sortable: false
        },
        {
          key: 'email',
          label: 'correo',
          sortable: false
        },
        {
          key: 'action',
          label: 'Acciones',
          sortable: false
        },
        
      ],
      items: [
        { id: 40, nombre: 'Dickerson', rut:'17790074-5',email: 'correo@gmail.com' },
        { id: 89, nombre: 'Geneva', rut:'17790074-5',email: 'correo@gmail.com' },
        { id: 38, nombre: 'Jami', rut:'17790074-5',email: 'correo@gmail.com' }
      ],
      search: ''
    }
  },
  methods: {
    searchData() {
      // Aquí puedes realizar la búsqueda en la lista de items utilizando el valor de search
      console.log('Search: ', this.search);
    },
    createUser() {
      this.$router.push({
        name: 'userform',
        params: { id: '0', action: 'create' }
      })
    },

    updateUser(id) {
      this.$router.push({
        name: 'userform',
        params: { id, action: 'update' }
      })
    },
    openModal(id) {
      this.userId = id;
      this.$refs.userModal.show();
    },
    onModalClose() {
        this.userId = null;
    }
  }
};
</script>
