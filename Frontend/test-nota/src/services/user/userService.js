import config from '@/config/index';

const userServices = {

  async usersList() {
    const response = await fetch(`${config.urlApi}/api/v1/listar_usuarios`);
    const data = await response.json();
    return { code: response.status, data };
  },

  async userList(id) {
    const response = await fetch(`${config.urlApi}/api/v1/listar_usuario/${id}`);
    const data = await response.json();
    return { code: response.status, data };
  },


  async updateUser({ form }) {
    const response = await fetch(`${config.urlApi}/api/v1/actualizar_usuario/${form.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form)
    });
  
    const data = await response.json();
    return { code: response.status, data };
  },

  async createUser({ form }) {
    const response = await fetch(`${config.urlApi}/api/v1/crear_usuario`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form)
    });
    const data = await response.json();
    return { code: response.status, data };
  },

  async deleteUserById(id) {
    const response = await fetch(`${config.urlApi}/api/v1/eliminar_usuario/${id}`, {
      method: 'DELETE'
    });
    const data = await response.json();
    return { code: response.status, data };
  }

};

export default userServices;