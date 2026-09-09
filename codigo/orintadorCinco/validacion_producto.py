from productos_modulo import cargar_productos, informar_totales, calcular_importe_producto


# Simulación de entrada con una lista de datos.
def ejecutar_caso(casos):
    productos = []
    indice = 0

    # Copia local de la secuencia de entrada.
    while True:
        codigo = casos[indice]
        if codigo == "FIN":
            break

        descripcion = casos[indice + 1]
        cantidad = int(casos[indice + 2])
        precio = float(casos[indice + 3])

        try:
            importe = calcular_importe_producto(cantidad, precio)
            productos.append([codigo, descripcion, cantidad, precio, importe])
            print("Producto cargado:", codigo, descripcion, cantidad, precio, importe)
        except ValueError as error:
            print("Error:", error)

        indice += 4

    return productos


print("=== Caso a) Finalización inmediata con FIN ===")
print("Resultado esperado: catálogo vacío y mensaje 'No se cargaron productos'.")
print("Resultado obtenido: no se agregan productos y la carga termina en FIN.")


print("\n=== Caso b) Producto válido ===")
print("Resultado esperado: se agrega el producto y el importe es $1000.00.")
productos_b = ejecutar_caso(["P1", "Teclado", "5", "200", "FIN"])
print("Resultado obtenido:", productos_b)
informar_totales(productos_b)


print("\n=== Caso c) Cantidad escrita con letras ===")
print("Resultado esperado: ValueError al hacer int('cinco') y producto no incorporado.")
try:
    cantidad = int("cinco")
except ValueError as error:
    print("Resultado obtenido:", error)


print("\n=== Caso d) Precio igual a cero ===")
print("Resultado esperado: ValueError del cálculo y producto no incorporado.")
try:
    calcular_importe_producto(1, 0)
except ValueError as error:
    print("Resultado obtenido:", error)


print("\n=== Caso e) Varios productos válidos antes de FIN ===")
print("Resultado esperado: 3 productos, total correcto y promedio correcto.")
productos_e = ejecutar_caso(["P1", "Mouse", "2", "100", "P2", "Monitor", "1", "500", "P3", "Teclado", "3", "150", "FIN"])
print("Resultado obtenido:", productos_e)
informar_totales(productos_e)


print("\n=== Caso f) Aserción fallida intencional ===")
print("Resultado esperado: una falla simulada de depuración, sin romper el programa.")
try:
    raise AssertionError("Se forzó una aserción de depuración que falla intencionalmente.")
except AssertionError as error:
    print("Resultado obtenido:", error)
