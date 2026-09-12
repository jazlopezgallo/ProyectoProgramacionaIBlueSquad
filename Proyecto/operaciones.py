"""
operaciones.py
--------------
Contiene toda la lógica del problema: validaciones, búsquedas, cálculos
e informes. Ninguna función de este módulo utiliza input() ni print():
reciben datos por parámetro y devuelven resultados mediante return.

Tampoco se utiliza manejo de excepciones (try/except): todas las
validaciones se resuelven con estructuras condicionales.
"""


# ---------------------------------------------------------------------------
# VALIDACIONES DE TEXTO Y NÚMEROS (sin try/except)
# ---------------------------------------------------------------------------

def es_entero(texto):
    """
    Determina si una cadena representa un número entero (positivo,
    negativo o cero), sin usar try/except.
    """
    texto = texto.strip()
    if texto == "":
        return False
    if texto[0] in "+-":
        texto = texto[1:]
    return texto.isdigit()


def texto_valido(texto):
    """Determina si una cadena no está vacía luego de quitar espacios."""
    return texto.strip() != ""


# ---------------------------------------------------------------------------
# CREACIÓN DE ESTRUCTURAS
# ---------------------------------------------------------------------------

def crear_matriz(cantidad_filas):
    """Crea una matriz de ceros con 'cantidad_filas' filas y 12 columnas (meses)."""
    return [[0 for columna in range(12)] for fila in range(cantidad_filas)]


def crear_meses_registrados():
    """Crea la lista de estado de los 12 meses, todos en False (no procesados)."""
    return [False for _ in range(12)]


# ---------------------------------------------------------------------------
# BÚSQUEDAS
# ---------------------------------------------------------------------------

def buscar_vendedor(vendedores_id, codigo):
    """Busca un vendedor por código. Devuelve su posición o -1 si no existe."""
    if codigo in vendedores_id:
        return vendedores_id.index(codigo)
    return -1


def buscar_producto(productos_id, codigo):
    """Busca un producto por código. Devuelve su posición o -1 si no existe."""
    if codigo in productos_id:
        return productos_id.index(codigo)
    return -1


# ---------------------------------------------------------------------------
# ALTA Y BAJA DE VENDEDORES
# ---------------------------------------------------------------------------

def agregar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                      matriz_vendedores, codigo, nombre, comision):
    """
    Valida y agrega un nuevo vendedor.
    Reglas: código numérico > 0 y no repetido; nombre no vacío y no
    duplicado; comisión > 0% y <= 100% (se guarda como decimal).

    Devuelve:
        (vendedores_id, vendedores_nombre, vendedores_comision,
         matriz_vendedores, exito, mensaje)
    """
    nombre = nombre.strip().capitalize()

    if codigo <= 0:
        return (vendedores_id, vendedores_nombre, vendedores_comision,
                matriz_vendedores, False, "Error: el código debe ser mayor que cero.")

    if codigo in vendedores_id:
        return (vendedores_id, vendedores_nombre, vendedores_comision,
                matriz_vendedores, False, "Error: el código ya se encuentra registrado.")

    if not texto_valido(nombre):
        return (vendedores_id, vendedores_nombre, vendedores_comision,
                matriz_vendedores, False, "Error: el nombre no puede estar vacío.")

    if nombre in vendedores_nombre:
        return (vendedores_id, vendedores_nombre, vendedores_comision,
                matriz_vendedores, False, "Error: el nombre ya se encuentra registrado.")

    if comision <= 0 or comision > 100:
        return (vendedores_id, vendedores_nombre, vendedores_comision,
                matriz_vendedores, False,
                "Error: la comisión debe ser mayor que 0% y menor o igual a 100%.")

    id_nuevo = vendedores_id[:] + [codigo]
    nombre_nuevo = vendedores_nombre[:] + [nombre]
    comision_nueva = vendedores_comision[:] + [comision / 100]
    matriz_nueva = [fila[:] for fila in matriz_vendedores] + [[0] * 12]

    mensaje = f"Vendedor '{nombre}' agregado con éxito (código {codigo})."
    return id_nuevo, nombre_nuevo, comision_nueva, matriz_nueva, True, mensaje


def eliminar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                       matriz_vendedores, codigo):
    """
    Elimina un vendedor por código, manteniendo sincronizadas las listas
    paralelas y la matriz de vendedores.

    Devuelve:
        (vendedores_id, vendedores_nombre, vendedores_comision,
         matriz_vendedores, exito, mensaje)
    """
    posicion = buscar_vendedor(vendedores_id, codigo)
    if posicion == -1:
        return (vendedores_id, vendedores_nombre, vendedores_comision,
                matriz_vendedores, False, "Error: el vendedor no existe.")

    nombre = vendedores_nombre[posicion]
    id_nuevo = vendedores_id[:posicion] + vendedores_id[posicion + 1:]
    nombre_nuevo = vendedores_nombre[:posicion] + vendedores_nombre[posicion + 1:]
    comision_nueva = vendedores_comision[:posicion] + vendedores_comision[posicion + 1:]
    matriz_nueva = [fila[:] for i, fila in enumerate(matriz_vendedores) if i != posicion]

    mensaje = f"Vendedor '{nombre}' eliminado del sistema."
    return id_nuevo, nombre_nuevo, comision_nueva, matriz_nueva, True, mensaje


# ---------------------------------------------------------------------------
# ALTA Y BAJA DE PRODUCTOS
# ---------------------------------------------------------------------------

def agregar_producto(productos_id, productos_nombre, productos_precio,
                      matriz_productos, codigo, nombre, precio):
    """
    Valida y agrega un nuevo producto.
    Reglas: código numérico > 0 y no repetido; nombre no vacío y no
    duplicado; precio numérico > 0.

    Devuelve:
        (productos_id, productos_nombre, productos_precio,
         matriz_productos, exito, mensaje)
    """
    nombre = nombre.strip().capitalize()

    if codigo <= 0:
        return (productos_id, productos_nombre, productos_precio,
                matriz_productos, False, "Error: el código debe ser mayor que cero.")

    if codigo in productos_id:
        return (productos_id, productos_nombre, productos_precio,
                matriz_productos, False, "Error: el código ya se encuentra registrado.")

    if not texto_valido(nombre):
        return (productos_id, productos_nombre, productos_precio,
                matriz_productos, False, "Error: el nombre no puede estar vacío.")

    if nombre in productos_nombre:
        return (productos_id, productos_nombre, productos_precio,
                matriz_productos, False, "Error: el producto ya se encuentra registrado.")

    if precio <= 0:
        return (productos_id, productos_nombre, productos_precio,
                matriz_productos, False, "Error: el precio debe ser mayor que cero.")

    id_nuevo = productos_id[:] + [codigo]
    nombre_nuevo = productos_nombre[:] + [nombre]
    precio_nuevo = productos_precio[:] + [precio]
    matriz_nueva = [fila[:] for fila in matriz_productos] + [[0] * 12]

    mensaje = f"Producto '{nombre}' agregado con éxito (código {codigo})."
    return id_nuevo, nombre_nuevo, precio_nuevo, matriz_nueva, True, mensaje


def eliminar_producto(productos_id, productos_nombre, productos_precio,
                       matriz_productos, codigo):
    """
    Elimina un producto por código, manteniendo sincronizadas las listas
    paralelas y la matriz de productos.

    Devuelve:
        (productos_id, productos_nombre, productos_precio,
         matriz_productos, exito, mensaje)
    """
    posicion = buscar_producto(productos_id, codigo)
    if posicion == -1:
        return (productos_id, productos_nombre, productos_precio,
                matriz_productos, False, "Error: el producto no existe.")

    nombre = productos_nombre[posicion]
    id_nuevo = productos_id[:posicion] + productos_id[posicion + 1:]
    nombre_nuevo = productos_nombre[:posicion] + productos_nombre[posicion + 1:]
    precio_nuevo = productos_precio[:posicion] + productos_precio[posicion + 1:]
    matriz_nueva = [fila[:] for i, fila in enumerate(matriz_productos) if i != posicion]

    mensaje = f"Producto '{nombre}' eliminado del sistema."
    return id_nuevo, nombre_nuevo, precio_nuevo, matriz_nueva, True, mensaje


# ---------------------------------------------------------------------------
# REGISTRO DE VENTAS
# ---------------------------------------------------------------------------

def registrar_venta(vendedores_id, productos_id, productos_precio,
                     matriz_vendedores, matriz_productos, meses_registrados,
                     codigo_vendedor, codigo_producto, mes, cantidad):
    """
    Valida y registra una venta. Si alguna validación falla, no modifica
    ninguna matriz y devuelve el motivo del error.

    Devuelve:
        (matriz_vendedores, matriz_productos, meses_registrados,
         exito, mensaje)
    """
    posicion_vendedor = buscar_vendedor(vendedores_id, codigo_vendedor)
    if posicion_vendedor == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, \
            "Error: el vendedor no existe."

    posicion_producto = buscar_producto(productos_id, codigo_producto)
    if posicion_producto == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, \
            "Error: el producto no existe."

    if mes < 1 or mes > 12:
        return matriz_vendedores, matriz_productos, meses_registrados, False, \
            "Error: el mes debe estar entre 1 y 12."

    if cantidad <= 0:
        return matriz_vendedores, matriz_productos, meses_registrados, False, \
            "Error: la cantidad debe ser mayor que cero."

    precio_unitario = productos_precio[posicion_producto]
    importe = cantidad * precio_unitario

    matriz_vendedores_nueva = [fila[:] for fila in matriz_vendedores]
    matriz_productos_nueva = [fila[:] for fila in matriz_productos]

    matriz_vendedores_nueva[posicion_vendedor][mes - 1] += importe
    matriz_productos_nueva[posicion_producto][mes - 1] += cantidad

    meses_registrados_nuevo = meses_registrados[:]
    meses_registrados_nuevo[mes - 1] = True

    mensaje = f"Venta registrada: {cantidad} unidades, importe ${importe}."
    return matriz_vendedores_nueva, matriz_productos_nueva, meses_registrados_nuevo, True, mensaje


# ---------------------------------------------------------------------------
# CONSULTAS E INDICADORES
# ---------------------------------------------------------------------------

def meses_procesados(meses_registrados):
    """Devuelve la lista de índices (0 a 11) de los meses ya registrados."""
    return [i for i in range(len(meses_registrados)) if meses_registrados[i]]


def total_importe_vendedor(matriz_vendedores, indice):
    """Importe total acumulado vendido por un vendedor (suma de sus 12 meses)."""
    return sum(matriz_vendedores[indice])


def total_unidades_producto(matriz_productos, indice):
    """Cantidad total de unidades vendidas de un producto (suma de sus 12 meses)."""
    return sum(matriz_productos[indice])


def total_anual_empresa(matriz_vendedores):
    """Importe total vendido por toda la empresa."""
    return sum(sum(fila) for fila in matriz_vendedores)


def promedio_mensual_vendedor(matriz_vendedores, indice, meses_registrados):
    """
    Promedio mensual de un vendedor, considerando únicamente los meses
    ya registrados/procesados por el sistema (no los 12 meses del año).
    Devuelve None si todavía no hay ningún mes registrado.
    """
    indices = meses_procesados(meses_registrados)
    if len(indices) == 0:
        return None
    total = sum(matriz_vendedores[indice][i] for i in indices)
    return total / len(indices)


def promedio_general_empresa(matriz_vendedores, meses_registrados):
    """
    Promedio general de importe vendido por la empresa, considerando
    únicamente los meses ya registrados. Devuelve None si no hay
    vendedores o no hay meses registrados.
    """
    indices = meses_procesados(meses_registrados)
    if len(indices) == 0 or len(matriz_vendedores) == 0:
        return None
    total = sum(matriz_vendedores[v][i] for v in range(len(matriz_vendedores)) for i in indices)
    return total / (len(indices) * len(matriz_vendedores))


def comision_vendedor(matriz_vendedores, vendedores_comision, indice):
    """Comisión ganada por un vendedor según su importe total y su porcentaje."""
    importe = total_importe_vendedor(matriz_vendedores, indice)
    return importe * vendedores_comision[indice]


def proyeccion_vendedor(matriz_vendedores, indice, meses_registrados):
    """Proyección anual estimada de un vendedor: promedio mensual x 12."""
    promedio = promedio_mensual_vendedor(matriz_vendedores, indice, meses_registrados)
    if promedio is None:
        return None
    return promedio * 12


def proyeccion_general(matriz_vendedores, meses_registrados):
    """Proyección anual estimada de la empresa: promedio general x 12."""
    promedio = promedio_general_empresa(matriz_vendedores, meses_registrados)
    if promedio is None:
        return None
    return promedio * 12


def producto_mas_vendido(productos_nombre, matriz_productos):
    """
    Determina el/los producto(s) más vendido(s) según unidades totales.
    Si hay empate, devuelve todos los productos que comparten el máximo.

    Devuelve: (lista_de_nombres, cantidad_maxima)
    """
    if len(productos_nombre) == 0:
        return [], 0
    totales = [sum(fila) for fila in matriz_productos]
    maximo = max(totales)
    nombres = [productos_nombre[i] for i in range(len(productos_nombre)) if totales[i] == maximo]
    return nombres, maximo


def vendedor_mayor_volumen(vendedores_nombre, matriz_vendedores):
    """
    Determina el/los vendedor(es) con mayor importe total vendido.
    Si hay empate, devuelve todos los que comparten el máximo.

    Devuelve: (lista_de_nombres, importe_maximo)
    """
    if len(vendedores_nombre) == 0:
        return [], 0
    totales = [sum(fila) for fila in matriz_vendedores]
    maximo = max(totales)
    nombres = [vendedores_nombre[i] for i in range(len(vendedores_nombre)) if totales[i] == maximo]
    return nombres, maximo


def mejor_mes_vendedor(matriz_vendedores, indice, meses):
    """
    Determina el/los mejor(es) mes(es) de un vendedor según importe vendido.
    Si hay empate, devuelve todos los meses que comparten el máximo.

    Devuelve: (lista_de_meses, importe_maximo)
    """
    fila = matriz_vendedores[indice]
    maximo = max(fila)
    meses_maximos = [meses[i] for i in range(len(fila)) if fila[i] == maximo]
    return meses_maximos, maximo


def mes_mayor_unidades(matriz_productos, meses_registrados, meses):
    """
    Determina el/los mes(es) con mayor cantidad de unidades vendidas,
    considerando solo los meses ya registrados.

    Devuelve: (lista_de_meses, cantidad_maxima)
    """
    indices = meses_procesados(meses_registrados)
    if len(indices) == 0:
        return [], 0
    totales_por_mes = [sum(matriz_productos[p][i] for p in range(len(matriz_productos))) for i in indices]
    maximo = max(totales_por_mes)
    meses_maximos = [meses[indices[j]] for j in range(len(indices)) if totales_por_mes[j] == maximo]
    return meses_maximos, maximo


def mes_mayor_facturacion(matriz_vendedores, meses_registrados, meses):
    """
    Determina el/los mes(es) con mayor facturación total,
    considerando solo los meses ya registrados.

    Devuelve: (lista_de_meses, importe_maximo)
    """
    indices = meses_procesados(meses_registrados)
    if len(indices) == 0:
        return [], 0
    totales_por_mes = [sum(matriz_vendedores[v][i] for v in range(len(matriz_vendedores))) for i in indices]
    maximo = max(totales_por_mes)
    meses_maximos = [meses[indices[j]] for j in range(len(indices)) if totales_por_mes[j] == maximo]
    return meses_maximos, maximo


def cumplimiento_objetivo_mes(vendedores_nombre, matriz_vendedores, mes, objetivo):
    """
    Evalúa qué vendedores alcanzaron el objetivo mensual en un mes dado.
    Implementado con comprensión de listas, tal como pide la consigna.

    Devuelve: (alcanzaron, no_alcanzaron)
    """
    alcanzaron = [
        vendedores_nombre[i]
        for i in range(len(vendedores_nombre))
        if matriz_vendedores[i][mes - 1] >= objetivo
    ]
    no_alcanzaron = [
        vendedores_nombre[i]
        for i in range(len(vendedores_nombre))
        if matriz_vendedores[i][mes - 1] < objetivo
    ]
    return alcanzaron, no_alcanzaron


def ranking_vendedores(vendedores_nombre, matriz_vendedores):
    """
    Genera el ranking de vendedores ordenado de mayor a menor según su
    importe total vendido, usando una función lambda como criterio de orden.

    Devuelve una lista de tuplas (nombre, importe_total).
    """
    totales = [(vendedores_nombre[i], sum(matriz_vendedores[i])) for i in range(len(vendedores_nombre))]
    totales.sort(key=lambda vendedor: vendedor[1], reverse=True)
    return totales


def top_vendedores(ranking, cantidad=3):
    """Devuelve el Top N del ranking utilizando slicing."""
    return ranking[:cantidad]
