from fastapi import APIRouter
from provider.db import Database

router = APIRouter()

db = Database()

@router.get('/api/v1/buscar_usuario/{nombreUsuario}')
def buscar_usuario(nombreUsuario: str):
    try:
        db.connect()
        print(nombreUsuario)
        results = db.query("SELECT * FROM usuario WHERE nombre_usuario = %s", (nombreUsuario,))
        usuario = []
        for result in results:
            user = {
                "id": result[0],
                "nombre_usuario": result[1],
            }
            usuario.append(user)
        
        db.disconnect()
        print(usuario)
        return usuario
    except Exception as e:
        raise e
    finally:
        db.disconnect()