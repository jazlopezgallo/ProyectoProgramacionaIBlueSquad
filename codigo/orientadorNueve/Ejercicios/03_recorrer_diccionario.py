# EJERCICIO 3 - Recorrer un diccionario
#
# Dado el siguiente diccionario:
notas = {
    "Ana": 8,
    "Luis": 6,
    "Marta": 9,
    "Pedro": 5
}

# Mostrar cada alumno junto con su nota.
# Ejemplo:
# Ana obtuvo 8

# Escribí tu solución debajo de esta línea:
def mostrar_notas(notas):
    for alumno, nota in notas.items():
        print(f"{alumno} obtuvo {nota}")

mostrar_notas(notas)
