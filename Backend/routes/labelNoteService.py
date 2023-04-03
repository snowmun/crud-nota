from fastapi import APIRouter
from provider.db import Database
from models.labelModel import Etiqueta
from fastapi.responses import JSONResponse

router = APIRouter()

db = Database()


@router.get('/api/v1/nota_etiqueta/{id}')
def listar_etiqueta(id: int):
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
