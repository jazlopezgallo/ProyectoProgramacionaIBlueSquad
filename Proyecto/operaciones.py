# ---------------------------------------------------------------------------
# FUNCIONES ORIGINALES
# ---------------------------------------------------------------------------

def es_entero(valor):
    valor_str = str(valor).strip()
    if valor_str.isdigit() == False:
        return [False, -1]
    numero = int(valor_str)
    return [True, numero]


def texto_valido(texto):
    texto_limpio = str(texto).strip().capitalize()
    if texto_limpio == "":
        return [False, ""]
    return [True, texto_limpio]


def busqueda_secuencial(lista, buscado):
    for i in range(len(lista)):
        if lista[i] == buscado:
            return i
    return -1


def crear_meses_registrados():
    return [False for _ in range(12)]


# ---------------------------------------------------------------------------
# WRAPPERS DE VALIDACIÓN
# Cada uno devuelve [ok, valor_limpio, mensaje_error]
# ---------------------------------------------------------------------------

def validar_numero_positivo(valor, mensaje_error):
    """Valida que sea entero y mayor a 0."""
    resultado = es_entero(valor)
    if resultado[0] == False or resultado[1] <= 0:
        return [False, -1, mensaje_error]
    return [True, resultado[1], ""]


def validar_numero_en_rango(valor, minimo, maximo, mensaje_error):
    """Valida que sea entero y esté dentro de [minimo, maximo]."""
    resultado = es_entero(valor)
    if resultado[0] == False or resultado[1] < minimo or resultado[1] > maximo:
        return [False, -1, mensaje_error]
    return [True, resultado[1], ""]


def validar_texto_no_vacio(texto, mensaje_error):
    """Valida que el texto no quede vacío tras limpiarlo."""
    resultado = texto_valido(texto)
    if resultado[0] == False:
        return [False, "", mensaje_error]
    return [True, resultado[1], ""]


def validar_no_duplicado(lista, valor, mensaje_error):
    """Valida que 'valor' NO esté ya en 'lista' (para altas)."""
    if busqueda_secuencial(lista, valor) != -1:
        return [False, valor, mensaje_error]
    return [True, valor, ""]


def validar_existe(lista, valor, mensaje_error):
    """Valida que 'valor' SÍ esté en 'lista' y devuelve su posición (para bajas)."""
    posicion = busqueda_secuencial(lista, valor)
    if posicion == -1:
        return [False, -1, mensaje_error]
    return [True, posicion, ""]


# ---------------------------------------------------------------------------
# ALTA Y BAJA DE VENDEDORES
# ---------------------------------------------------------------------------

def agregar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                     matriz_vendedores, codigo, nombre, comision):

    estado_actual = (vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores)

    validacion = validar_numero_positivo(codigo, "Error: el código debe ser numérico y mayor que cero.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    codigo = validacion[1]

    validacion = validar_texto_no_vacio(nombre, "Error: el nombre no puede estar vacío.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    nombre = validacion[1]

    validacion = validar_numero_en_rango(comision, 0, 100, "Error: comisión inválida (debe ser entre 0 y 100).")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    comision = validacion[1]

    validacion = validar_no_duplicado(vendedores_id, codigo, "Error: código de vendedor ya registrado.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])

    validacion = validar_no_duplicado(vendedores_nombre, nombre, "Error: el nombre ya existe.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])

    # Inserción
    id_nuevo = vendedores_id[:] + [codigo]
    nombre_nuevo = vendedores_nombre[:] + [nombre]
    comision_nueva = vendedores_comision[:] + [comision / 100]
    matriz_nueva = [fila[:] for fila in matriz_vendedores] + [[0] * 12]

    return id_nuevo, nombre_nuevo, comision_nueva, matriz_nueva, True, f"Vendedor '{nombre}' agregado exitosamente."


def eliminar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, codigo):

    estado_actual = (vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores)

    validacion = validar_numero_positivo(codigo, "Error: código inválido.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    codigo = validacion[1]

    validacion = validar_existe(vendedores_id, codigo, "Error: el vendedor no existe.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    posicion = validacion[1]

    nombre = vendedores_nombre[posicion]
    id_nuevo = vendedores_id[:posicion] + vendedores_id[posicion + 1:]
    nombre_nuevo = vendedores_nombre[:posicion] + vendedores_nombre[posicion + 1:]
    comision_nueva = vendedores_comision[:posicion] + vendedores_comision[posicion + 1:]
    matriz_nueva = [fila[:] for i, fila in enumerate(matriz_vendedores) if i != posicion]

    return id_nuevo, nombre_nuevo, comision_nueva, matriz_nueva, True, f"Vendedor '{nombre}' eliminado."


# ---------------------------------------------------------------------------
# ALTA Y BAJA DE PRODUCTOS
# ---------------------------------------------------------------------------

def agregar_producto(productos_id, productos_nombre, productos_precio,
                     matriz_productos, codigo, nombre, precio):

    estado_actual = (productos_id, productos_nombre, productos_precio, matriz_productos)

    validacion = validar_numero_positivo(codigo, "Error: código inválido.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    codigo = validacion[1]

    validacion = validar_texto_no_vacio(nombre, "Error: nombre vacío.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    nombre = validacion[1]

    validacion = validar_numero_positivo(precio, "Error: precio inválido.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    precio = validacion[1]

    validacion = validar_no_duplicado(productos_id, codigo, "Error: código de producto ya registrado.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])

    validacion = validar_no_duplicado(productos_nombre, nombre, "Error: producto ya existente.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])

    # Inserción
    id_nuevo = productos_id[:] + [codigo]
    nombre_nuevo = productos_nombre[:] + [nombre]
    precio_nuevo = productos_precio[:] + [precio]
    matriz_nueva = [fila[:] for fila in matriz_productos] + [[0] * 12]

    return id_nuevo, nombre_nuevo, precio_nuevo, matriz_nueva, True, f"Producto '{nombre}' agregado."


def eliminar_producto(productos_id, productos_nombre, productos_precio, matriz_productos, codigo):

    estado_actual = (productos_id, productos_nombre, productos_precio, matriz_productos)

    validacion = validar_numero_positivo(codigo, "Error: código inválido.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    codigo = validacion[1]

    validacion = validar_existe(productos_id, codigo, "Error: el producto no existe.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    posicion = validacion[1]

    nombre = productos_nombre[posicion]
    id_nuevo = productos_id[:posicion] + productos_id[posicion + 1:]
    nombre_nuevo = productos_nombre[:posicion] + productos_nombre[posicion + 1:]
    precio_nuevo = productos_precio[:posicion] + productos_precio[posicion + 1:]
    matriz_nueva = [fila[:] for i, fila in enumerate(matriz_productos) if i != posicion]

    return id_nuevo, nombre_nuevo, precio_nuevo, matriz_nueva, True, f"Producto '{nombre}' eliminado."


# ---------------------------------------------------------------------------
# REGISTRO DE VENTAS
# ---------------------------------------------------------------------------

def registrar_venta(vendedores_id, productos_id, productos_precio,
                    matriz_vendedores, matriz_productos, meses_registrados,
                    codigo_vendedor, codigo_producto, mes, cantidad):

    estado_actual = (matriz_vendedores, matriz_productos, meses_registrados)

    validacion = validar_numero_positivo(codigo_vendedor, "Error: código de vendedor no válido.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    codigo_vendedor = validacion[1]

    validacion = validar_numero_positivo(codigo_producto, "Error: código de producto no válido.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    codigo_producto = validacion[1]

    validacion = validar_numero_en_rango(mes, 1, 12, "Error: el mes debe estar entre 1 y 12.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    mes = validacion[1]

    validacion = validar_numero_positivo(cantidad, "Error: cantidad no válida.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    cantidad = validacion[1]

    validacion = validar_existe(vendedores_id, codigo_vendedor, "Error: el vendedor no existe.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    posicion_vendedor = validacion[1]

    validacion = validar_existe(productos_id, codigo_producto, "Error: el producto no existe.")
    if validacion[0] == False:
        return estado_actual + (False, validacion[2])
    posicion_producto = validacion[1]

    importe = cantidad * productos_precio[posicion_producto]

    matriz_vendedores_nueva = [fila[:] for fila in matriz_vendedores]
    matriz_productos_nueva = [fila[:] for fila in matriz_productos]
    meses_registrados_nuevo = meses_registrados[:]

    matriz_vendedores_nueva[posicion_vendedor][mes - 1] += importe
    matriz_productos_nueva[posicion_producto][mes - 1] += cantidad
    meses_registrados_nuevo[mes - 1] = True

    return matriz_vendedores_nueva, matriz_productos_nueva, meses_registrados_nuevo, True, f"Venta registrada: ${importe}."

# ---------------------------------------------------------------------------
# REPORTES Y ESTADÍSTICAS (Integrado)
# ---------------------------------------------------------------------------

def producto_mas_vendido(productos_nombre, matriz_productos):
    totales = [sum(fila) for fila in matriz_productos]
    if not totales or max(totales) == 0:
        return [], 0
    maximo = max(totales)
    return [productos_nombre[i] for i, total in enumerate(totales) if total == maximo], maximo


def vendedor_mayor_volumen(vendedores_nombre, matriz_vendedores):
    totales = [sum(fila) for fila in matriz_vendedores]
    if not totales or max(totales) == 0:
        return [], 0
    maximo = max(totales)
    return [vendedores_nombre[i] for i, total in enumerate(totales) if total == maximo], maximo


def mes_mayor_unidades(matriz_productos, meses_registrados, meses):
    totales = [sum(fila[i] for fila in matriz_productos) if meses_registrados[i] else -1
               for i in range(len(meses))]
    if not totales or max(totales) < 0:
        return [], 0
    maximo = max(totales)
    return [meses[i] for i, total in enumerate(totales) if total == maximo], maximo


def ranking_vendedores(vendedores_nombre, matriz_vendedores):
    totales = [sum(fila) for fila in matriz_vendedores]
    return sorted(zip(vendedores_nombre, totales), key=lambda dato: dato[1], reverse=True)


def top_vendedores(ranking, cantidad):
    return ranking[:cantidad]


def cumplimiento_objetivo_mes(vendedores_nombre, matriz_vendedores,
                               mes, objetivo_mensual, meses_registrados):
    if mes < 1 or mes > len(meses_registrados):
        return [], [], False
    if not meses_registrados[mes - 1]:
        return [], [], False

    alcanzaron = [nombre for nombre, fila in zip(vendedores_nombre, matriz_vendedores)
                  if fila[mes - 1] >= objetivo_mensual]
    no_alcanzaron = [nombre for nombre, fila in zip(vendedores_nombre, matriz_vendedores)
                     if fila[mes - 1] < objetivo_mensual]
    return alcanzaron, no_alcanzaron, True


def total_importe_vendedor(matriz_vendedores, posicion):
    return sum(matriz_vendedores[posicion])


def comision_vendedor(matriz_vendedores, vendedores_comision, posicion):
    return total_importe_vendedor(matriz_vendedores, posicion) * vendedores_comision[posicion]


def proyeccion_vendedor(matriz_vendedores, posicion, meses_registrados):
    cantidad_meses = sum(meses_registrados)
    if cantidad_meses == 0:
        return None
    promedio = sum(matriz_vendedores[posicion][i] for i in range(len(meses_registrados))
                   if meses_registrados[i]) / cantidad_meses
    return promedio * 12