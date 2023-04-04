import config from '@/config/index';

const regionServices = {
  async regionsList() {
    const response = await fetch(`${config.urlApi}/api/v1/listar_regiones`);
    const data = await response.json();
    return { code: response.status, data };
  },

async regionList(id) {
    const response = await fetch(`${config.urlApi}/api/v1/listar_region/${id}`);
    const data = await response.json();
    return { code: response.status, data };
  },

}

export default regionServices;
