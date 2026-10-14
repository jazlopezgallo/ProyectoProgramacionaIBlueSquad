"""
EJERCICIO 8 - Archivo + diccionario

Archivo disponible: reclamos.txt
Formato:
numero_reclamo;categoria;detalle

Consigna:
Procesar el archivo y construir un diccionario con la cantidad
de reclamos por categoria.

Luego mostrar:
- Cada categoria con su cantidad.
- La categoria con mayor cantidad de reclamos.

Ejemplo conceptual:
{"Internet": 4, "Facturacion": 2, "Soporte": 2}

Requisitos:
- Leer el archivo una sola vez.
- No usar readlines().
- El diccionario debe construirse durante la lectura.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch = open("reclamos.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo reclamos.txt")
else:
    reclamos_por_categoria = {}

    for linea in arch:
        numero, categoria, detalle = linea.rstrip("\n").split(";")
        if categoria not in reclamos_por_categoria:
            reclamos_por_categoria[categoria] = 0
        reclamos_por_categoria[categoria] += 1

    arch.close()
    print("Cantidad de reclamos por categoria:")
    for categoria in reclamos_por_categoria:
        print(categoria + ":", reclamos_por_categoria[categoria])

    categoria_mayor = ""
    cantidad_mayor = 0
    for categoria in reclamos_por_categoria:
        if reclamos_por_categoria[categoria] > cantidad_mayor:
            categoria_mayor = categoria
            cantidad_mayor = reclamos_por_categoria[categoria]

    if categoria_mayor != "":
        print("Categoria con mas reclamos:", categoria_mayor)
        print("Cantidad:", cantidad_mayor)
    else:
        print("El archivo no contiene reclamos")
