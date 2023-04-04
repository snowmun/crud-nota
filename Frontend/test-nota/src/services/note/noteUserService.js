import config from '../../config/index';

const noteUserServices = {
  async noteUserList(id) {
    const response = await fetch(`${config.urlApi}/api/v1/listar_nota_usuario/${id}`);
    const data = await response.json();
    return { code: response.status, data };
  },
};

export default noteUserServices;
