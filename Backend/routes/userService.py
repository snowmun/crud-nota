from fastapi import APIRouter
from models.datoPersonalModel import DatoPersonal
from provider.db import Database
from script.validateRut import validar_rut

router = APIRouter()
db = Database()  # instanciar el objeto de base de datos

@router.get('/api/v1/listar_usuarios')
def listar_usuarios():
    try:
        db.connect()  
        results = db.query("""
            SELECT u.id, u.nombre_usuario, dp.nombre, dp.apellido, dp.email, dp.edad, dp.rut, dp.profesion, dp.id_comuna
            FROM usuario u
            JOIN dato_personal dp ON u.id_dato_personal = dp.id """) 
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
                "id_comuna": result[8],
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
            SELECT u.id, u.nombre_usuario, dp.nombre, dp.apellido, dp.email, dp.edad, dp.rut, dp.profesion, dp.id_comuna, c.id_region
            FROM usuario u
            JOIN dato_personal dp ON u.id_dato_personal = dp.id
            JOIN comuna c ON dp.id_comuna = c.id
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
                "id_region": result[9]
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
        return {"mensaje": f"Error al actualizar el usuario: {str(e)}"}

@router.post('/api/v1/crear_usuario')
def crear_usuario(usuario: DatoPersonal):
    db.connect()
    try:
        # Validar el RUT antes de guardar los datos
        if not validar_rut(usuario.rut):
            return {"mensaje": "El RUT ingresado no es válido"}
        
        # Verificar si ya existe un usuario con el mismo RUT
        db.mycursor.execute("SELECT COUNT(*) FROM dato_personal WHERE rut = %s ", (usuario.rut,))
        result = db.mycursor.fetchone()
        if result[0] > 0:
            return {"mensaje": "Ya existe un usuario con el mismo RUT"}
        
        # Verificar si el nombre de usuario ya existe 
        db.mycursor.execute("SELECT COUNT(*) FROM usuario WHERE nombre_usuario = %s ", (usuario.nombre_usuario,))
        result = db.mycursor.fetchone()
        if result[0] > 0:
            return {"mensaje": f"El nombre de usuario '{usuario.nombre_usuario}' ya está en uso y no se puede crear el usuario"}
        
        # Crear el usuario
        db.mycursor.execute("INSERT INTO dato_personal (nombre, apellido, email, edad, rut, profesion, id_comuna) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (usuario.nombre, usuario.apellido, usuario.email, usuario.edad, usuario.rut, usuario.profesion, usuario.id_comuna))
        id_dato_personal = db.mycursor.lastrowid
        db.mycursor.execute("INSERT INTO usuario (nombre_usuario, id_dato_personal) VALUES (%s, %s)", (usuario.nombre_usuario, id_dato_personal))
        db.mydb.commit()
        return {"mensaje": "Usuario creado correctamente"}
    except Exception as e:
        db.mydb.rollback() 
        return {"mensaje": f"Error al crear el usuario: {str(e)}"}

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