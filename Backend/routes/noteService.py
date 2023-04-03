from fastapi import APIRouter, HTTPException
from provider.db import Database  # importar el módulo de base de datos
from models.noteModel import Nota  # importar el modelo de datos de nota

router = APIRouter()

db = Database()  # instanciar el objeto de base de datos

@router.get('/api/v1/listar_notas')
def listar_notas():
    try:
        db.connect()  # conectarse a la base de datos
        results = db.query("SELECT * FROM nota")  # realizar una consulta SELECT para obtener todas las notas
        notas = []
        for result in results:
            # crear un diccionario para cada nota y agregarlo a la lista de notas
            nota = {
                "id": result[0],
                "titulo": result[1],
                "contenido": result[2],
                "nota_activa": result[3],
                "plazo_maximo": str(result[4]),
                "id_usuario": result[5],
                "categoria_id": result[6]
            }
            notas.append(nota)
        
        return {"notas": notas}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.disconnect()  # cerrar la conexión a la base de datos
    


@router.get('/api/v1/listar_nota/{id}')
def listar_nota(id: int):
    try:
        db.connect() 
        results = db.query("SELECT * FROM nota WHERE id = %s" % id)  # realizar una consulta SELECT para obtener la nota con el ID especificado
        notas = []
        for result in results:
            nota = {
                "id": result[0],
                "titulo": result[1],
                "contenido": result[2],
                "activo": result[3],
                "fecha_termino": str(result[4]),
                "id_usuario": result[5],
                "id_tipo": result[6]
            }
            notas.append(nota)
        return {"nota": notas}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.disconnect()
    
    
@router.put('/api/v1/actualizar_nota/{id}')
def actualizar_nota(id: int, nota: Nota):
    try:
        db.connect() 
        db.mycursor.execute("UPDATE nota SET titulo = %s, contenido = %s, activo = %s, fecha_termino = %s, id_usuario = %s, id_tipo = %s WHERE id = %s", 
                   (nota.titulo, nota.contenido, nota.activo, nota.fecha_termino, nota.id_usuario, nota.id_tipo, id))  # realizar una consulta UPDATE para actualizar la nota con el ID especificado
        db.mydb.commit()  # confirmar los cambios en la base de datos
        return {"mensaje": "Nota actualizada correctamente"}
    except Exception as e:
        db.mydb.rollback()
        raise e
    finally:
        db.disconnect()
    

@router.get('/api/v1/nota_etiqueta/{id}')
def listar_etiqueta(id: int):
    try:
        db.connect()
        results = db.query("SELECT * FROM nota_etiqueta WHERE id_etiqueta = %s", (id,))
        etiqueta = []
        for result in results:
            # Obtener los datos de la nota asociada a cada registro de nota_etiqueta
            noteData = db.query("SELECT * FROM nota WHERE id = %s", (result[1],))
            etiquetas = {
                "id": result[0],
                "id_nota": result[1],
                "id_etiqueta": result[2],
                "nota": noteData[0] if noteData else None
            }
            etiqueta.append(etiquetas)
        return {"etiqueta": etiqueta}
    except Exception as e:
        raise e
    finally:
        db.disconnect()

@router.post('/api/v1/crear_nota')
def crear_nota(nota: Nota):
    try:
        db.connect()
        # Verificar si el título ya existe y está activo
        db.mycursor.execute("SELECT COUNT(*) FROM nota WHERE titulo = %s AND activo = 1", (nota.titulo,))
        result = db.mycursor.fetchone()
        if result[0] > 0:
            # Si el título ya existe, no se puede crear la nota, por lo que se devuelve un mensaje de error
            return {"mensaje": f"El título '{nota.titulo}' ya está en uso y no se puede crear la nota"}

        # Crear la nota
        db.mycursor.execute("INSERT INTO nota (titulo, contenido, activo, fecha_termino, id_usuario, id_tipo) VALUES (%s, %s, %s, %s, %s, %s)",
                            (nota.titulo, nota.contenido, nota.activo, nota.fecha_termino, nota.id_usuario, nota.id_tipo))
        nota_id = db.mycursor.lastrowid
        if nota.etiqueta:
            # Si la nota tiene una etiqueta, se agrega un registro a la tabla nota_etiqueta
            db.mycursor.execute("INSERT INTO nota_etiqueta (id_nota, id_etiqueta) VALUES (%s, %s)", (nota_id, nota.etiqueta))
        db.mydb.commit()
        return {"mensaje": "Nota creada correctamente"}
    except Exception as e:
        db.mydb.rollback()
        raise e
    finally:
        db.disconnect()

@router.delete('/api/v1/eliminar_nota/{id}')
def eliminar_nota(id: int):
    try:
        db.connect()
        # Eliminar las etiquetas asociadas a la nota
        db.mycursor.execute("DELETE FROM nota_etiqueta WHERE id_nota = %s", (id,))
        # Eliminar la nota
        db.mycursor.execute("DELETE FROM nota WHERE id = %s", (id,))
        db.mydb.commit()
        return {"mensaje": "Nota eliminada correctamente"}
    except Exception as e:
        db.mydb.rollback()
        raise e
    finally:
        db.disconnect()
