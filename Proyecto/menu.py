import Crmv2


def menu_admin(vendedores, matriz_vendedores, productos, matriz_productos):
    while True:
        print("\n=== MENÚ DE ADMINISTRADOR ===")
        print("1. Modificar lista de vendedores (Agregar / Eliminar)")
        print("2. Modificar lista de productos (Agregar / Eliminar)")
        print("3. Imprimir matrices de productos")
        print("4. Imprimir matrices de vendedores")
        print("5. Revisar total anual de ventas")
        print("6. Revisar promedio de ventas mensuales")
        print("7. Volver")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            print("\n-- Modificar Vendedores --")
            print("1. Agregar")
            print("2. Eliminar")
            sub_op = input("Seleccione 1 o 2: ")
            if sub_op == '1':
                nombre = input("Ingrese el nombre del nuevo vendedor: ")
                vendedores, matriz_vendedores, msg = Crmv2.agregar_vendedor(vendedores, matriz_vendedores, nombre)
                print(msg)
            elif sub_op == '2':
                nombre = input("Ingrese el nombre del vendedor a eliminar: ")
                vendedores, matriz_vendedores, msg = Crmv2.eliminar_vendedor(vendedores, matriz_vendedores, nombre)
                print(msg)
            else:
                print("Opción no válida.")

        elif opcion == '2':
            print("\n-- Modificar Productos --")
            print("1. Agregar")
            print("2. Eliminar")
            sub_op = input("Seleccione 1 o 2: ")
            if sub_op == '1':
                nombre = input("Ingrese el nombre del nuevo producto: ")
                productos, matriz_productos, msg = Crmv2.agregar_producto(productos, matriz_productos, nombre)
                print(msg)
            elif sub_op == '2':
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                productos, matriz_productos, msg = Crmv2.eliminar_producto(productos, matriz_productos, nombre)
                print(msg)
            else:
                print("Opción no válida.")

        elif opcion == '3':
            print(Crmv2.imprimir_matriz_productos(productos, matriz_productos))

        elif opcion == '4':
            print(Crmv2.imprimir_matriz_vendedores(vendedores, matriz_vendedores))

        elif opcion == '5':
            total = Crmv2.total_anual_empresa(matriz_vendedores)
            print(f"\nEl total anual de ventas de toda la empresa es: ${total}")

        elif opcion == '6':
            promedio = Crmv2.promedio_ventas_mensuales_empresa(matriz_vendedores, vendedores)
            if promedio is None:
                print("\nNo hay vendedores para calcular el promedio.")
            else:
                print(f"\nEl promedio de ventas mensuales por vendedor es: ${promedio:.2f}")

        elif opcion == '7':
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    return vendedores, matriz_vendedores, productos, matriz_productos


def menu_vendedor(vendedores, matriz_vendedores, productos, matriz_productos):
    nombre = input("Por favor, ingrese su nombre de vendedor: ").capitalize()

    if nombre not in vendedores:
        print(f"\nAcceso denegado: El nombre '{nombre}' no se encuentra en la lista de vendedores.")
        return vendedores, matriz_vendedores, productos, matriz_productos

    indice_vend = vendedores.index(nombre)

    while True:
        print(f"\n=== MENÚ DE VENDEDOR: {nombre} ===")
        print("1. Modificar mis ingresos mensuales")
        print("2. Revisar mi promedio de ventas mensuales")
        print("3. Revisar mi total anual")
        print("4. Añadir nuevos productos")
        print("5. Añadir proyecciones en base al promedio mensual")
        print("6. Revisar el producto más vendido")
        print("7. Volver")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            try:
                mes = int(input("Ingrese el número del mes a modificar (1-12): "))
                valor = int(input("Ingrese el nuevo monto: $"))
                matriz_vendedores = Crmv2.modificar_ingreso_mes(matriz_vendedores, indice_vend, mes, valor)
                print("Ingreso actualizado exitosamente.")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")

        elif opcion == '2':
            promedio = Crmv2.revisar_promedio_vendedor(matriz_vendedores, indice_vend)
            print(f"\nTu promedio de ventas mensuales es: ${promedio:.2f}")

        elif opcion == '3':
            total = Crmv2.revisar_total_vendedor(matriz_vendedores, indice_vend)
            print(f"\nTu total de ventas anuales es: ${total}")

        elif opcion == '4':
            nombre_p = input("Ingrese el nombre del nuevo producto: ")
            productos, matriz_productos, msg = Crmv2.agregar_producto(productos, matriz_productos, nombre_p)
            print(msg)

        elif opcion == '5':
            try:
                meses_proy = int(input("¿Para cuántos meses a futuro desea calcular la proyección?: "))
                proyeccion = Crmv2.anadir_proyeccion(matriz_vendedores, indice_vend, meses_proy)
                print(f"\nProyección para los próximos {meses_proy} meses: ${proyeccion:.2f}")
            except ValueError:
                print("Entrada inválida para meses.")

        elif opcion == '6':
            prod, ventas = Crmv2.producto_mas_vendido(productos, matriz_productos)
            if prod is None:
                print("No hay productos en el sistema.")
            else:
                print(f"\nEl producto más vendido es '{prod}' con un total de ${ventas}.")

        elif opcion == '7':
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    return vendedores, matriz_vendedores, productos, matriz_productos


if __name__ == '__main__':
    # Estado local mantenido por el menú (no globales del módulo Crmv2)
    vendedores = Crmv2.DEFAULT_VENDEDORES[:]
    productos = Crmv2.DEFAULT_PRODUCTOS[:]
    precios = Crmv2.DEFAULT_PRECIOS[:]
    matriz_vendedores, matriz_productos = Crmv2.creacionmatrices(vendedores, productos)

    while True:
        print("\n" + "=" * 30)
        print("--- SISTEMA CRM PRINCIPAL ---")
        print("=" * 30)
        print("1. Acceso Administrador")
        print("2. Acceso Vendedor")
        print("3. Apagar Sistema")

        tipo_usuario = input("Ingrese su opción (1, 2 o 3): ")

        if tipo_usuario == '1':
            vendedores, matriz_vendedores, productos, matriz_productos = menu_admin(vendedores, matriz_vendedores, productos, matriz_productos)
        elif tipo_usuario == '2':
            vendedores, matriz_vendedores, productos, matriz_productos = menu_vendedor(vendedores, matriz_vendedores, productos, matriz_productos)
        elif tipo_usuario == '3':
            print("Apagando el sistema CRM... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
