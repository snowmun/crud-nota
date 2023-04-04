import re
from provider.db import Database

db = Database() 

def validar_rut(rut):
    # Patrón de expresión regular para validar el RUT. Permite 7 u 8 dígitos seguidos de un guión y un dígito o letra K
    rut_regex = r'^\d{7,8}[-][0-9kK]{1}$'
    if not re.match(rut_regex, rut):
        return False
    # Eliminar puntos del RUT y dividir en número y dígito verificador
    rut = rut.replace('.', '')
    rut = rut.split('-')
    verificador = rut[1]
    numero = rut[0]
    revertido = numero[::-1] # Revertir el número para empezar por los dígitos menos significativos
    factor = 2
    suma = 0
    # Multiplicar cada dígito por un factor y sumar los resultados
    for i in revertido:
        suma += int(i) * factor
        factor += 1
        if factor == 8:
            factor = 2
    dv = 11 - (suma % 11) # Calcular el dígito verificador
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = 'K'
    else:
        dv = str(dv)
    # Comparar el dígito verificador calculado con el ingresado y retornar verdadero o falso según corresponda
    if dv.upper() == verificador.upper():
        return True
    else:
        return False
    
def usuario_existe(nombre_usuario: str, id: int  ):
    db.connect()
    result = ('',)
    if id != 0:
        db.mycursor.execute("""
            SELECT u.nombre_usuario
            FROM usuario u 
            JOIN dato_personal dp ON u.id_dato_personal = dp.id
            WHERE u.id = %s
        """, (id,))
        result = db.mycursor.fetchone()

    if result[0] != nombre_usuario:
        db.mycursor.execute("SELECT COUNT(*) FROM usuario WHERE nombre_usuario = %s ", (nombre_usuario,))
        result = db.mycursor.fetchone()
        if result[0] > 0:
            return True

    return None
        
# Verificar si el RUT ya existe en otro usuario
def rut_existe(rut: str, id: int):
    db.connect()
    if id != 0:
        db.mycursor.execute("SELECT COUNT(*) FROM dato_personal WHERE rut = %s AND id NOT IN (SELECT id_dato_personal FROM usuario WHERE id = %s)", (rut, id))
        result = db.mycursor.fetchone()
        if result[0] > 0:
            return True
        return False
    else:
        # Verificar si el RUT ya existe en otro usuario
        db.mycursor.execute("SELECT COUNT(*) FROM dato_personal WHERE rut = %s", (rut,))
        result = db.mycursor.fetchone()
        if result[0] > 0:
            return True
        return False

