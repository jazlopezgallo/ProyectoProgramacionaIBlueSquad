"""
EJERCICIO 4 - Procesamiento numerico de registros

Archivo disponible: ventas.txt
Formato:
codigo;producto;cantidad;precio_unitario

Consigna:
Leer el archivo una sola vez e informar:
1. Importe total vendido.
2. Cantidad total de unidades vendidas.
3. Producto correspondiente a la venta de mayor importe
   (cantidad * precio_unitario).

Requisitos:
- No cargar todo el archivo en memoria.
- Procesar linea por linea.
- Convertir los campos numericos al tipo adecuado.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch = open("ventas.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo ventas.txt")
else:
    importe_total = 0
    unidades_totales = 0
    importe_mayor = 0
    producto_mayor = ""
    hay_ventas = False

    for linea in arch:
        codigo, producto, cantidad, precio_unitario = linea.rstrip("\n").split(";")
        cantidad = int(cantidad)
        precio_unitario = float(precio_unitario)
        importe = cantidad * precio_unitario

        importe_total += importe
        unidades_totales += cantidad

        if not hay_ventas or importe > importe_mayor:
            importe_mayor = importe
            producto_mayor = producto
            hay_ventas = True

    arch.close()
    print("Importe total vendido:", importe_total)
    print("Cantidad total de unidades vendidas:", unidades_totales)
    if hay_ventas:
        print("Producto de la venta de mayor importe:", producto_mayor)
    else:
        print("El archivo no contiene ventas")
