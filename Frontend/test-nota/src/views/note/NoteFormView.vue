<template>
    <b-container class="mt-5">
      <b-row justify="center">
        <b-col sm="12" md="8">
          <b-card>
            <h3 v-if="selectedAction == 'create'" justify="center">Crear Nota</h3>
            <h3 v-else>Editar Nota</h3>
            <b-form @submit.prevent="save" v-if="show">
              <b-form-group label="Titulo" class="mr-3">
                <b-form-input v-model="form.titulo" placeholder="Ej: 'Arreglar Pc'" />
              </b-form-group>
              <b-form-group label="Contenido">
                <b-form-textarea v-model="form.contenido" placeholder="Ej: 'Esta es una descripcion'" />
              </b-form-group>
              <b-form-group label="¿La nota está actualmente activa?">
                <b-form-radio-group v-model="form.radioValue">
                  <b-form-radio value="true">Si</b-form-radio>
                  <b-form-radio value="false">No</b-form-radio>
                </b-form-radio-group>
              </b-form-group>
              <b-row>
                <b-col sm="12" md="6">
                  <b-form-group label="Realizar antes del:">
                    <b-form-datepicker v-model="form.fecha" placeholder="Ej: 'dd/mm/yyyy'" />
                  </b-form-group>
                </b-col>
                <b-col sm="12" md="6">
                  <b-form-group label="Asignar Usuario">
                    <b-form-select v-model="form.usuario" :options="usuarios" value-field="id" text-field="nombre" placeholder="Seleccione un usuario" class="custom-select">
                      <template #first>
                        <b-form-select-option :value="null" disabled>Seleccione un usuario</b-form-select-option>
                      </template>
                    </b-form-select>
                  </b-form-group>
                  <b-form-group label="Asignar etiqueta">
                    <b-form-select v-model="form.etiqueta" :options="etiquetas" value-field="id" text-field="nombre" placeholder="Seleccione una etiqueta" class="custom-select">
                      <template #first>
                        <b-form-select-option :value="null" disabled>Seleccione una etiquetas</b-form-select-option>
                      </template>
                    </b-form-select>
                  </b-form-group>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  <b-button type="submit" variant="success" class="mt-3 btn-guardar">
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
export default {
    name: 'NoteForm',
    data() {
        return {
        loading: false,
        show: true,
        selectedAction: null,
        form: {
            titulo: null,
            contenido: null,
            radioValue: null,
            fechaTermino: new Date(),
            usuario: null,
            etiqueta: null
        },
        usuarios: [
            { id: 1, nombre: 'Juan' },
            { id: 2, nombre: 'Pedro' },
            { id: 3, nombre: 'María' },
            { id: 4, nombre: 'Ana' }
        ],
        etiquetas: [
            { id: 1, nombre: 'pan' },
            { id: 2, nombre: 'verdura' },
            { id: 3, nombre: 'juguito' },
            { id: 4, nombre: 'electronica' }
        ]
        };
    },
    mounted() {
    this.init();
    },
    methods: {
        submitForm() {
        console.log(this.form);
        },
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
        async getElement(notaId) {
            console.log(notaId)
            // this.loading = true
            // hacer peticion para obtener el elemento
            // await this.getArea({ id: AreaId })
                // .then(() => {
                // this.form = this.selectedArea
                // })
                // .catch((error) => {
                // console.error({ error })
                // })
                // .finally(() => {
                // this.loading = false
                // })
        },
        save(event) {
        event.preventDefault()
        //   hacer peticion fetch para editar o crear
        //   if (this.form.name.length > 0) {
            // if (this.selectedAction === 'update') {
            //   this.loading = true
            //   this.updateArea({ form: this.form })
            //     .then(({ error, errors }) => {
            //       if (!error) {
            //         this.$toast.success('Se actualiza correctamente')
            //         this.back()
            //       } else {
            //         const mensaje = errors[0].message
            //         this.$toast.warning(`Error Al Actualizar: ${mensaje}`)
            //       }
            //     })
            //     .catch(() => {
            //       this.$toast.error('Error al Actualizar')
            //     })
            //     .finally(() => {
            //       this.loading = false
            //     })
            // } else if (this.selectedAction === 'create') {
            //   this.loading = true
            //   this.createArea({ form: this.form })
            //     .then(({ error, errors }) => {
            //       if (!error) {
            //         this.$toast.success('Se crea correctamente')
            //         this.back()
            //       } else {
            //         const mensaje = errors[0].message
            //         this.$toast.warning(`Error Al crear: ${mensaje}`)
            //       }
            //     })
            //     .catch(() => {
            //       this.$toast.error('Error al crear')
            //     })
            //     .finally(() => {
            //       this.loading = false
            //     })
            // }
        //   } else {
        //     this.$toast.warning('Debe ingresar un nombre de Área')
        //     this.loading = false
        //   }
        },
        clearForm() {
            this.form.titulo = null;
            this.form.contenido = null;
            this.form.radioValue = null;
            this.form.fecha = new Date();
            this.form.usuario = null;
        },
        back() {
            this.$router.push({
                name: 'note',
            })
        }
    }
}
  </script>
<style scoped>
    .btn-guardar{
        margin-right: 1rem;
    }
    .btn-limpiar{
        margin-right: 1rem;
    }

</style>