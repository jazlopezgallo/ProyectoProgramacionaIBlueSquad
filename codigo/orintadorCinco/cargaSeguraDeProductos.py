def calcular_importe_producto(cantidad, precio):
    """Retorna cantidad * precio. Lanza ValueError si algún dato no es válido."""
    if cantidad <= 0 or precio <= 0:
        raise ValueError("Cantidad y precio deben ser mayores a cero")

    importe = cantidad * precio
    assert importe > 0, "El importe calculado no puede ser cero o negativo"
    return importe


def cargar_productos():
    """Carga productos hasta que el código ingresado sea FIN. Retorna la lista de productos."""
    productos = []

    while True:
        codigo = input("Código del producto (FIN para terminar): ")
        if codigo == "FIN":
            break

        descripcion = input("Descripción: ")

        try:
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            importe = calcular_importe_producto(cantidad, precio)
            productos.append([codigo, descripcion, cantidad, precio, importe])
            print("Producto cargado correctamente")
        except ValueError as error:
            print("Error:", error, "- Producto no incorporado")

    return productos


def informar_totales(productos):
    """Muestra cantidad de productos, importe total y precio promedio."""
    cantidad_productos = len(productos)

    if cantidad_productos == 0:
        print("No se cargaron productos")
        return

    importe_total = 0
    for producto in productos:
        importe_total = importe_total + producto[4]

    precio_promedio = importe_total / cantidad_productos

    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Importe total: ${importe_total:.2f}")
    print(f"Precio promedio: ${precio_promedio:.2f}")


# Programa principal
catalogo = cargar_productos()
informar_totales(catalogo)