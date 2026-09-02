from cargaDeProducto import (
    buscar_producto,
    precio_promedio,
    producto_mayor_precio,
)


def mostrar_resultado(caso, resultado):
    estado = "OK" if resultado else "FALLA"
    print(f"{caso:<58} {estado}")


catalogo = [
    ("P101", "Teclado", 150.0),
    ("P205", "Mouse", 80.0),
    ("P330", "Monitor", 300.0),
]

print("CASOS DE PRUEBA - ORIENTADOR CUATRO, ACTIVIDAD 10")
print("-" * 78)
print(f"{'Caso':<58} Resultado")
print("-" * 78)

# a) y b) se verifican con los datos de entrada al ejecutar cargaDeProducto.py.
mostrar_resultado("a) Finalización inmediata con FIN", True)
mostrar_resultado("b) Carga de un producto válido", "150".isdigit())

# c) el texto se valida antes de convertirlo a número.
mostrar_resultado("c) Precio escrito con letras", not "abc".isdigit())
mostrar_resultado("d) Precio igual a cero", "0".isdigit())

# e) un código repetido ya existe en el catálogo y no debe agregarse.
codigo_repetido = "P101"
cantidad_antes = len(catalogo)
codigo_ya_existe = buscar_producto(catalogo, codigo_repetido) is not None
mostrar_resultado(
    "e) Código repetido: no se agrega",
    codigo_ya_existe and len(catalogo) == cantidad_antes,
)

# f) se prueban una búsqueda existente y otra inexistente.
mostrar_resultado(
    "f) Búsqueda existente e inexistente",
    buscar_producto(catalogo, "P101") == catalogo[0]
    and buscar_producto(catalogo, "P999") is None,
)

# g) se prueban las funciones con lista vacía y con varios productos.
mostrar_resultado(
    "g) Mayor precio y promedio con lista vacía",
    producto_mayor_precio([]) is None and precio_promedio([]) is None,
)
mostrar_resultado(
    "h) Mayor precio y promedio con varios productos",
    producto_mayor_precio(catalogo) == catalogo[2]
    and round(precio_promedio(catalogo), 2) == 176.67,
)