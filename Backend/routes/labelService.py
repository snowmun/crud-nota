from fastapi import APIRouter
from provider.db import Database
from models.labelModel import Etiqueta

router = APIRouter()

db = Database()

@router.get('/api/v1/listar_etiquetas')
def listar_etiquetas():
    try:
        db.connect()
        results = db.query("SELECT * FROM etiqueta")
        db.disconnect()
        etiqueta = []
        for result in results:
            etiquetas = {
                "id": result[0],
                "nombre": result[1],
            }
            etiqueta.append(etiquetas)
        return etiqueta
    except Exception as e:
        raise e
    finally:
        db.disconnect()

@router.get('/api/v1/listar_etiqueta/{id}')
def listar_etiqueta(id: int):
    try:
        db.connect()
        results = db.query("SELECT * FROM etiqueta WHERE id = %s" % id)
        etiqueta = []
        for result in results:
            etiquetas = {
                "id": result[0],
                "nombre": result[1],
            }
            etiqueta.append(etiquetas)
        
        db.disconnect()
        return etiqueta
    except Exception as e:
        raise e
    finally:
        db.disconnect()

@router.put('/api/v1/actualizar_etiqueta/{id}')
def actualizar_etiqueta(id: int, etiqueta: Etiqueta):
    try:
        db.connect()
        db.mycursor.execute("UPDATE etiqueta SET nombre = %s WHERE id = %s", 
                   (etiqueta.nombre, id))
        db.mydb.commit()
        db.disconnect()
        return {"mensaje": "Etiqueta actualizada correctamente"}
    except Exception as e:
        db.mydb.rollback()
        raise e
    finally:
        db.disconnect()

@router.post('/api/v1/crear_etiqueta')
def crear_etiqueta(etiqueta: Etiqueta):
    try:
        db.connect()
        # Verificar si el nombre ya existe
        db.mycursor.execute("SELECT COUNT(*) FROM etiqueta WHERE nombre = %s ", (etiqueta.nombre,))
        result = db.mycursor.fetchone()
        if result[0] > 0:
            db.disconnect()
            return {"mensaje": f"El título '{etiqueta.nombre}' ya está en uso y no se puede crear la etiqueta"}

        # Crear la etiqueta
        db.mycursor.execute("INSERT INTO etiqueta (nombre) VALUES (%s)",
                        (etiqueta.nombre,))
        db.mydb.commit()
        db.disconnect()
        return {"mensaje": "etiqueta creada correctamente"}
    except Exception as e:
        db.mydb.rollback()
        raise e
    finally:
        db.disconnect()

@router.delete('/api/v1/eliminar_etiqueta/{id}')
def eliminar_etiqueta(id: int):
    try:
        db.connect()
        # Eliminar las etiquetas asociadas con nota_etiqueta
        db.mycursor.execute("DELETE FROM nota_etiqueta WHERE id_etiqueta = %s", (id,))
        
        # Eliminar la etiqueta
        db.mycursor.execute("DELETE FROM etiqueta WHERE id = %s", (id,))
        db.mydb.commit()
        db.disconnect()
        return {"mensaje": "Etiqueta eliminada correctamente"}
    except Exception as e:
        db.mydb.rollback()
        raise e
    finally:
        db.disconnect()
