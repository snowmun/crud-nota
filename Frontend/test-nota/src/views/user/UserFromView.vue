<template>
    <b-container class="mt-5">
      <b-row justify="center">
        <b-col sm="12" md="8">
          <b-card>
            <h3 v-if="selectedAction == 'create'" justify="center">Crear Nota</h3>
            <h3 v-else>Editar Usuario</h3>
            <b-form @submit.prevent="save" v-if="show">
              <b-form-group label="Nombre" class="mr-3">
                <b-form-input v-model="form.nombre" placeholder="Ingrese su nombre" />
              </b-form-group>
              <b-form-group label="Apellido" class="mr-3">
                <b-form-input v-model="form.apellido" placeholder="Ingrese su apellido" />
              </b-form-group>
              <b-form-group label="Edad" class="mr-3">
                <b-form-input type="number" v-model="form.edad" placeholder="Ingrese su edad" />
              </b-form-group>
              <b-form-group label="RUT" class="mr-3">
                <b-form-input v-model="form.rut" placeholder="Ingrese su RUT" />
              </b-form-group>
              <b-form-group label="Email" class="mr-3">
                <b-form-input v-model="form.email" placeholder="Ingrese su email" />
              </b-form-group>
              <b-form-group label="Profesión" class="mr-3">
                <b-form-input v-model="form.profesion" placeholder="Ingrese su profesión" />
              </b-form-group>
              <b-form-group label="Región">
                <b-form-select v-model="form.region" :options="regiones" value-field="id" text-field="nombre" placeholder="Seleccione una región" class="custom-select" @change="getComunas">
                  <template #first>
                    <b-form-select-option :value="null" disabled>Seleccione una región</b-form-select-option>
                  </template>
                </b-form-select>
              </b-form-group>
              <b-form-group label="Comuna" >
                <b-form-select v-model="form.comuna"  :options="comunas" value-field="id" text-field="nombre" placeholder="Seleccione una comuna" class="custom-select">
                  <template #first>
                    <b-form-select-option :value="null" disabled>Seleccione una comuna</b-form-select-option>
                  </template>
                </b-form-select>
              </b-form-group>
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
    name: 'userForm',
    data() {
        return {
            loading: false,
            show: true,
            selectedAction: null,
            form: {
                nombre: null,
                apellido: null,
                edad: null,
                rut: null,
                email: null,
                profesion: null,
                region: null,
                comuna: null,
            },
            regiones: [],
            comunas: [],
        };
    },
    created() {
        this.getRegiones();
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
        async getRegiones() {
            try {
                const response = await fetch('https://apis.digital.gob.cl/dpa/regiones');
                const data = await response.json();
                this.regiones = data;
            } catch (error) {
                console.error(error);
            }
        },
        async getComunas() {
            try {
                const response = await fetch(`https://apis.digital.gob.cl/dpa/regiones/${this.form.region.id}/comunas`);
                const data = await response.json();
                this.comunas = data;
            } catch (error) {
                console.error(error);
            }
        },
        clearForm() {
            this.form.nombre = null;
            this.form.apellido = null;
            this.form.edad = null;
            this.form.rut = null;
            this.form.email = null;
            this.form.profesion = null;
            this.form.region = null;
            this.form.comuna = null;
        },
        back() {
            this.$router.push({
                name: 'user',
            })
        },
    },
};
</script>