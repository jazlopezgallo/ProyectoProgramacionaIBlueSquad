import datos
import operacionesv2 as operaciones

def color_error(mensaje):
    print(f"\033[31m{mensaje}\033[0m")

def color_exito(mensaje):
    print(f"\033[32m{mensaje}\033[0m")

def color_info(mensaje):
    print(f"\033[34m{mensaje}\033[0m")

def pedir_entero(mensaje):
    texto = input(mensaje)
    while not operaciones.es_entero(texto)[0]:
        color_error("Error: debe ingresar un número entero válido.")
        texto = input(mensaje)
    return int(texto)

def pedir_texto(mensaje):
    texto = input(mensaje).strip()
    while not operaciones.texto_valido(texto)[0]:
        color_error("Error: el dato no puede estar vacío.")
        texto = input(mensaje).strip()
    return texto

def mostrar_menu(titulo, opciones):
    color_info(f"\n--- {titulo} ---")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")

def mostrar_meses(meses):
    for i, mes in enumerate(meses, 1):
        print(f"{i}. {mes}")

def mostrar_matriz(titulo, nombres, matriz):
    print(f"\n{titulo}")
    for i, nombre in enumerate(nombres):
        print(f"{nombre}: {matriz[i]}")

def gestionar_vendedores(ids, nombres, comisiones, matriz):
    print("\n1. Agregar\n2. Eliminar\n3. Buscar")
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        codigo = pedir_entero("Código: ")
        nombre = pedir_texto("Nombre: ")
        comision = pedir_entero("Comisión (%): ")
        ids, nombres, comisiones, matriz, ok, mensaje = operaciones.agregar_vendedor(
            ids, nombres, comisiones, matriz, codigo, nombre, comision)
        color_exito(mensaje) if ok else color_error(mensaje)
    elif opcion == "2":
        codigo = pedir_entero("Código a eliminar: ")
        ids, nombres, comisiones, matriz, ok, mensaje = operaciones.eliminar_vendedor(
            ids, nombres, comisiones, matriz, codigo)
        color_exito(mensaje) if ok else color_error(mensaje)
    elif opcion == "3":
        codigo = pedir_entero("Código a buscar: ")
        posicion = operaciones.busqueda_secuencial(ids, codigo)
        if posicion == -1:
            color_error("Error: el vendedor no existe.")
        else:
            print(f"Código: {ids[posicion]}")
            print(f"Nombre: {nombres[posicion]}")
            print(f"Comisión: {comisiones[posicion] * 100:.0f}%")
    else:
        color_error("Opción inválida.")
    return ids, nombres, comisiones, matriz

def gestionar_productos(ids, nombres, precios, matriz):
    print("\n1. Agregar\n2. Eliminar\n3. Buscar")
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        codigo = pedir_entero("Código: ")
        nombre = pedir_texto("Nombre: ")
        precio = pedir_entero("Precio unitario: ")
        ids, nombres, precios, matriz, ok, mensaje = operaciones.agregar_producto(
            ids, nombres, precios, matriz, codigo, nombre, precio)
        color_exito(mensaje) if ok else color_error(mensaje)
    elif opcion == "2":
        codigo = pedir_entero("Código a eliminar: ")
        ids, nombres, precios, matriz, ok, mensaje = operaciones.eliminar_producto(
            ids, nombres, precios, matriz, codigo)
        color_exito(mensaje) if ok else color_error(mensaje)
    elif opcion == "3":
        codigo = pedir_entero("Código a buscar: ")
        posicion = operaciones.busqueda_secuencial(ids, codigo)
        if posicion == -1:
            color_error("Error: el producto no existe.")
        else:
            print(f"Código: {ids[posicion]}")
            print(f"Nombre: {nombres[posicion]}")
            print(f"Precio: ${precios[posicion]:.2f}")
    else:
        color_error("Opción inválida.")
    return ids, nombres, precios, matriz

def registrar_venta_menu(vendedores_id, productos_id, precios, matriz_vendedores,
                         matriz_productos, meses_registrados, meses, codigo_fijo=None):
    codigo_vendedor = codigo_fijo if codigo_fijo is not None else pedir_entero("Código de vendedor: ")
    codigo_producto = pedir_entero("Código de producto: ")
    mostrar_meses(meses)
    mes = pedir_entero("Mes (1-12): ")
    cantidad = pedir_entero("Cantidad de unidades: ")

    matriz_vendedores, matriz_productos, meses_registrados, ok, mensaje = operaciones.registrar_venta(
        vendedores_id, productos_id, precios, matriz_vendedores, matriz_productos,
        meses_registrados, codigo_vendedor, codigo_producto, mes, cantidad)

    color_exito(mensaje) if ok else color_error(mensaje)
    return matriz_vendedores, matriz_productos, meses_registrados

def menu_administrador(vendedores_id, vendedores_nombre, vendedores_comision,
                        productos_id, productos_nombre, productos_precio,
                        matriz_vendedores, matriz_productos, meses_registrados,
                        meses, objetivo_mensual):
    opciones = [
        "Gestionar vendedores (Agregar / Eliminar / Buscar)",
        "Gestionar productos (Agregar / Eliminar / Buscar)",
        "Registrar venta",
        "Consultar matriz de productos",
        "Consultar matriz de vendedores",
        "Producto más vendido",
        "Vendedor con mayor volumen de ventas",
        "Mes con mayor cantidad de unidades",
        "Ranking de vendedores / Top 3",
        "Cumplimiento de objetivo por mes",
        "Volver"
    ]

    while True:
        mostrar_menu("ADMINISTRADOR", opciones)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores = gestionar_vendedores(
                vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores)
        elif opcion == "2":
            productos_id, productos_nombre, productos_precio, matriz_productos = gestionar_productos(
                productos_id, productos_nombre, productos_precio, matriz_productos)
        elif opcion == "3":
            matriz_vendedores, matriz_productos, meses_registrados = registrar_venta_menu(
                vendedores_id, productos_id, productos_precio, matriz_vendedores,
                matriz_productos, meses_registrados, meses)
        elif opcion == "4":
            mostrar_matriz("MATRIZ DE PRODUCTOS - UNIDADES POR MES", productos_nombre, matriz_productos)
        elif opcion == "5":
            mostrar_matriz("MATRIZ DE VENDEDORES - IMPORTE POR MES", vendedores_nombre, matriz_vendedores)
        elif opcion == "6":
            nombres, total = operaciones.producto_mas_vendido(productos_nombre, matriz_productos)
            print("No hay ventas registradas." if not nombres else
                  f"Producto/s más vendido/s: {', '.join(nombres)} ({total} unidades)")
        elif opcion == "7":
            nombres, total = operaciones.vendedor_mayor_volumen(vendedores_nombre, matriz_vendedores)
            print("No hay ventas registradas." if not nombres else
                  f"Vendedor/es con mayor volumen: {', '.join(nombres)} (${total:.2f})")
        elif opcion == "8":
            meses_max, total = operaciones.mes_mayor_unidades(
                matriz_productos, meses_registrados, meses)
            print("Todavía no hay meses registrados." if not meses_max else
                  f"Mes/es con mayor cantidad de unidades: {', '.join(meses_max)} ({total} unidades)")
        elif opcion == "9":
            ranking = operaciones.ranking_vendedores(vendedores_nombre, matriz_vendedores)
            for i, (nombre, total) in enumerate(ranking, 1):
                print(f"{i}. {nombre} -> ${total:.2f}")
            print("\nTop 3:")
            for i, (nombre, total) in enumerate(operaciones.top_vendedores(ranking, 3), 1):
                print(f"{i}. {nombre} -> ${total:.2f}")
        elif opcion == "10":
            mostrar_meses(meses)
            mes = pedir_entero("Mes a evaluar: ")
            alcanzaron, no_alcanzaron, registrado = operaciones.cumplimiento_objetivo_mes(
                vendedores_nombre, matriz_vendedores, mes, objetivo_mensual, meses_registrados)
            if not registrado:
                color_error("El mes seleccionado todavía no está registrado.")
            else:
                print(f"Objetivo: ${objetivo_mensual:.2f}")
                print("Alcanzaron:", ", ".join(alcanzaron) if alcanzaron else "-")
                print("No alcanzaron:", ", ".join(no_alcanzaron) if no_alcanzaron else "-")
        elif opcion == "11":
            return (vendedores_id, vendedores_nombre, vendedores_comision,
                    productos_id, productos_nombre, productos_precio,
                    matriz_vendedores, matriz_productos, meses_registrados)
        else:
            color_error("Opción inválida.")

def menu_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                  productos_id, productos_precio, matriz_vendedores,
                  matriz_productos, meses_registrados, meses):
    codigo_vendedor = pedir_entero("Ingrese su código de vendedor: ")
    posicion = operaciones.busqueda_secuencial(vendedores_id, codigo_vendedor)

    if posicion == -1:
        color_error("El código de vendedor no existe.")
        return matriz_vendedores, matriz_productos, meses_registrados

    opciones = [
        "Registrar venta",
        "Consultar mi importe total vendido",
        "Consultar mi comisión",
        "Consultar mi proyección estimada",
        "Volver"
    ]

    while True:
        mostrar_menu(f"VENDEDOR: {vendedores_nombre[posicion]}", opciones)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            matriz_vendedores, matriz_productos, meses_registrados = registrar_venta_menu(
                vendedores_id, productos_id, productos_precio, matriz_vendedores,
                matriz_productos, meses_registrados, meses, codigo_vendedor)
        elif opcion == "2":
            total = operaciones.total_importe_vendedor(matriz_vendedores, posicion)
            print(f"Mi importe total vendido: ${total:.2f}")
        elif opcion == "3":
            comision = operaciones.comision_vendedor(
                matriz_vendedores, vendedores_comision, posicion)
            print(f"Mi comisión: ${comision:.2f}")
        elif opcion == "4":
            proyeccion = operaciones.proyeccion_vendedor(
                matriz_vendedores, posicion, meses_registrados)
            print("Todavía no hay meses registrados." if proyeccion is None else
                  f"Mi proyección estimada anual: ${proyeccion:.2f}")
        elif opcion == "5":
            return matriz_vendedores, matriz_productos, meses_registrados
        else:
            color_error("Opción inválida.")

def main():
    (matriz_vendedores, matriz_productos, productos_precio, vendedores_nombre,
     productos_nombre, meses, vendedores_id, vendedores_comision,
     objetivo_mensual, productos_id) = datos.creaciondatos()

    meses_registrados = [False] * len(meses)

    while True:
        mostrar_menu("BLUE SQUAD SALESMATRIX", ["Administrador", "Vendedor", "Salir"])
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            (vendedores_id, vendedores_nombre, vendedores_comision,
             productos_id, productos_nombre, productos_precio,
             matriz_vendedores, matriz_productos, meses_registrados) = menu_administrador(
                vendedores_id, vendedores_nombre, vendedores_comision,
                productos_id, productos_nombre, productos_precio,
                matriz_vendedores, matriz_productos, meses_registrados,
                meses, objetivo_mensual)
        elif opcion == "2":
            matriz_vendedores, matriz_productos, meses_registrados = menu_vendedor(
                vendedores_id, vendedores_nombre, vendedores_comision,
                productos_id, productos_precio, matriz_vendedores,
                matriz_productos, meses_registrados, meses)
        elif opcion == "3":
            print("Sistema finalizado.")
            break
        else:
            color_error("Opción inválida.")

if __name__ == "__main__":
    main()