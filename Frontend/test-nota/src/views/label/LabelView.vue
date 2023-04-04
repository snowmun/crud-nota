<template>
  <b-card>
    <div class="d-flex justify-content-between align-items-center">
      <b-button variant="primary" class="mb-3 col-sm-auto mxel-sm-2 " @click="createLabel" >Crear Etiqueta</b-button>
    </div>
    <b-table striped hover stacked="md" :items="lebelList" v-if="!loading" :fields="fieldsTable">
      <template #cell(action)="row">
        <div>
          <b-button size="sm" variant="warning" class="mx-1 my-1" @click="updateLabel(row.item.id)">
            <b-icon-pencil></b-icon-pencil>
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
  </b-card>
</template>

<script>
import labelService from '@/services/label/labelService'

export default {
  name: 'labelView',
  data() {
    return {
      loading: false,
      lebelList: null,
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
    }
  },

  mounted() {
    this.init()
  },

  methods: {

    async init() {
      this.getLabels()
    },

    async getLabels(){
      await labelService.labelsList()
        .then(({code , data}) => {
          if (code == 200){
            this.lebelList = data
            this.$toasted.success('Etiquetas encontradas')
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
          labelService.deleteLabelById(id)
            .then(({code}) => {
              if (code == 200){
                this.$toasted.success('Etiqueta eliminada con exito')
              } else {
                this.$toasted.warning('error en el servidor al eliminar ');
              }
            })
            .catch(() => {
              this.$toasted.error('Error al eliminar');
            })
            .finally(() => {
              this.getLabels();
            });
        }
      })
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
