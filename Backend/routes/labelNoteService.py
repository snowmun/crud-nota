from fastapi import APIRouter, HTTPException
from provider.db import Database

router = APIRouter()

db = Database()


@router.get('/api/v1/nota_etiqueta/{id}')
def listar_etiqueta(id: int):
    try:
        db.connect()
        results = db.query("SELECT * FROM nota_etiqueta WHERE id = %s" % id)
        db.disconnect()
        etiqueta = []
        for result in results:
            etiquetas = {
                "id": result[0],
                "id_nota": result[1],
                "id_etiqueta": result[2],
            }
            etiqueta.append(etiquetas)
        return {"etiqueta": etiqueta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.disconnect()

@router.get('/api/v1/nota_etiqueta_nombre/{id}')
def nota_etiqueta_nombre(id: int):
    try:
        db.connect()
        results = db.query("SELECT e.id, e.nombre FROM nota_etiqueta nt JOIN etiqueta e ON nt.id_etiqueta = e.id WHERE nt.id_nota = %s LIMIT 1" % id)
        db.disconnect()
        if results:
            result = results[0]
            etiqueta = {"id": result[0], "nombre": result[1]}
            return etiqueta
        else:
            return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.disconnect()