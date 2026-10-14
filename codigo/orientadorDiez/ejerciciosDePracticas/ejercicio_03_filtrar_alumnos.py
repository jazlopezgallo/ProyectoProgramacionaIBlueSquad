"""
EJERCICIO 3 - Separar campos con split()

Archivo disponible: alumnos.txt
Formato de cada registro:
legajo;nombre

Consigna:
Mostrar solamente los alumnos cuyo legajo sea mayor a 10000.

Ejemplo de salida:
Legajo: 12000 - Nombre: Maria Lopez

Requisitos:
- No usar readlines().
- Procesar registro por registro.
- Separar los campos con split(";").
- Convertir el legajo a int para comparar.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch = open("alumnos.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo alumnos.txt")
else:
    for linea in arch:
        legajo, nombre = linea.rstrip("\n").split(";")
        if int(legajo) > 10000:
            print("Legajo:", legajo, "- Nombre:", nombre)

    arch.close()
