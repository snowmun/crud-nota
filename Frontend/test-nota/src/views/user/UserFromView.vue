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
              <b-form-group label="Nombre de Usuario" class="mr-3">
                <b-form-input v-model="form.nombre_usuario" placeholder="Ingrese su nombre de usuario" />
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
                <b-form-select v-model="form.id_region" :options="regionList" value-field="id" text-field="nombre" placeholder="Seleccione una región" class="custom-select" @change="getComunas">
                  <template #first>
                    <b-form-select-option :value="null" disabled>Seleccione una región</b-form-select-option>
                  </template>
                </b-form-select>
              </b-form-group>
              <b-form-group label="Comuna" >
                <b-form-select v-model="form.id_comuna"  :options="communeList" value-field="id" text-field="nombre" placeholder="Seleccione una comuna" class="custom-select">
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
import userServices from '@/services/user/userService'
import regionServices from '@/services/region/regionService'
import comunneServices from '@/services/commune/communeService'

export default {
  name: 'userForm',
  data() {
      return {
          loading: false,
          show: true,
          selectedAction: null,
          userList: null,
          form: {
              nombre: null,
              apellido: null,
              nombre_usuario: null,
              edad: null,
              rut: null,
              email: null,
              profesion: null,
              id_region: null,
              id_comuna: null,
          },
          regionList: [],
          communeList: [],
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
    async getElement(id) {
      this.loading = true
      await userServices.userList(id)
      .then(({code , data}) => {
        if (code == 200){
          this.form = data[0]
          this.getComunas()
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
    async save(event) {
      event.preventDefault()
      if (this.selectedAction === 'update') {
        this.loading = true
        await userServices.updateUser({ form: this.form })
          .then(({ code, data }) => {
            console.log(code==200 && !data.error)
            if (code==200 && !data.error) {
              this.$toasted.success('Se actualiza correctamente')
              this.back()
            } else {
              this.$toasted.error(`No se pudo actualizar: ${data.error}`)
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
        await userServices.createUser({ form: this.form })
          .then(({ code, data }) => {
            console.log(code==200 && !data.error)
            if (code==200 && !data.error) {
              this.$toasted.success('Se actualiza correctamente')
              this.back()
            } else {
              this.$toasted.error(`No se pudo actualizar: ${data.error}`)
            }
          })
          .catch(() => {
            this.$toasted.error('Error al Actualizar')
          })
          .finally(() => {
            this.loading = false
          })
      }
    },
    async getRegiones() {
      this.loading = true
      await regionServices.regionsList()
      .then(({code , data}) => {
        if (code == 200){
          this.regionList = data
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
    async getComunas() {
      this.loading = true
      await comunneServices.comuneList(this.form.id_region)
      .then(({code , data}) => {
        if (code == 200){
          this.communeList = data
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

    
    clearForm() {
        this.form.nombre = null;
        this.form.apellido = null;
        this.form.edad = null;
        this.form.rut = null;
        this.form.email = null;
        this.form.profesion = null;
        this.form.id_region = null;
        this.form.id_comuna = null;
    },
    back() {
        this.$router.push({
            name: 'user',
        })
    },
  },
};
</script>
<style scoped>
    .btn-guardar{
        margin-right: 1rem;
    }
    .btn-limpiar{
        margin-right: 1rem;
    }

</style>