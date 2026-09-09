from productos_modulo import cargar_productos, informar_totales


def main():
    productos = cargar_productos()
    informar_totales(productos)


if __name__ == "__main__":
    main()
