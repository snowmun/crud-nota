from fastapi import APIRouter
from models.datoPersonalModel import DatoPersonal
from provider.db import Database
from script.validaciones import validar_rut
from script.validaciones import rut_existe
from script.validaciones import usuario_existe

router = APIRouter()
db = Database()  # instanciar el objeto de base de datos

@router.get('/api/v1/listar_usuarios')
def listar_usuarios():
    try:
        db.connect()  
        results = db.query("""
            SELECT u.id, u.nombre_usuario, dp.nombre, dp.apellido, dp.email, dp.edad, dp.rut, dp.profesion, c.nombre AS nombre_comuna, r.nombre AS nombre_region
            FROM usuario u
            JOIN dato_personal dp ON u.id_dato_personal = dp.id
            JOIN comuna c ON dp.id_comuna = c.id
            JOIN region r ON c.id_region = r.id """) 
        usuarios = []
        for result in results:
            usuario = {
                "id": result[0],
                "nombre_usuario": result[1],
                "nombre": result[2],
                "apellido": result[3],
                "email": result[4],
                "edad": result[5],
                "rut": result[6],
                "profesion": result[7],
                "nombre_comuna": result[8],
                "nombre_region": result[9]
            }
            usuarios.append(usuario)
        db.disconnect() 
        return usuarios
    except Exception as e:
        db.disconnect()
        return {"mensaje": f"Error al listar los usuarios: {str(e)}"}


@router.get('/api/v1/listar_usuario/{id}')
def listar_usuario(id: int):
    try:
        db.connect() 
        cursor = db.mycursor
        cursor.execute("""
            SELECT u.id, u.nombre_usuario, dp.nombre, dp.apellido, dp.email, dp.edad, dp.rut, dp.profesion, dp.id_comuna, c.id_region,
            c.nombre AS nombre_comuna, r.nombre AS nombre_region
            FROM usuario u
            JOIN dato_personal dp ON u.id_dato_personal = dp.id
            JOIN comuna c ON dp.id_comuna = c.id
            JOIN region r ON c.id_region = r.id
            WHERE u.id = %s """, (id,))
        usuarios = []
        for result in cursor:
            usuario = {
                "id": result[0],
                "nombre_usuario": result[1],
                "nombre": result[2],
                "apellido": result[3],
                "email": result[4],
                "edad": result[5],
                "rut": result[6],
                "profesion": result[7],
                "id_comuna": result[8],
                "id_region": result[9],
                "nombre_comuna": result[10],
                "nombre_region": result[11]
            }
            usuarios.append(usuario)
        db.disconnect() 
        return usuarios
    except Exception as e:
        db.disconnect()
        return {"mensaje": f"Error al listar el usuario: {str(e)}"}

@router.put('/api/v1/actualizar_usuario/{id}')
def actualizar_usuario(id: int, usuario: DatoPersonal):
    db.connect() 
    try:
        if not validar_rut(usuario.rut):
            return {"error": "El RUT ingresado no es válido"}
        
        if rut_existe(usuario.rut, id):
            return {"error": f"El RUT '{usuario.rut}' ya está en uso por otro usuario y no se puede actualizar"}
        
        if usuario_existe(usuario.nombre_usuario, id):
            return {"error": f"El nombre de usuario '{usuario.nombre_usuario}' ya está en uso y no se puede crear el usuario"}

        db.mycursor.execute("""
            UPDATE usuario u 
            JOIN dato_personal dp ON u.id_dato_personal = dp.id
            SET 
                u.nombre_usuario = %s, 
                dp.nombre = %s,
                dp.apellido = %s,
                dp.email = %s,
                dp.edad = %s,
                dp.rut = %s,
                dp.profesion = %s,
                dp.id_comuna = %s
            WHERE u.id = %s
        """, 
        (
            usuario.nombre_usuario, 
            usuario.nombre, 
            usuario.apellido, 
            usuario.email, 
            usuario.edad, 
            usuario.rut, 
            usuario.profesion, 
            usuario.id_comuna, 
            id
        )) 
        db.mydb.commit()  
        return {"mensaje": "Usuario actualizado correctamente"}
    except Exception as e:
        db.mydb.rollback()  
        return {"error": f"Error al actualizar el usuario: {str(e)}"}


@router.post('/api/v1/crear_usuario')
def crear_usuario(usuario: DatoPersonal):
    db.connect()
    try:
        if not validar_rut(usuario.rut):
            return {"error": "El RUT ingresado no es válido"}
        
        if rut_existe(usuario.rut, id= 0):
            return {"error": f"El RUT '{usuario.rut}' ya está en uso por otro usuario y no se puede actualizar"}
        
        if usuario_existe(usuario.nombre_usuario, id= 0):
            return {"error": f"El nombre de usuario '{usuario.nombre_usuario}' ya está en uso y no se puede crear el usuario"}
        
        # Crear el usuario
        db.mycursor.execute("INSERT INTO dato_personal (nombre, apellido, email, edad, rut, profesion, id_comuna) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (usuario.nombre, usuario.apellido, usuario.email, usuario.edad, usuario.rut, usuario.profesion, usuario.id_comuna))
        id_dato_personal = db.mycursor.lastrowid
        db.mycursor.execute("INSERT INTO usuario (nombre_usuario, id_dato_personal) VALUES (%s, %s)", (usuario.nombre_usuario, id_dato_personal))
        db.mydb.commit()
        return {"mensaje": "Usuario creado correctamente"}
    except Exception as e:
        db.mydb.rollback() 
        return {"error": f"Error al crear el usuario: {str(e)}"}

@router.delete('/api/v1/eliminar_usuario/{id}')
def eliminar_usuario(id: int):
    db.connect()
    try:
        db.mycursor.execute("DELETE FROM usuario WHERE id_dato_personal = %s", (id,))
        db.mycursor.execute("DELETE FROM dato_personal WHERE id = %s", (id,))
        db.mydb.commit()
        return {"mensaje": "Datos de usuario eliminados correctamente"}
    except Exception as e:
        db.mydb.rollback() 
        return {"mensaje": f"Error al eliminar los datos de usuario: {str(e)}"}