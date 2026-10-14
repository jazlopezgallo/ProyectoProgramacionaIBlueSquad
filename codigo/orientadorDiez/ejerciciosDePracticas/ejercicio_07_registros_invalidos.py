"""
EJERCICIO 7 - Registros invalidos y excepciones

Archivo disponible: stock.txt
Formato esperado:
codigo;descripcion;cantidad

El archivo contiene algunos registros incorrectos.

Consigna:
Recorrer el archivo y calcular el total de unidades en stock
considerando solamente los registros validos.
Tambien informar cuantos registros fueron descartados.

Se considera invalido un registro cuando:
- No tiene exactamente 3 campos.
- La cantidad no puede convertirse a entero.

Requisitos:
- Procesar una linea por vez.
- Usar manejo de excepciones para las conversiones necesarias.
- No detener el programa por un registro incorrecto.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch = open("stock.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo stock.txt")
else:
    total_unidades = 0
    registros_descartados = 0

    for linea in arch:
        campos = linea.rstrip("\n").split(";")
        if len(campos) != 3:
            registros_descartados += 1
        else:
            try:
                cantidad = int(campos[2])
            except ValueError:
                registros_descartados += 1
            else:
                total_unidades += cantidad

    arch.close()
    print("Total de unidades en stock:", total_unidades)
    print("Registros descartados:", registros_descartados)
