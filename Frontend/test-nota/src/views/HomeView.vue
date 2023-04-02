<template>
  <b-card>
    <h3 class="text-center">Todas las Notas</h3>
    <div class="table-responsive">
      <b-table striped hover stacked="md" :items="items" v-if="!loading" :fields="fieldsTable" class="margin-top__20">
        <template #cell(action)>
          <div class="d-flex justify-content-center">
            <b-button size="sm" variant="outline-primary" class="mr-2 custom-button">
              <b-icon-pencil></b-icon-pencil>
            </b-button>
            <b-button size="sm" variant="outline-primary" class="mr-2 custom-button">
              <b-icon-eye></b-icon-eye>
            </b-button>
            <b-button size="sm" variant="danger" class="custom-button">
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
    </div>
  </b-card>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      loading: false,
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
          key: 'end_date',
          label: 'Fecha Termino',
          sortable: false
        },
      ],
      items: [
        { id: 40, titulo: 'Dickerson', usuario:'name',estado: 'active', end_date: '2023-04-01' },
        { id: 21, titulo: 'Larsen', usuario:'name',estado: 'active', end_date: '2023-04-01' },
        { id: 89, titulo: 'Geneva', usuario:'name',estado: 'inactive', end_date: '2023-04-01'  },
        { id: 38, titulo: 'Jami', usuario:'name',estado: 'active', end_date: '2023-04-01'  }
      ]
    }
  },
};
</script>

<style scoped>
.custom-button {
  border: 1px solid #dee2e6;
  border-radius: 5px;
  padding: 0.5rem 1rem;
}
.table-responsive {
  overflow-x: auto;
}
</style>