"""
EJERCICIO 5 - Busqueda secuencial en archivo

Archivo disponible: productos.txt
Formato:
codigo;descripcion;precio

Consigna:
Solicitar al usuario un codigo de producto.
Recorrer el archivo y mostrar descripcion y precio si se encuentra.
Si no existe, informar "Producto inexistente".

Requisitos:
- No usar readlines().
- Usar una variable bandera para indicar si fue encontrado.
- No usar break para cortar el ciclo.
- Manejar error de apertura.
"""

# Escriba su solucion debajo de esta linea.

codigo_buscado = input("Ingrese el codigo del producto: ")
encontrado = False

try:
    arch = open("productos.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo productos.txt")
else:
    for linea in arch:
        codigo, descripcion, precio = linea.rstrip("\n").split(";")
        if codigo == codigo_buscado:
            print("Descripcion:", descripcion)
            print("Precio:", precio)
            encontrado = True

    arch.close()
    if not encontrado:
        print("Producto inexistente")
