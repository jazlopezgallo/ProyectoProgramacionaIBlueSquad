# EJERCICIO 12 - Diccionario y conjunto
#
# Dado el siguiente diccionario:
alumnos = {
    1001: "Ana",
    1002: "Luis",
    1003: "Marta",
    1004: "Pedro"
}

# Y el siguiente conjunto de DNI presentes:
presentes = {1001, 1003}

# Mostrar el nombre de los alumnos presentes.

# Escribí tu solución debajo de esta línea:
print("Alumnos presentes:")
for dni in presentes:
    if dni in alumnos:
        print(alumnos[dni])
