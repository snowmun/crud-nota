import config from '../../config/index';

const noteServices = {
  async notesList() {
    const response = await fetch(`${config.urlApi}/api/v1/listar_notas`);
    const data = await response.json();
    return { code: response.status, data };
  },

  async noteList(id) {
    const response = await fetch(`${config.urlApi}/api/v1/listar_nota/${id}`);
    const data = await response.json();
    return { code: response.status, data };
  },

  async createNote({ form }) {
    const response = await fetch(`${config.urlApi}/api/v1/crear_nota`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form)
    });
    const data = await response.json();
    return { code: response.status, data };
  },

  async updateNote({ form }) {
    const response = await fetch(`${config.urlApi}/api/v1/actualizar_nota/${form.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form)
    });
  
    const data = await response.json();
    return { code: response.status, data };
    
  },

  async deleteNoteById(id) {
    const response = await fetch(`${config.urlApi}/api/v1/eliminar_nota/${id}`, {
      method: 'DELETE'
    });
    const data = await response.json();
    return { code: response.status, data };

  }
};

export default noteServices;

  