# 9. Desafío integrador: catálogo de productos
def cargar_productos():
    productos = []
    codigo = input("Código del producto (FIN para terminar): ")

    while codigo != "FIN":
        ya_existe = False
        for producto in productos:
            if producto[0] == codigo:
                ya_existe = True

        if ya_existe:
            print("Código repetido, no se agrega")
        else:
            descripcion = input("Descripción: ")
            precio_texto = input("Precio: ")
            if precio_texto.replace(",", ".", 1).replace(".", "", 1).isdigit():
                precio = float(precio_texto.replace(",", ".", 1))
                productos.append((codigo, descripcion, precio))
            else:
                print("Precio inválido, no se agrega el producto")

        codigo = input("Código del producto (FIN para terminar): ")

    return productos

def mostrar_productos(productos):
    for producto in productos:
        codigo, descripcion, precio = producto
        print(f"{codigo} - {descripcion}: ${precio:.2f}")

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto[0] == codigo:
            return producto
    return None

def producto_mayor_precio(productos):
    if len(productos) == 0:
        return None

    mayor = productos[0]
    for producto in productos:
        if producto[2] > mayor[2]:
            mayor = producto
    return mayor

def precio_promedio(productos):
    if len(productos) == 0:
        return None
    suma = 0
    for producto in productos:
        suma = suma + producto[2]
    promedio = suma / len(productos)
    return promedio

def main():
    catalogo = cargar_productos()
    mostrar_productos(catalogo)

    codigo_buscado = input("Ingrese un código para buscar: ")
    encontrado = buscar_producto(catalogo, codigo_buscado)

    if encontrado is not None:
        print("Producto encontrado:", encontrado)
    else:
        print("Producto no encontrado")

    mayor = producto_mayor_precio(catalogo)
    print("Producto de mayor precio:", mayor)

    promedio = precio_promedio(catalogo)
    print("Precio promedio:", promedio)

if __name__ == "__main__":
    main()