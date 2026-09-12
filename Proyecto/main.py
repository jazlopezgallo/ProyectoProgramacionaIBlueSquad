"""
main.py
-------
Punto de entrada del sistema BlueSquad SalesMatrix.
Contiene el menú, las entradas por consola (input) y las salidas (print).
No contiene lógica de cálculo: toda la lógica vive en operaciones.py.
"""

import datos
import operaciones


# ---------------------------------------------------------------------------
# FUNCIONES AUXILIARES DE ENTRADA (validan sin try/except)
# ---------------------------------------------------------------------------

def pedir_entero(mensaje):
    """
    Solicita un número entero por consola hasta recibir uno válido.
    Utiliza operaciones.es_entero() en lugar de try/except.
    """
    texto = input(mensaje)
    while not operaciones.es_entero(texto):
        print("Error: debe ingresar un número entero válido.")
        texto = input(mensaje)
    return int(texto)


def pedir_texto_no_vacio(mensaje):
    """Solicita una cadena no vacía por consola hasta recibir una válida."""
    texto = input(mensaje)
    while not operaciones.texto_valido(texto):
        print("Error: el dato no puede estar vacío.")
        texto = input(mensaje)
    return texto


def mostrar_meses(meses):
    """Imprime la lista de meses numerada, para que el usuario elija uno."""
    for i in range(len(meses)):
        print(f"{i + 1}. {meses[i]}")


# ---------------------------------------------------------------------------
# GESTIÓN DE VENDEDORES
# ---------------------------------------------------------------------------

def gestionar_vendedores(vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores):
    print("\n--- Gestionar vendedores ---")
    print("1. Agregar vendedor")
    print("2. Eliminar vendedor")
    print("3. Buscar vendedor")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = pedir_entero("Código del nuevo vendedor: ")
        nombre = pedir_texto_no_vacio("Nombre del nuevo vendedor: ")
        comision = pedir_entero("Porcentaje de comisión (ej: 5 para 5%): ")
        vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, exito, mensaje = \
            operaciones.agregar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                                          matriz_vendedores, codigo, nombre, comision)
        print(mensaje)

    elif opcion == "2":
        codigo = pedir_entero("Código del vendedor a eliminar: ")
        vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, exito, mensaje = \
            operaciones.eliminar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                                           matriz_vendedores, codigo)
        print(mensaje)

    elif opcion == "3":
        codigo = pedir_entero("Código del vendedor a buscar: ")
        posicion = operaciones.buscar_vendedor(vendedores_id, codigo)
        if posicion == -1:
            print("Error: el vendedor no existe.")
        else:
            print(f"Código: {vendedores_id[posicion]}")
            print(f"Nombre: {vendedores_nombre[posicion]}")
            print(f"Comisión: {vendedores_comision[posicion] * 100:.0f}%")

    else:
        print("Opción inválida.")

    return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores


# ---------------------------------------------------------------------------
# GESTIÓN DE PRODUCTOS
# ---------------------------------------------------------------------------

def gestionar_productos(productos_id, productos_nombre, productos_precio, matriz_productos):
    print("\n--- Gestionar productos ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = pedir_entero("Código del nuevo producto: ")
        nombre = pedir_texto_no_vacio("Nombre del nuevo producto: ")
        precio = pedir_entero("Precio unitario: ")
        productos_id, productos_nombre, productos_precio, matriz_productos, exito, mensaje = \
            operaciones.agregar_producto(productos_id, productos_nombre, productos_precio,
                                          matriz_productos, codigo, nombre, precio)
        print(mensaje)

    elif opcion == "2":
        codigo = pedir_entero("Código del producto a eliminar: ")
        productos_id, productos_nombre, productos_precio, matriz_productos, exito, mensaje = \
            operaciones.eliminar_producto(productos_id, productos_nombre, productos_precio,
                                           matriz_productos, codigo)
        print(mensaje)

    elif opcion == "3":
        codigo = pedir_entero("Código del producto a buscar: ")
        posicion = operaciones.buscar_producto(productos_id, codigo)
        if posicion == -1:
            print("Error: el producto no existe.")
        else:
            print(f"Código: {productos_id[posicion]}")
            print(f"Nombre: {productos_nombre[posicion]}")
            print(f"Precio: ${productos_precio[posicion]}")

    else:
        print("Opción inválida.")

    return productos_id, productos_nombre, productos_precio, matriz_productos


# ---------------------------------------------------------------------------
# REGISTRO DE VENTA (compartido por administrador y vendedor)
# ---------------------------------------------------------------------------

def pedir_datos_venta_y_registrar(vendedores_id, productos_id, productos_precio,
                                   matriz_vendedores, matriz_productos, meses_registrados,
                                   codigo_vendedor_fijo=None):
    """
    Pide los datos de una venta por consola y la registra.
    Si 'codigo_vendedor_fijo' viene indicado (menú vendedor), no se
    solicita el código de vendedor: se usa siempre el mismo.
    """
    if codigo_vendedor_fijo is None:
        codigo_vendedor = pedir_entero("Código del vendedor: ")
    else:
        codigo_vendedor = codigo_vendedor_fijo

    codigo_producto = pedir_entero("Código del producto: ")
    print("\nMeses disponibles:")
    mostrar_meses(datos.MESES)
    mes = pedir_entero("Mes (1-12): ")
    cantidad = pedir_entero("Cantidad de unidades: ")

    matriz_vendedores, matriz_productos, meses_registrados, exito, mensaje = \
        operaciones.registrar_venta(vendedores_id, productos_id, productos_precio,
                                     matriz_vendedores, matriz_productos, meses_registrados,
                                     codigo_vendedor, codigo_producto, mes, cantidad)
    print(mensaje)
    return matriz_vendedores, matriz_productos, meses_registrados


# ---------------------------------------------------------------------------
# INFORMES
# ---------------------------------------------------------------------------

def informe_general(vendedores_nombre, matriz_vendedores, meses_registrados):
    print("\n--- Informe 1: Resumen general ---")
    total = operaciones.total_anual_empresa(matriz_vendedores)
    promedio = operaciones.promedio_general_empresa(matriz_vendedores, meses_registrados)
    proyeccion = operaciones.proyeccion_general(matriz_vendedores, meses_registrados)
    meses_max, importe_max = operaciones.mes_mayor_facturacion(matriz_vendedores, meses_registrados, datos.MESES)

    print(f"Importe total vendido: ${total}")
    if promedio is None:
        print("Promedio mensual: sin meses registrados todavía.")
    else:
        print(f"Promedio mensual de la empresa: ${promedio:.2f}")
    if proyeccion is None:
        print("Proyección estimada: sin meses registrados todavía.")
    else:
        print(f"Proyección estimada anual: ${proyeccion:.2f}")
    if len(meses_max) == 0:
        print("Mes con mayor facturación: sin meses registrados todavía.")
    else:
        print(f"Mes/es con mayor facturación: {', '.join(meses_max)} (${importe_max})")


def informe_producto_mas_vendido(productos_nombre, matriz_productos):
    print("\n--- Informe: Producto más vendido ---")
    nombres, maximo = operaciones.producto_mas_vendido(productos_nombre, matriz_productos)
    if len(nombres) == 0:
        print("No hay productos cargados en el sistema.")
    else:
        print(f"Producto/s más vendido/s: {', '.join(nombres)} ({maximo} unidades)")


def informe_vendedor_mayor_volumen(vendedores_nombre, matriz_vendedores):
    print("\n--- Informe: Vendedor con mayor volumen ---")
    nombres, maximo = operaciones.vendedor_mayor_volumen(vendedores_nombre, matriz_vendedores)
    if len(nombres) == 0:
        print("No hay vendedores cargados en el sistema.")
    else:
        print(f"Vendedor/es con mayor volumen: {', '.join(nombres)} (${maximo})")


def informe_mes_mayor_unidades(matriz_productos, meses_registrados):
    print("\n--- Informe: Mes con mayor cantidad de unidades ---")
    meses_max, cantidad = operaciones.mes_mayor_unidades(matriz_productos, meses_registrados, datos.MESES)
    if len(meses_max) == 0:
        print("Todavía no hay meses registrados.")
    else:
        print(f"Mes/es con mayor cantidad de unidades: {', '.join(meses_max)} ({cantidad} unidades)")


def informe_ranking(vendedores_nombre, matriz_vendedores):
    print("\n--- Ranking de vendedores ---")
    ranking = operaciones.ranking_vendedores(vendedores_nombre, matriz_vendedores)
    for posicion in range(len(ranking)):
        nombre, importe = ranking[posicion]
        print(f"{posicion + 1}. {nombre} -> ${importe}")

    print("\n--- Top 3 ---")
    top3 = operaciones.top_vendedores(ranking, 3)
    for posicion in range(len(top3)):
        nombre, importe = top3[posicion]
        print(f"{posicion + 1}. {nombre} -> ${importe}")


def informe_cumplimiento_objetivo(vendedores_nombre, matriz_vendedores):
    print("\nSeleccione el mes a evaluar:")
    mostrar_meses(datos.MESES)
    mes = pedir_entero("Mes (1-12): ")
    if mes < 1 or mes > 12:
        print("Error: el mes debe estar entre 1 y 12.")
        return

    alcanzaron, no_alcanzaron = operaciones.cumplimiento_objetivo_mes(
        vendedores_nombre, matriz_vendedores, mes, datos.OBJETIVO_MENSUAL
    )
    print(f"\nObjetivo mensual: ${datos.OBJETIVO_MENSUAL}")
    print(f"Vendedores que alcanzaron el objetivo ({len(alcanzaron)}): {', '.join(alcanzaron) if alcanzaron else '-'}")
    print(f"Vendedores que NO alcanzaron el objetivo ({len(no_alcanzaron)}): {', '.join(no_alcanzaron) if no_alcanzaron else '-'}")


# ---------------------------------------------------------------------------
# MENÚ ADMINISTRADOR
# ---------------------------------------------------------------------------

def menu_administrador(vendedores_id, vendedores_nombre, vendedores_comision,
                        productos_id, productos_nombre, productos_precio,
                        matriz_vendedores, matriz_productos, meses_registrados):
    while True:
        print("\n========= ADMINISTRADOR =========")
        print("1. Gestionar vendedores")
        print("2. Gestionar productos")
        print("3. Registrar venta")
        print("4. Consultar matriz de productos")
        print("5. Consultar matriz de vendedores")
        print("6. Informe general")
        print("7. Producto más vendido")
        print("8. Vendedor con mayor volumen de ventas")
        print("9. Mes con mayor cantidad de unidades")
        print("10. Ranking de vendedores / Top 3")
        print("11. Cumplimiento de objetivo por mes")
        print("12. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores = \
                gestionar_vendedores(vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores)

        elif opcion == "2":
            productos_id, productos_nombre, productos_precio, matriz_productos = \
                gestionar_productos(productos_id, productos_nombre, productos_precio, matriz_productos)

        elif opcion == "3":
            matriz_vendedores, matriz_productos, meses_registrados = pedir_datos_venta_y_registrar(
                vendedores_id, productos_id, productos_precio,
                matriz_vendedores, matriz_productos, meses_registrados
            )

        elif opcion == "4":
            print("\n--- MATRIZ DE PRODUCTOS (unidades por mes) ---")
            for i in range(len(productos_nombre)):
                print(f"{productos_nombre[i]}: {matriz_productos[i]}")

        elif opcion == "5":
            print("\n--- MATRIZ DE VENDEDORES (importe por mes) ---")
            for i in range(len(vendedores_nombre)):
                print(f"{vendedores_nombre[i]}: {matriz_vendedores[i]}")

        elif opcion == "6":
            informe_general(vendedores_nombre, matriz_vendedores, meses_registrados)

        elif opcion == "7":
            informe_producto_mas_vendido(productos_nombre, matriz_productos)

        elif opcion == "8":
            informe_vendedor_mayor_volumen(vendedores_nombre, matriz_vendedores)

        elif opcion == "9":
            informe_mes_mayor_unidades(matriz_productos, meses_registrados)

        elif opcion == "10":
            informe_ranking(vendedores_nombre, matriz_vendedores)

        elif opcion == "11":
            informe_cumplimiento_objetivo(vendedores_nombre, matriz_vendedores)

        elif opcion == "12":
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    return (vendedores_id, vendedores_nombre, vendedores_comision,
            productos_id, productos_nombre, productos_precio,
            matriz_vendedores, matriz_productos, meses_registrados)


# ---------------------------------------------------------------------------
# MENÚ VENDEDOR
# ---------------------------------------------------------------------------

def menu_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                   productos_id, productos_precio,
                   matriz_vendedores, matriz_productos, meses_registrados):

    codigo_vendedor = pedir_entero("Ingrese su código de vendedor: ")
    posicion = operaciones.buscar_vendedor(vendedores_id, codigo_vendedor)

    if posicion == -1:
        print("Acceso denegado: el código no corresponde a ningún vendedor.")
        return matriz_vendedores, matriz_productos, meses_registrados

    nombre = vendedores_nombre[posicion]

    while True:
        print(f"\n=========== VENDEDOR: {nombre} ===========")
        print("1. Registrar venta")
        print("2. Consultar mi importe total vendido")
        print("3. Consultar mi comisión")
        print("4. Consultar mi promedio mensual")
        print("5. Consultar mi mejor mes")
        print("6. Consultar cumplimiento del objetivo")
        print("7. Consultar mi proyección estimada")
        print("8. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matriz_vendedores, matriz_productos, meses_registrados = pedir_datos_venta_y_registrar(
                vendedores_id, productos_id, productos_precio,
                matriz_vendedores, matriz_productos, meses_registrados,
                codigo_vendedor_fijo=codigo_vendedor
            )

        elif opcion == "2":
            total = operaciones.total_importe_vendedor(matriz_vendedores, posicion)
            print(f"\nTu importe total vendido es: ${total}")

        elif opcion == "3":
            comision = operaciones.comision_vendedor(matriz_vendedores, vendedores_comision, posicion)
            print(f"\nTu comisión ganada es: ${comision:.2f}")

        elif opcion == "4":
            promedio = operaciones.promedio_mensual_vendedor(matriz_vendedores, posicion, meses_registrados)
            if promedio is None:
                print("\nTodavía no hay meses registrados para calcular tu promedio.")
            else:
                print(f"\nTu promedio mensual es: ${promedio:.2f}")

        elif opcion == "5":
            meses_max, importe = operaciones.mejor_mes_vendedor(matriz_vendedores, posicion, datos.MESES)
            print(f"\nTu mejor mes: {', '.join(meses_max)} (${importe})")

        elif opcion == "6":
            print("\nSeleccione el mes a evaluar:")
            mostrar_meses(datos.MESES)
            mes = pedir_entero("Mes (1-12): ")
            if mes < 1 or mes > 12:
                print("Error: el mes debe estar entre 1 y 12.")
            else:
                importe_mes = matriz_vendedores[posicion][mes - 1]
                if importe_mes >= datos.OBJETIVO_MENSUAL:
                    print(f"\n¡Objetivo alcanzado! Vendiste ${importe_mes} en {datos.MESES[mes - 1]}.")
                else:
                    print(f"\nObjetivo no alcanzado. Vendiste ${importe_mes} en {datos.MESES[mes - 1]} "
                          f"(objetivo: ${datos.OBJETIVO_MENSUAL}).")

        elif opcion == "7":
            proyeccion = operaciones.proyeccion_vendedor(matriz_vendedores, posicion, meses_registrados)
            if proyeccion is None:
                print("\nTodavía no hay meses registrados para calcular tu proyección.")
            else:
                print(f"\nTu proyección estimada anual es: ${proyeccion:.2f}")

        elif opcion == "8":
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    return matriz_vendedores, matriz_productos, meses_registrados


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------

def main():
    vendedores_id = datos.VENDEDORES_ID_INICIAL[:]
    vendedores_nombre = datos.VENDEDORES_NOMBRE_INICIAL[:]
    vendedores_comision = datos.VENDEDORES_COMISION_INICIAL[:]

    productos_id = datos.PRODUCTOS_ID_INICIAL[:]
    productos_nombre = datos.PRODUCTOS_NOMBRE_INICIAL[:]
    productos_precio = datos.PRODUCTOS_PRECIO_INICIAL[:]

    matriz_vendedores = operaciones.crear_matriz(len(vendedores_id))
    matriz_productos = operaciones.crear_matriz(len(productos_id))
    meses_registrados = operaciones.crear_meses_registrados()

    while True:
        print("\n================================")
        print("      BLUE SQUAD SALESMATRIX")
        print("================================")
        print("1. Administrador")
        print("2. Vendedor")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            (vendedores_id, vendedores_nombre, vendedores_comision,
             productos_id, productos_nombre, productos_precio,
             matriz_vendedores, matriz_productos, meses_registrados) = menu_administrador(
                vendedores_id, vendedores_nombre, vendedores_comision,
                productos_id, productos_nombre, productos_precio,
                matriz_vendedores, matriz_productos, meses_registrados
            )

        elif opcion == "2":
            matriz_vendedores, matriz_productos, meses_registrados = menu_vendedor(
                vendedores_id, vendedores_nombre, vendedores_comision,
                productos_id, productos_precio,
                matriz_vendedores, matriz_productos, meses_registrados
            )

        elif opcion == "3":
            print("Apagando el sistema CRM... ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.")


if __name__ == "__main__":
    main()
