"""
operaciones.py
--------------
Contiene toda la lógica de negocio, validaciones, búsqueda, altas, bajas, 
registro de ventas y cálculos para los informes. 
"""

# ---------------------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN (Retornan listas [Booleano, Valor])
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

# ---------------------------------------------------------------------------
# BÚSQUEDA SECUENCIAL
# ---------------------------------------------------------------------------

def busqueda_secuencial(lista, buscado):
    for i in range(len(lista)):
        if lista[i] == buscado:
            return i
    return -1

def crear_meses_registrados():
    return [False for _ in range(12)]

# ---------------------------------------------------------------------------
# ALTA Y BAJA DE VENDEDORES
# ---------------------------------------------------------------------------

def agregar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                     matriz_vendedores, codigo, nombre, comision):
    
    # 1. Validaciones y extracción de datos limpios
    validacion_codigo = es_entero(codigo)
    if validacion_codigo[0] == False or validacion_codigo[1] <= 0:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el código debe ser numérico y mayor que cero."
    codigo = validacion_codigo[1]
    
    validacion_nombre = texto_valido(nombre)
    if validacion_nombre[0] == False:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el nombre no puede estar vacío."
    nombre = validacion_nombre[1]
    
    validacion_comision = es_entero(comision)
    if validacion_comision[0] == False:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: comisión inválida."
    comision = validacion_comision[1]
    
    # 2. Lógica
    if comision > 100:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: la comisión no puede ser mayor al 100%."
    if busqueda_secuencial(vendedores_id, codigo) != -1:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: código de vendedor ya registrado."
    if busqueda_secuencial(vendedores_nombre, nombre) != -1:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el nombre ya existe."
    
    # 3. Inserción
    id_nuevo = vendedores_id[:] + [codigo]
    nombre_nuevo = vendedores_nombre[:] + [nombre]
    comision_nueva = vendedores_comision[:] + [comision / 100]
    matriz_nueva = [fila[:] for fila in matriz_vendedores] + [[0] * 12]
    
    return id_nuevo, nombre_nuevo, comision_nueva, matriz_nueva, True, f"Vendedor '{nombre}' agregado exitosamente."

def eliminar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, codigo):
    validacion_codigo = es_entero(codigo)
    if validacion_codigo[0] == False or validacion_codigo[1] <= 0:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: código inválido."
    codigo = validacion_codigo[1]
    
    posicion = busqueda_secuencial(vendedores_id, codigo)
    if posicion == -1:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el vendedor no existe."
    
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
    
    # 1. Validaciones
    validacion_codigo = es_entero(codigo)
    if validacion_codigo[0] == False or validacion_codigo[1] <= 0:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: código inválido."
    codigo = validacion_codigo[1]
    
    validacion_nombre = texto_valido(nombre)
    if validacion_nombre[0] == False:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: nombre vacío."
    nombre = validacion_nombre[1]
    
    validacion_precio = es_entero(precio)
    if validacion_precio[0] == False or validacion_precio[1] <= 0:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: precio inválido."
    precio = validacion_precio[1]
    
    # 2. Lógica
    if busqueda_secuencial(productos_id, codigo) != -1:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: código de producto ya registrado."
    if busqueda_secuencial(productos_nombre, nombre) != -1:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: producto ya existente."
    
    # 3. Inserción
    id_nuevo = productos_id[:] + [codigo]
    nombre_nuevo = productos_nombre[:] + [nombre]
    precio_nuevo = productos_precio[:] + [precio]
    matriz_nueva = [fila[:] for fila in matriz_productos] + [[0] * 12]
    
    return id_nuevo, nombre_nuevo, precio_nuevo, matriz_nueva, True, f"Producto '{nombre}' agregado."

def eliminar_producto(productos_id, productos_nombre, productos_precio, matriz_productos, codigo):
    validacion_codigo = es_entero(codigo)
    if validacion_codigo[0] == False or validacion_codigo[1] <= 0:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: código inválido."
    codigo = validacion_codigo[1]
    
    posicion = busqueda_secuencial(productos_id, codigo)
    if posicion == -1:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el producto no existe."
    
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
    
    # 1. Validaciones
    validacion_vend = es_entero(codigo_vendedor)
    if validacion_vend[0] == False or validacion_vend[1] <= 0:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: código de vendedor no válido."
    codigo_vendedor = validacion_vend[1]
    
    validacion_prod = es_entero(codigo_producto)
    if validacion_prod[0] == False or validacion_prod[1] <= 0:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: código de producto no válido."
    codigo_producto = validacion_prod[1]
    
    validacion_mes = es_entero(mes)
    if validacion_mes[0] == False or validacion_mes[1] <= 0:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: mes no válido."
    mes = validacion_mes[1]
    
    validacion_cant = es_entero(cantidad)
    if validacion_cant[0] == False or validacion_cant[1] <= 0:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: cantidad no válida."
    cantidad = validacion_cant[1]
    
    # 2. Lógica
    if mes < 1 or mes > 12:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el mes debe estar entre 1 y 12."
    
    posicion_vendedor = busqueda_secuencial(vendedores_id, codigo_vendedor)
    posicion_producto = busqueda_secuencial(productos_id, codigo_producto)
    
    if posicion_vendedor == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el vendedor no existe."
    if posicion_producto == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el producto no existe."
    
    importe = cantidad * productos_precio[posicion_producto]
    
    matriz_vendedores_nueva = [fila[:] for fila in matriz_vendedores]
    matriz_productos_nueva = [fila[:] for fila in matriz_productos]
    meses_registrados_nuevo = meses_registrados[:]
    
    matriz_vendedores_nueva[posicion_vendedor][mes - 1] += importe
    matriz_productos_nueva[posicion_producto][mes - 1] += cantidad
    meses_registrados_nuevo[mes - 1] = True
    
    return matriz_vendedores_nueva, matriz_productos_nueva, meses_registrados_nuevo, True, f"Venta registrada: ${importe}."


# ---------------------------------------------------------------------------
# FUNCIONES AUXILIARES (Para no repetir código)
# ---------------------------------------------------------------------------
def _obtener_maximo_filas(nombres, matriz):
    """Suma cada fila de una matriz y devuelve quiénes tienen el valor máximo."""
    if not nombres:
        return [], 0
    totales = [sum(fila) for fila in matriz]
    maximo = max(totales)
    nombres_max = [nombres[i] for i, total in enumerate(totales) if total == maximo]
    return nombres_max, maximo

def _obtener_maximo_columnas(matriz, meses_registrados, meses_nombres):
    """Suma cada columna (mes) de una matriz y devuelve cuáles tienen el valor máximo."""
    if not any(meses_registrados):
        return [], 0
    
    # En lugar de usar índices complejos, extraemos el mes de cada fila directamente
    totales_por_mes = [sum(fila[m] for fila in matriz) for m in range(12)]
    maximo = max(totales_por_mes)
    meses_max = [meses_nombres[i] for i, total in enumerate(totales_por_mes) if total == maximo and meses_registrados[i]]
    return meses_max, maximo

# ---------------------------------------------------------------------------
# CÁLCULOS E INFORMES GENERALES
# ---------------------------------------------------------------------------

def total_anual_empresa(matriz_vendedores):
    return sum(sum(fila) for fila in matriz_vendedores)

def promedio_general_empresa(matriz_vendedores, meses_registrados):
    cant_meses = sum(meses_registrados)
    # Se simplificó a una sola línea (Operador Ternario)
    return total_anual_empresa(matriz_vendedores) / cant_meses if cant_meses > 0 else None

def proyeccion_general(matriz_vendedores, meses_registrados):
    promedio = promedio_general_empresa(matriz_vendedores, meses_registrados)
    return promedio * 12 if promedio else None

# Ahora estas 4 funciones simplemente llaman a las auxiliares de arriba
def producto_mas_vendido(productos_nombre, matriz_productos):
    return _obtener_maximo_filas(productos_nombre, matriz_productos)

def vendedor_mayor_volumen(vendedores_nombre, matriz_vendedores):
    return _obtener_maximo_filas(vendedores_nombre, matriz_vendedores)

def mes_mayor_facturacion(matriz_vendedores, meses_registrados, meses_nombres):
    return _obtener_maximo_columnas(matriz_vendedores, meses_registrados, meses_nombres)

def mes_mayor_unidades(matriz_productos, meses_registrados, meses_nombres):
    return _obtener_maximo_columnas(matriz_productos, meses_registrados, meses_nombres)

# ---------------------------------------------------------------------------
# RANKING Y OBJETIVOS
# ---------------------------------------------------------------------------

def ranking_vendedores(vendedores_nombre, matriz_vendedores):
    totales = [(vendedores_nombre[i], sum(matriz_vendedores[i])) for i in range(len(vendedores_nombre))]
    # Reemplazamos el "Burbuja" por el ordenamiento nativo de Python (mucho más rápido)
    # Ordena la lista de mayor a menor basándose en el importe (x[1])
    return sorted(totales, key=lambda x: x[1], reverse=True)

def top_vendedores(ranking, cantidad):
    return ranking[:cantidad]

def cumplimiento_objetivo_mes(vendedores_nombre, matriz_vendedores, mes, objetivo):
    alcanzaron, no_alcanzaron = [], []
    
    # Usamos zip() para iterar nombre y fila al mismo tiempo sin necesidad de un índice 'i'
    for nombre, fila in zip(vendedores_nombre, matriz_vendedores):
        if fila[mes - 1] >= objetivo:
            alcanzaron.append(nombre)
        else:
            no_alcanzaron.append(nombre)
            
    return alcanzaron, no_alcanzaron

# ---------------------------------------------------------------------------
# INFORMES INDIVIDUALES (Vendedor)
# ---------------------------------------------------------------------------

def total_importe_vendedor(matriz_vendedores, posicion):
    return sum(matriz_vendedores[posicion])

def comision_vendedor(matriz_vendedores, vendedores_comision, posicion):
    return total_importe_vendedor(matriz_vendedores, posicion) * vendedores_comision[posicion]

def promedio_mensual_vendedor(matriz_vendedores, posicion, meses_registrados):
    cant_meses = sum(meses_registrados)
    return total_importe_vendedor(matriz_vendedores, posicion) / cant_meses if cant_meses > 0 else None

def mejor_mes_vendedor(matriz_vendedores, posicion, meses_nombres):
    fila = matriz_vendedores[posicion]
    maximo = max(fila)
    meses_max = [meses_nombres[i] for i, val in enumerate(fila) if val == maximo]
    return meses_max, maximo

def proyeccion_vendedor(matriz_vendedores, posicion, meses_registrados):
    promedio = promedio_mensual_vendedor(matriz_vendedores, posicion, meses_registrados)
    return promedio * 12 if promedio else None