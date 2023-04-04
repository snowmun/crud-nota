import config from '@/config/index';

const typeServices = {
  async typeList() {
    const response = await fetch(`${config.urlApi}/api/v1/listar_tipo`);
    const data = await response.json();
    return { code: response.status, data };
  },
}

export default typeServices;
