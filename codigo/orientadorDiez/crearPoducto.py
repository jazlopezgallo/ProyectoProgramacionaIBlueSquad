def crear_productos():
    try:
        arch = open("productos.csv", mode="wt")
    except OSError:
        print("No se pudo crear el archivo productos.csv")
    else:
        arch.write("codigo;descripcion;cantidad;precio\n")
        arch.close()
        print("Archivo productos.csv creado")

#Cargar Poductos
def cargar_productos():
    try:
        arch = open("productos.csv", mode="at")
    except OSError:
        print("No se pudo abrir el archivo productos.csv")
    else:
        codigo = input("Ingrese el codigo del producto (FIN para terminar): ")

        while codigo != "FIN":
            descripcion = input("Ingrese la descripcion: ").strip()
            cantidad_texto = input("Ingrese la cantidad: ")
            precio_texto = input("Ingrese el precio: ")

            if codigo == "" or descripcion == "":
                print("El codigo y la descripcion no pueden estar vacios")
            else:
                try:
                    cantidad = int(cantidad_texto)
                    precio = float(precio_texto)
                except ValueError:
                    print("La cantidad y el precio deben ser numericos")
                else:
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa")
                    elif precio <= 0:
                        print("El precio debe ser mayor a cero")
                    else:
                        arch.write(
                            codigo + ";" + descripcion + ";" +
                            str(cantidad) + ";" + str(precio) + "\n"
                        )

            codigo = input(
                "Ingrese el codigo del producto (FIN para terminar): "
            )

        arch.close()
        print("Carga de productos finalizada")

#Leer productos 
def cargar_productos():
    try:
        arch = open("productos.csv", mode="at")
    except OSError:
        print("No se pudo abrir el archivo productos.csv")
    else:
        codigo = input("Ingrese el codigo del producto (FIN para terminar): ")

        while codigo != "FIN":
            descripcion = input("Ingrese la descripcion: ").strip()
            cantidad_texto = input("Ingrese la cantidad: ")
            precio_texto = input("Ingrese el precio: ")

            if codigo == "" or descripcion == "":
                print("El codigo y la descripcion no pueden estar vacios")
            else:
                try:
                    cantidad = int(cantidad_texto)
                    precio = float(precio_texto)
                except ValueError:
                    print("La cantidad y el precio deben ser numericos")
                else:
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa")
                    elif precio <= 0:
                        print("El precio debe ser mayor a cero")
                    else:
                        arch.write(
                            codigo + ";" + descripcion + ";" +
                            str(cantidad) + ";" + str(precio) + "\n"
                        )

            codigo = input(
                "Ingrese el codigo del producto (FIN para terminar): "
            )

        arch.close()
        print("Carga de productos finalizada")

def main():
    crear_productos()
    cargar_productos()


if __name__ == "__main__":
    main()