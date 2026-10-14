# EJERCICIO 5 - Contar apariciones
#
# Dada la siguiente lista:
colores = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]

# Crear un diccionario que indique cuántas veces aparece cada color.
#
# Resultado esperado:
# {'rojo': 3, 'azul': 2, 'verde': 1}

# Escribí tu solución debajo de esta línea:

def contar_colores(colores):
    diccionario_colores = {}
    for color in colores:
        diccionario_colores[color] = diccionario_colores.get(color, 0) + 1
    return diccionario_colores

resultado = contar_colores(colores)
print(resultado)