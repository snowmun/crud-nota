<template>
  <b-card>
    <div class="d-flex justify-content-between align-items-center">
      <b-button variant="primary" class="mb-3 col-sm-auto mx-sm-2 " @click="createUser" >Crear Usuario</b-button>
      <div class="d-flex col-3">
        <b-input-group class="mb-3 ">
          <b-form-input v-model="search" placeholder="Buscar por nombre de usuario"/>
        </b-input-group>
      </div>
    </div>
    <b-table striped hover stacked="md" :items="userList" v-if="!loading" :fields="fieldsTable" :filter="search">
      <template #cell(action)="row">
        <div>
          <b-button size="sm" variant="warning" class="mx-1 my-1" @click="updateUser(row.item.id)">
            <b-icon-pencil></b-icon-pencil>
          </b-button>
          <b-button size="sm" variant="secondary" class="mx-1 my-1" @click="openModal(row.item.id)">
            <b-icon-eye></b-icon-eye> 
          </b-button>
          <b-button size="sm" variant="danger" class="mx-1 my-1 " @click="destroy(row.item.id)">
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
import UserModalComponent from'@/components/user/UserModalComponent.vue'
import userServices from '@/services/user/userService'

export default {
  name: 'NoteView',
  components: {
    UserModalComponent
  },
  data() {
    return {
      loading: false,
      userId: null,
      userList: null,
      search: '',
      fieldsTable: [
        {
          key: 'index',
          label: '#',
          sortable: false
        },
        {
          key: 'nombre',
          label: 'Nombre',
          sortable: false
        },
        {
          key: 'apellido',
          label: 'Apellido',
          sortable: false
        },
        {
          key: 'nombre_usuario',
          label: 'Nombre de Usuario',
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
    }
  },
  computed: {
    filteredUserListList() {
      return (labelId) => {
        return this.userList.filter(user => user.nombre_usuario === labelId)
      }
    },
  },

  async mounted() {
    this.init()
  },
  
  methods: {
    async init(){
      await this.getUser()
    },

    async getUser(){
      this.loading = true
      await userServices.usersList()
        .then(({code , data}) => {
          if (code == 200){
            this.userList = data.map((nota, index) => ({...nota, index: index + 1}))
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
          userServices.deleteUserById(id)
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
              this.getUser();
            });
        }
      })
    },
  }
};
</script>
