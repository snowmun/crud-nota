<template>
  <b-container class="mt-5">
    <b-row justify="center">
      <b-col sm="12" md="8">
        <b-card>
          <h3 v-if="selectedAction == 'create'" justify="center">Crear Etiqueta</h3>
          <h3 v-else>Editar Etiqueta</h3>
          <b-form >
            <b-form-group label="Nombre" class="mr-3">
              <b-form-input v-model="form.nombre" placeholder="Ej: 'computadores'" />
            </b-form-group>
            <b-row>
              <b-col>
                <b-button type="submit" variant="success" class="mt-3 btn-guardar" @click="saveLabels">
                  <b-spinner small v-if="loading"></b-spinner>
                  <span v-else>Guardar</span>
                </b-button>
                <b-button variant="warning" class="mt-3 btn-limpiar" @click="clearForm">Limpiar</b-button>
                <b-button variant="danger" @click="() => back()" class="mt-3 ">Cancelar</b-button>
              </b-col>
            </b-row>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>
  
  
<script>
import labelService from '@/services/label/labelService'
import '@/assets/css/general.css';

export default {
  name: 'LabelForm',
  data() {
    return {
      loading: false,
      show: true,
      selectedAction: null,
      form: {
          nombre: null,
      },
    };
  },

  mounted() {
      this.init();
  },

  methods: {

    init() {
        this.prepareData()
    },

    prepareData() {
      const { params } = this.$route
      if (params && params.action) {
          const { id, action } = params
          this.selectedAction = action
          if (params.action !== 'create') this.getElement(id)
      }
    },

    async getElement(id) {
        this.loading = true
        await labelService.labelList(id)
          .then(({code, data}) => {
            if (code == 200){
              this.form = data[0]
            }
          })
          .catch((error) => {
            console.error({ error })
          })
          .finally(() => {
            this.loading = false
          })
    },

    async saveLabels() {
      if (this.selectedAction === 'update') {
        this.loading = true
        await labelService.updateLabel({ form: this.form })
          .then(({ error, errors }) => {
            if (!error) {
              this.$toasted.success('Se actualiza correctamente')
              this.back()
            } else {
              const mensaje = errors[0].message
              this.$toasted.warning(`Error Al Actualizar: ${mensaje}`)
            }
          })
          .catch(() => {
            this.$toasted.error('Error al Actualizar')
          })
          .finally(() => {
            this.loading = false
          })
      } else if (this.selectedAction === 'create') {
        this.loading = true
        await labelService.createLabel({ form: this.form })
          .then(({code}) => {
            if (code == 200) {
              this.$toasted.success('Se crea correctamente')
              this.back()
            } else {
              this.$toasted.warning(`error del servidor al crear`)
            }
          })
          .catch(() => {
            this.$toast.error('Error al crear')
          })
          .finally(() => {
            this.loading = false
          })
      }
    },

    clearForm() {
      this.form.nombre = null;
    },

    back() {
      this.$router.push({
          name: 'label',
      })
    }
  }
}
  </script>