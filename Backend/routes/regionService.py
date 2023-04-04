from fastapi import APIRouter
from provider.db import Database

router = APIRouter()

db = Database()

@router.get('/api/v1/listar_regiones')
def listar_regiones():
    try:
        db.connect()
        results = db.query("SELECT * FROM region")
        db.disconnect()
        region = []
        for result in results:
            regiones = {
                "id": result[0],
                "nombre": result[1],
            }
            region.append(regiones)
        return region
    except Exception as e:
        raise e
    finally:
        db.disconnect()
        
@router.get('/api/v1/listar_region/{id}')
def listar_region(id: int):
    try:
        db.connect()
        results = db.query("SELECT * FROM region WHERE id = %s" % id)
        region = []
        for result in results:
            regiones = {
                "id": result[0],
                "nombre": result[1],
            }
            region.append(regiones)
        
        db.disconnect()
        return region
    except Exception as e:
        raise e
    finally:
        db.disconnect()