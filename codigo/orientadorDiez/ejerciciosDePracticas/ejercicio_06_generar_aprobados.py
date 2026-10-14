"""
EJERCICIO 6 - Leer un archivo y generar otro

Archivo disponible: notas.txt
Formato:
legajo;nombre;nota

Consigna:
Leer notas.txt y crear el archivo aprobados.txt.
En aprobados.txt deben guardarse solo los alumnos con nota >= 6,
manteniendo el siguiente formato:
legajo;nombre;nota

Al finalizar, informar cuantos alumnos fueron guardados.

Requisitos:
- Abrir un archivo para lectura y otro para escritura.
- Procesar registro por registro.
- Agregar salto de linea en cada escritura.
- Cerrar ambos archivos.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch_entrada = open("notas.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo notas.txt")
else:
    try:
        arch_salida = open("aprobados.txt", mode="wt")
    except OSError:
        arch_entrada.close()
        print("No se pudo crear el archivo aprobados.txt")
    else:
        cantidad_aprobados = 0

        for linea in arch_entrada:
            legajo, nombre, nota = linea.rstrip("\n").split(";")
            if float(nota) >= 6:
                arch_salida.write(legajo + ";" + nombre + ";" + nota + "\n")
                cantidad_aprobados += 1

        arch_entrada.close()
        arch_salida.close()
        print("Cantidad de alumnos guardados:", cantidad_aprobados)
