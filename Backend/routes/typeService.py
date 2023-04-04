from fastapi import APIRouter, HTTPException
from provider.db import Database  # importar el módulo de base de datos
from models.noteModel import Nota  # importar el modelo de datos de nota

router = APIRouter()

db = Database()  # instanciar el objeto de base de datos

@router.get('/api/v1/listar_tipo')
def listar_tipo():
    try:
        db.connect()  # conectarse a la base de datos
        results = db.query("SELECT * FROM tipo")
        tipos = []
        for result in results:
            # crear un diccionario para cada nota y agregarlo a la lista de notas
            tipo = {
                "id": result[0],
                "nombre": result[1],
            }
            tipos.append(tipo)
        
        return tipos
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.disconnect()  # cerrar la conexión a la base de datos