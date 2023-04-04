import config from '../../config/index';

const labelServices = {
  async labelsList() {
    const response = await fetch(`${config.urlApi}/api/v1/listar_etiquetas`);
    const data = await response.json();
    return { code: response.status, data };
  },

  async labelList(id) {
    const response = await fetch(`${config.urlApi}/api/v1/listar_etiqueta/${id}`);
    const data = await response.json();
    return { code: response.status, data };
  },

  async createLabel({ form }) {
    const response = await fetch(`${config.urlApi}/api/v1/crear_etiqueta`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form)
    });
    const data = await response.json();
    return { code: response.status, data };
  },

  async updateLabel({ form }) {
    const response = await fetch(`${config.urlApi}/api/v1/actualizar_etiqueta/${form.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form)
    });
  
    const data = await response.json();
    return { code: response.status, data };
    
  },

  async deleteLabelById(id) {
    const response = await fetch(`${config.urlApi}/api/v1/eliminar_etiqueta/${id}`, {
      method: 'DELETE'
    });
    const data = await response.json();
    return { code: response.status, data };

  }
};

export default labelServices;