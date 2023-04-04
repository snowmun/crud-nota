import config from '@/config/index';

const comunneServices = {

  async communesList() {
    const response = await fetch(`${config.urlApi}/api/v1/listar_comunas`);
    const data = await response.json();
    return { code: response.status, data };
  },

async comuneList(id) {
    const response = await fetch(`${config.urlApi}/api/v1/listar_comuna/${id}`);
    const data = await response.json();
    return { code: response.status, data };
  },

}

export default comunneServices;
