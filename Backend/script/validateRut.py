import re

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
