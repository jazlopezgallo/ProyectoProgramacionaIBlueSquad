# ---------------------------------------------------------------------------
# FUNCIONES BÁSICAS Y VALIDACIONES
# Las que devuelven datos de distinto tipo usan tuplas (no listas).
# Los wrappers de validación devuelven (ok, valor_limpio, mensaje_error).
# ---------------------------------------------------------------------------

def es_entero(valor):
    """Devuelve (es_valido, numero)."""
    valor_str = str(valor).strip()
    return (valor_str.isdigit(), int(valor_str) if valor_str.isdigit() else -1)


def texto_valido(texto):
    """Devuelve (es_valido, texto_limpio)."""
    texto_limpio = str(texto).strip().capitalize()
    return (texto_limpio != "", texto_limpio)


def busqueda_secuencial(lista, buscado):
    """Posición de 'buscado' en 'lista' o -1 si no está."""
    return lista.index(buscado) if buscado in lista else -1


def validar_numero(valor, minimo, maximo, mensaje_error):
    """Entero dentro de [minimo, maximo]. Con maximo = None no hay tope."""
    ok, numero = es_entero(valor)
    ok = ok and numero >= minimo and (maximo is None or numero <= maximo)
    return (ok, numero if ok else -1, "" if ok else mensaje_error)


def validar_texto(texto, mensaje_error):
    ok, texto_limpio = texto_valido(texto)
    return (ok, texto_limpio, "" if ok else mensaje_error)


def validar_no_duplicado(lista, valor, mensaje_error):
    """Para altas: 'valor' NO debe estar en 'lista'."""
    ok = valor not in lista
    return (ok, valor, "" if ok else mensaje_error)


def validar_existe(lista, valor, mensaje_error):
    """Para bajas y ventas: 'valor' SÍ debe estar en 'lista'. Devuelve su posición."""
    posicion = busqueda_secuencial(lista, valor)
    return (posicion != -1, posicion, "" if posicion != -1 else mensaje_error)


def primer_error(validaciones):
    """Mensaje de la primera validación fallida, o "" si todas son correctas."""
    errores = [validacion[2] for validacion in validaciones if not validacion[0]]
    return errores[0] if errores else ""


def resultado(error, mensaje_ok):
    """Arma la tupla (ok, mensaje) que devuelven todas las operaciones."""
    return (error == "", error if error else mensaje_ok)


# ---------------------------------------------------------------------------
# ALTA Y BAJA DE VENDEDORES Y PRODUCTOS
# Las listas paralelas y la matriz se modifican en el lugar (sin copias).
# ---------------------------------------------------------------------------

def agregar_elemento(ids, nombres, valores, matriz, codigo, nombre, v_valor, entidad):
    """Alta común a vendedores y productos. v_valor es la validación de la comisión o del precio."""
    v_codigo = validar_numero(codigo, 1, None, "Error: el código debe ser numérico y mayor que cero.")
    v_nombre = validar_texto(nombre, "Error: el nombre no puede estar vacío.")
    error = primer_error([v_codigo, v_nombre, v_valor,
                          validar_no_duplicado(ids, v_codigo[1], f"Error: código de {entidad} ya registrado."),
                          validar_no_duplicado(nombres, v_nombre[1], f"Error: el {entidad} ya existe.")])
    if error == "":
        ids.append(v_codigo[1])
        nombres.append(v_nombre[1])
        valores.append(v_valor[1])
        matriz.append([0] * 12)
    return resultado(error, f"{entidad.capitalize()} '{v_nombre[1]}' agregado.")


def agregar_vendedor(ids, nombres, comisiones, matriz, codigo, nombre, comision):
    """La comisión se ingresa como porcentaje (mayor a 0 y hasta 100) y se guarda como decimal."""
    ok, porcentaje, mensaje = validar_numero(comision, 1, 100, "Error: la comisión debe ser mayor a 0 y como máximo 100.")
    return agregar_elemento(ids, nombres, comisiones, matriz, codigo, nombre, (ok, porcentaje / 100, mensaje), "vendedor")


def agregar_producto(ids, nombres, precios, matriz, codigo, nombre, precio):
    v_precio = validar_numero(precio, 1, None, "Error: el precio debe ser mayor a 0.")
    return agregar_elemento(ids, nombres, precios, matriz, codigo, nombre, v_precio, "producto")


def eliminar_elemento(ids, nombres, valores, matriz, codigo, entidad):
    """Baja común a vendedores y productos. Solo se permite si no tiene ventas registradas,
    para no perder información histórica ni modificar los totales de la empresa."""
    ok, posicion, error = validar_existe(ids, codigo, f"Error: el {entidad} no existe.")
    if ok and sum(matriz[posicion]) > 0:
        error = f"Error: no se puede eliminar un {entidad} con ventas registradas."
    nombre = ""
    if error == "":
        nombre = nombres.pop(posicion)
        for lista in (ids, valores, matriz):
            lista.pop(posicion)
    return resultado(error, f"{entidad.capitalize()} '{nombre}' eliminado.")


# ---------------------------------------------------------------------------
# MESES PROCESADOS
# Regla: un mes pasa a procesado (True) cuando se registra una venta en él,
# o cuando el administrador lo cierra manualmente aunque no haya tenido ventas.
# ---------------------------------------------------------------------------

def procesar_mes(meses_registrados, meses, mes):
    ok, numero, error = validar_numero(mes, 1, 12, "Error: el mes debe estar entre 1 y 12.")
    if ok and meses_registrados[numero - 1]:
        error = f"{meses[numero - 1]} ya estaba marcado como procesado."
    if error == "":
        meses_registrados[numero - 1] = True
    return resultado(error, f"{meses[numero - 1]} marcado como procesado.")


# ---------------------------------------------------------------------------
# REGISTRO DE VENTAS
# Actualiza en conjunto la matriz de productos (unidades vendidas)
# y la matriz de vendedores (importe vendido).
# ---------------------------------------------------------------------------

def registrar_venta(vendedores_id, productos_id, productos_precio,
                    matriz_vendedores, matriz_productos, meses_registrados,
                    codigo_vendedor, codigo_producto, mes, cantidad):
    v_vendedor = validar_existe(vendedores_id, codigo_vendedor, "Error: el vendedor no existe.")
    v_producto = validar_existe(productos_id, codigo_producto, "Error: el producto no existe.")
    v_mes = validar_numero(mes, 1, 12, "Error: el mes debe estar entre 1 y 12.")
    v_cantidad = validar_numero(cantidad, 1, None, "Error: la cantidad debe ser mayor a 0.")
    error = primer_error([v_vendedor, v_producto, v_mes, v_cantidad])
    importe = 0
    if error == "":
        columna = v_mes[1] - 1
        importe = v_cantidad[1] * productos_precio[v_producto[1]]
        matriz_vendedores[v_vendedor[1]][columna] += importe
        matriz_productos[v_producto[1]][columna] += v_cantidad[1]
        meses_registrados[columna] = True
    return resultado(error, f"Venta registrada: ${importe}.")


# ---------------------------------------------------------------------------
# INFORMES E INDICADORES
# ---------------------------------------------------------------------------

def maximos(nombres, totales, minimo):
    """(nombres con el total máximo, máximo) contemplando empates.
    Si no hay totales válidos (>= minimo) devuelve ([], 0)."""
    maximo = max(totales) if totales else -1
    ganadores = [nombre for nombre, total in zip(nombres, totales) if total == maximo and maximo >= minimo]
    return (ganadores, maximo if ganadores else 0)


def mayor_total(nombres, matriz):
    """Producto más vendido (matriz de productos) o vendedor con mayor importe (matriz de vendedores)."""
    return maximos(nombres, [sum(fila) for fila in matriz], 1)


def totales_por_mes(matriz, meses_registrados):
    """Total de cada mes; los meses no procesados valen -1 para que no participen."""
    return [sum(columna) if registrado else -1
            for columna, registrado in zip(zip(*matriz), meses_registrados)]


def mes_mayor_total(matriz, meses_registrados, meses):
    """Mes con más unidades (matriz de productos) o mayor facturación (matriz de vendedores).
    En ambos casos solo participan los meses procesados."""
    return maximos(meses, totales_por_mes(matriz, meses_registrados), 0)


def ranking_vendedores(vendedores_nombre, matriz_vendedores):
    """Ranking descendente por importe vendido."""
    totales = [sum(fila) for fila in matriz_vendedores]
    return sorted(zip(vendedores_nombre, totales), key=lambda dato: dato[1], reverse=True)


def top_vendedores(ranking, cantidad):
    return ranking[:cantidad]


def cumplimiento_objetivo_mes(vendedores_nombre, matriz_vendedores, mes, objetivo_mensual, meses_registrados):
    """(alcanzaron, no_alcanzaron, mes_procesado) para el mes elegido."""
    procesado = 1 <= mes <= len(meses_registrados) and meses_registrados[mes - 1]
    alcanzaron = [nombre for nombre, fila in zip(vendedores_nombre, matriz_vendedores)
                  if procesado and fila[mes - 1] >= objetivo_mensual]
    no_alcanzaron = [nombre for nombre, fila in zip(vendedores_nombre, matriz_vendedores)
                     if procesado and fila[mes - 1] < objetivo_mensual]
    return (alcanzaron, no_alcanzaron, procesado)


def promedio_mensual(valores, meses_registrados):
    """Suma de los valores de los meses procesados / cantidad de meses procesados.
    - Empresa: valores = totales_por_mes(matriz_vendedores, meses_registrados).
    - Vendedor: valores = su propia fila de la matriz de vendedores.
    Devuelve None si todavía no hay meses procesados."""
    procesados = [valor for valor, registrado in zip(valores, meses_registrados) if registrado]
    return sum(procesados) / meses_registrados.count(True) if True in meses_registrados else None


def proyeccion_anual(valores, meses_registrados):
    """Estimación matemática: promedio mensual * 12."""
    promedio = promedio_mensual(valores, meses_registrados)
    return None if promedio is None else promedio * 12


def comision_vendedor(matriz_vendedores, vendedores_comision, posicion):
    return sum(matriz_vendedores[posicion]) * vendedores_comision[posicion]
