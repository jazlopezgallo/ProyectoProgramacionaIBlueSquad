import datos
import operaciones


# ---------------------------------------------------------------------------
# PRESENTACIÓN Y ENTRADA DE DATOS
# ---------------------------------------------------------------------------

def color(mensaje, codigo):
    print(f"\033[{codigo}m{mensaje}\033[0m")

def color_error(mensaje):
    color(mensaje, 31)

def mostrar_resultado(resultado):
    """Recibe la tupla (ok, mensaje) que devuelven las operaciones."""
    color(resultado[1], 32 if resultado[0] else 31)

def pesos(valor):
    return f"${valor:.2f}"

def pedir_entero(mensaje):
    texto = input(mensaje)
    while not operaciones.es_entero(texto)[0]:
        color_error("Error: debe ingresar un número entero válido.")
        texto = input(mensaje)
    return int(texto)

def pedir_texto(mensaje):
    texto = input(mensaje)
    while not operaciones.texto_valido(texto)[0]:
        color_error("Error: el dato no puede estar vacío.")
        texto = input(mensaje)
    return texto

def pedir_mes(meses, meses_registrados, mensaje):
    for i, mes in enumerate(meses, 1):
        print(f"{i}. {mes} ({'procesado' if meses_registrados[i - 1] else 'sin información'})")
    return pedir_entero(mensaje)

def elegir_opcion(titulo, opciones):
    color(f"\n--- {titulo} ---", 34)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    return input("Seleccione una opción: ").strip()

def mostrar_maximos(titulo, maximo, es_importe):
    """Muestra el resultado de operaciones.maximos: (nombres empatados, total)."""
    nombres, total = maximo
    detalle = pesos(total) if es_importe else f"{total} unidades"
    print(f"{titulo}: {', '.join(nombres)} ({detalle})" if nombres else "Todavía no hay datos registrados.")

def mostrar_ranking(ranking):
    for i, (nombre, total) in enumerate(ranking, 1):
        print(f"{i}. {nombre} -> {pesos(total)}")


# ---------------------------------------------------------------------------
# MENÚS
# ---------------------------------------------------------------------------

def gestionar(ids, nombres, valores, matriz, entidad):
    """Agregar / Eliminar / Buscar, común a vendedores (valores = comisiones) y productos (valores = precios)."""
    es_vendedor = entidad == "vendedor"
    opcion = elegir_opcion(f"GESTIÓN DE {'VENDEDORES' if es_vendedor else 'PRODUCTOS'}", ["Agregar", "Eliminar", "Buscar"])
    if opcion == "1":
        codigo = pedir_entero("Código: ")
        nombre = pedir_texto("Nombre: ")
        agregar = operaciones.agregar_vendedor if es_vendedor else operaciones.agregar_producto
        valor = pedir_entero("Comisión (%): " if es_vendedor else "Precio unitario: ")
        mostrar_resultado(agregar(ids, nombres, valores, matriz, codigo, nombre, valor))
    elif opcion == "2":
        codigo = pedir_entero("Código a eliminar: ")
        mostrar_resultado(operaciones.eliminar_elemento(ids, nombres, valores, matriz, codigo, entidad))
    elif opcion == "3":
        posicion = operaciones.busqueda_secuencial(ids, pedir_entero("Código a buscar: "))
        if posicion == -1:
            color_error(f"Error: el {entidad} no existe.")
        else:
            print(f"Código: {ids[posicion]}\nNombre: {nombres[posicion]}")
            print(f"Comisión: {valores[posicion] * 100:.0f}%" if es_vendedor else f"Precio: {pesos(valores[posicion])}")
    else:
        color_error("Opción inválida.")

def registrar_venta_menu(vendedores_id, productos_id, precios, matriz_vendedores,
                         matriz_productos, meses_registrados, meses, codigo_fijo=None):
    codigo_vendedor = codigo_fijo if codigo_fijo is not None else pedir_entero("Código de vendedor: ")
    codigo_producto = pedir_entero("Código de producto: ")
    mes = pedir_mes(meses, meses_registrados, "Mes (1-12): ")
    cantidad = pedir_entero("Cantidad de unidades: ")
    mostrar_resultado(operaciones.registrar_venta(
        vendedores_id, productos_id, precios, matriz_vendedores, matriz_productos,
        meses_registrados, codigo_vendedor, codigo_producto, mes, cantidad))


def menu_administrador(vendedores_id, vendedores_nombre, vendedores_comision,
                       productos_id, productos_nombre, productos_precio,
                       matriz_vendedores, matriz_productos, meses_registrados,
                       meses, objetivo_mensual):
    opciones = [
        "Gestionar vendedores (Agregar / Eliminar / Buscar)",
        "Gestionar productos (Agregar / Eliminar / Buscar)",
        "Registrar venta",
        "Marcar mes como procesado (mes sin ventas)",
        "Producto más vendido (unidades vendidas)",
        "Vendedor con mayor importe vendido",
        "Ranking de vendedores por importe vendido / Top 3",
        "Cumplimiento de objetivo mensual",
        "Promedio mensual y proyección anual de la empresa",
        "Volver"
    ]
    opcion_salir = str(len(opciones))
    opcion = ""

    while opcion != opcion_salir:
        opcion = elegir_opcion("ADMINISTRADOR", opciones)

        if opcion == "1":
            gestionar(vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, "vendedor")
        elif opcion == "2":
            gestionar(productos_id, productos_nombre, productos_precio, matriz_productos, "producto")
        elif opcion == "3":
            registrar_venta_menu(vendedores_id, productos_id, productos_precio, matriz_vendedores,
                                 matriz_productos, meses_registrados, meses)
        elif opcion == "4":
            mes = pedir_mes(meses, meses_registrados, "Mes a marcar como procesado (1-12): ")
            mostrar_resultado(operaciones.procesar_mes(meses_registrados, meses, mes))
        elif opcion == "5":
            mostrar_maximos("Producto/s más vendido/s",
                            operaciones.mayor_total(productos_nombre, matriz_productos), False)
        elif opcion == "6":
            mostrar_maximos("Vendedor/es con mayor importe vendido",
                            operaciones.mayor_total(vendedores_nombre, matriz_vendedores), True)
        elif opcion == "7":
            ranking = operaciones.ranking_vendedores(vendedores_nombre, matriz_vendedores)
            mostrar_ranking(ranking)
            print("\nTop 3:")
            mostrar_ranking(operaciones.top_vendedores(ranking, 3))
        elif opcion == "8":
            mes = pedir_mes(meses, meses_registrados, "Mes a evaluar: ")
            alcanzaron, no_alcanzaron, procesado = operaciones.cumplimiento_objetivo_mes(
                vendedores_nombre, matriz_vendedores, mes, objetivo_mensual, meses_registrados)
            if not procesado:
                color_error("El mes seleccionado no es válido o todavía no fue procesado.")
            else:
                print(f"Objetivo de importe mensual vendido: {pesos(objetivo_mensual)}")
                print("Alcanzaron:", ", ".join(alcanzaron) if alcanzaron else "-")
                print("No alcanzaron:", ", ".join(no_alcanzaron) if no_alcanzaron else "-")
        elif opcion == "9":
            totales =operaciones.totales_por_mes(matriz_vendedores, meses_registrados)
            promedio = operaciones.promedio_mensual(totales, meses_registrados)
            if promedio is None:
                color_error("Todavía no hay meses procesados.")
            else:
                print(f"Meses procesados: {meses_registrados.count(True)}")
                print(f"Promedio mensual de la empresa: {pesos(promedio)}")
                print(f"Proyección anual estimada de la empresa: {pesos(operaciones.proyeccion_anual(totales, meses_registrados))}")
        elif opcion == opcion_salir:
            print("Volviendo al menú principal...")
        else:
            color_error("Opción inválida.")


def menu_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                  productos_id, productos_precio, matriz_vendedores,
                  matriz_productos, meses_registrados, meses):
    codigo_vendedor = pedir_entero("Ingrese su código de vendedor: ")
    posicion = operaciones.busqueda_secuencial(vendedores_id, codigo_vendedor)
    opciones = [
        "Registrar venta",
        "Consultar mi importe total vendido",
        "Consultar mi comisión",
        "Consultar mi proyección anual estimada",
        "Volver"
    ]
    opcion_salir = str(len(opciones))
    # Si el código no existe, el ciclo no se ejecuta
    opcion = opcion_salir if posicion == -1 else ""
    if posicion == -1:
        color_error("El código de vendedor no existe.")

    while opcion != opcion_salir:
        opcion = elegir_opcion(f"VENDEDOR: {vendedores_nombre[posicion]}", opciones)

        if opcion == "1":
            registrar_venta_menu(vendedores_id, productos_id, productos_precio, matriz_vendedores,
                                 matriz_productos, meses_registrados, meses, codigo_vendedor)
        elif opcion == "2":
            print(f"Mi importe total vendido: {pesos(sum(matriz_vendedores[posicion]))}")
        elif opcion == "3":
            print(f"Mi comisión: {pesos(operaciones.comision_vendedor(matriz_vendedores, vendedores_comision, posicion))}")
        elif opcion == "4":
            proyeccion = operaciones.proyeccion_anual(matriz_vendedores[posicion], meses_registrados)
            print("Todavía no hay meses procesados." if proyeccion is None else
                  f"Mi proyección anual estimada (según mi propio promedio mensual): {pesos(proyeccion)}")
        elif opcion == opcion_salir:
            print("Volviendo al menú principal...")
        else:
            color_error("Opción inválida.")


def main():
    (matriz_vendedores, matriz_productos, productos_precio, vendedores_nombre,
     productos_nombre, meses, vendedores_id, vendedores_comision,
     objetivo_mensual, productos_id, meses_registrados) = datos.creaciondatos()

    opcion = ""
    while opcion != "3":
        opcion = elegir_opcion("BLUE SQUAD SALESMATRIX", ["Administrador", "Vendedor", "Salir"])

        if opcion == "1":
            menu_administrador(vendedores_id, vendedores_nombre, vendedores_comision,
                               productos_id, productos_nombre, productos_precio,
                               matriz_vendedores, matriz_productos, meses_registrados,
                               meses, objetivo_mensual)
        elif opcion == "2":
            menu_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                          productos_id, productos_precio, matriz_vendedores,
                          matriz_productos, meses_registrados, meses)
        elif opcion == "3":
            print("Sistema finalizado.")
        else:
            color_error("Opción inválida.")


if __name__ == "__main__":
    main()
