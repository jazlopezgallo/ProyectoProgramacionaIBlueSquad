"""
EJERCICIO 2 - Leer un archivo registro por registro

Archivo disponible: mensajes.txt

Consigna:
Leer el archivo completo sin usar readlines().
Informar:
1. Cantidad total de lineas.
2. Cantidad de lineas que tienen mas de 15 caracteres
   (sin contar el salto de linea).

Requisitos:
- Abrir en modo lectura de texto.
- Procesar una linea por vez.
- Manejar el posible error de apertura.
- Cerrar el archivo.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch = open("mensajes.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo mensajes.txt")
else:
    cantidad_lineas = 0
    lineas_largas = 0

    for linea in arch:
        cantidad_lineas += 1
        texto = linea.rstrip("\n")
        if len(texto) > 15:
            lineas_largas += 1

    arch.close()
    print("Cantidad total de lineas:", cantidad_lineas)
    print("Lineas con mas de 15 caracteres:", lineas_largas)
