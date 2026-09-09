def calcular_importe_producto(cantidad, precio):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero.")
    if precio <= 0:
        raise ValueError("El precio debe ser mayor a cero.")

    importe = cantidad * precio
    assert importe > 0, "El importe calculado debe ser mayor a cero."
    return importe

def cargar_productos():
    """Carga productos hasta ingresar FIN. Devuelve la lista de productos."""
    productos = []

    while True:
        codigo = input("Código del producto (FIN para terminar): ").strip()
        if codigo.upper() == "FIN":
            break

        descripcion = input("Descripción: ").strip()

        try:
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
        except ValueError:
            print("Error: cantidad o precio deben ser numéricos. Producto no incorporado.")
            continue

        try:
            importe = calcular_importe_producto(cantidad, precio)
        except ValueError as error:
            print("Error:", error, "- Producto no incorporado.")
            continue

        productos.append([codigo, descripcion, cantidad, precio, importe])
        print("Producto cargado correctamente.")

    return productos

def informar_totales(productos):
    """Muestra cantidad de productos, importe total y precio promedio."""
    cantidad_productos = len(productos)

    if cantidad_productos == 0:
        print("No se cargaron productos.")
        return

    importe_total = sum(producto[4] for producto in productos)
    precio_promedio = importe_total / cantidad_productos

    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Importe total: ${importe_total:.2f}")
    print(f"Precio promedio: ${precio_promedio:.2f}")
