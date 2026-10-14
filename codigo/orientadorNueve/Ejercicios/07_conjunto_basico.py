# EJERCICIO 7 - Crear y recorrer un conjunto
#
# Dada la siguiente lista con elementos repetidos:
lenguajes = ["Python", "Java", "Python", "C", "Java", "C++"]

# Crear un conjunto con los lenguajes sin repetir.
# Luego recorrerlo y mostrar cada lenguaje.

# Escribí tu solución debajo de esta línea:

def crear_conjunto(lenguajes):
    conjunto_lenguajes = set(lenguajes)
    return conjunto_lenguajes

conjunto_lenguajes = crear_conjunto(lenguajes)
for lenguaje in conjunto_lenguajes:
    print(lenguaje)

crear_conjunto(lenguajes)

