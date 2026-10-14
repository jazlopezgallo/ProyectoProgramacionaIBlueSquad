"""
EJERCICIO 1 - Crear un archivo de texto

Objetivo:
Practicar apertura en modo escritura, write(), salto de linea y cierre.

Consigna:
Crear un programa que genere el archivo "nombres.txt".
Solicitar nombres por teclado y guardar un nombre por linea.
La carga finaliza cuando el usuario ingresa FIN.

Requisitos:
- Abrir el archivo en modo texto/escritura.
- Agregar "\n" al guardar cada nombre.
- Cerrar el archivo al finalizar.
- Si el archivo no puede crearse, mostrar un mensaje de error.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch = open("nombres.txt", mode="wt")
except OSError:
    print("No se pudo crear el archivo nombres.txt")
else:
    nombre = input("Ingrese un nombre (FIN para terminar): ")
    while nombre != "FIN":
        arch.write(nombre + "\n")
        nombre = input("Ingrese un nombre (FIN para terminar): ")

    arch.close()
    print("Los nombres se guardaron en nombres.txt")
