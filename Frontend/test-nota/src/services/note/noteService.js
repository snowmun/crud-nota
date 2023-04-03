import config from '../../config/index';

const noteServices = {
  async notesList() {
    const response = await fetch(`${config.urlApi}/api/v1/listar_notas`);
    const data = await response.json();
    return { code: response.status, data };
  },

  async createNote({ titulo, contenido, nombre_usuario, tipo_emergencia, end_date }) {
    const response = await fetch(`${config.urlApi}/api/v1/crear_nota`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ titulo, contenido, nombre_usuario, tipo_emergencia, end_date })
    });
    const data = await response.json();
    return { code: response.status, data };
  },

  async updateNote({ id, titulo, contenido, nombre_usuario, tipo_emergencia, end_date }) {
    const response = await fetch(`${config.urlApi}/api/v1/actualizar_nota/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ titulo, contenido, nombre_usuario, tipo_emergencia, end_date })
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

  