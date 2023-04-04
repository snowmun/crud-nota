import config from '@/config/index';

const loginServices = {

  async userLogin(nombreUsuario) {
    const response = await fetch(`${config.urlApi}/api/v1/buscar_usuario/${nombreUsuario}`);
    const data = await response.json();
    return { code: response.status, data };
  }

};

export default loginServices;