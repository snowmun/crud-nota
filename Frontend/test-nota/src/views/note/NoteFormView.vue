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
            <b-form-group label="Asignar tipo de emergencia">
              <b-form-select v-model="form.id_tipo" :options="typeList" value-field="id" text-field="nombre" placeholder="Seleccione una etiqueta" class="custom-select">
                <template #first>
                  <b-form-select-option :value="null" disabled>Seleccione una etiquetas</b-form-select-option>
                </template>
              </b-form-select>
            </b-form-group>
            <b-form-group label="¿La nota está actualmente activa?">
              <b-form-radio-group v-model="form.activo" @change="form.activo = parseInt(form.activo)">
                <b-form-radio value="1">Si</b-form-radio>
                <b-form-radio value="0">No</b-form-radio>
              </b-form-radio-group>
            </b-form-group>
            <b-row>
              <b-col sm="12" md="6">
                <b-form-group label="Realizar antes del:">
                  <b-form-datepicker v-model="form.fecha_termino" placeholder="Ej: 'dd/mm/yyyy'" />
                </b-form-group>
              </b-col>
              <b-col sm="12" md="6">
                <b-form-group label="Asignar Usuario">
                  <b-form-select v-model="form.id_usuario" :options="userList" value-field="id" text-field="nombre" placeholder="Seleccione un usuario" class="custom-select">
                    <template #first>
                      <b-form-select-option :value="null" disabled>Seleccione un usuario</b-form-select-option>
                    </template>
                  </b-form-select>
                </b-form-group>
                <b-form-group label="Asignar etiqueta">
                  <b-form-select v-model="form.id_etiqueta" :options="lebelList" value-field="id" text-field="nombre" placeholder="Seleccione una etiqueta" class="custom-select">
                    <template #first>
                      <b-form-select-option :value="null" disabled>Seleccione una etiquetas</b-form-select-option>
                    </template>
                  </b-form-select>
                </b-form-group>
              </b-col>
            </b-row>
            <b-row>
              <b-col>
                <b-button variant="success" class="mt-3 btn-guardar" @click="saveNote">
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
import noteServices from '@/services/note/noteService'
import userServices from '@/services/user/userService'
import labelService from '@/services/label/labelService'
import typeService from '@/services/type/typeService'
import '@/assets/css/general.css';

export default {
  name: 'NoteForm',
  data() {
    return {
      loading: false,
      show: true,
      selectedAction: null,
      userList: null,
      lebelList: null,
      typeList: null,
      form: {
          titulo: null,
          contenido: null,
          activo : null,
          fecha_termino: new Date(),
          id_usuario: null,
          id_etiqueta:null,
          id_tipo: null
      },
    };
  },
    
  mounted() {
    this.init();
  },

  methods: {

    async init() {
      this.prepareData()
      this.getUsers()
      this.getLabels()
      this.getType()
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
      await noteServices.noteList(id)
        .then(({code , data}) => {
          if (code == 200){
            // se agrega la propiedad index a cada objeto en notaList
            this.form = data.nota[0]
            this.$toasted.success('Notas cargadas correctamente')
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

    async getUsers(){
      await userServices.usersList()
        .then(({code , data}) => {
          if (code == 200){
            this.userList = data
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

    async getType(){
      await typeService.typeList()
        .then(({code , data}) => {
          if (code == 200){
            this.typeList = data
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
    
    async saveNote() {
      if (this.selectedAction === 'update') {
        this.loading = true
        await noteServices.updateNote({ form: this.form })
          .then(({code}) => {
            if (code == 200) {
              this.$toasted.success('Se actualiza correctamente')
              this.back()
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
        await noteServices.createNote({ form: this.form })
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
