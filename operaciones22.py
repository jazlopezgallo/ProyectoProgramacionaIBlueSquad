def validarnumeros(numero):
    """Valida que el string sea un entero no negativo, sin generar errores."""
    numero = numero.strip()
    return numero.isdigit() and int(numero) >= 0


def validartexto(texto):
    """Valida que el texto no esté vacío tras normalizarlo."""
    return texto.strip().capitalize() != ""

# Wrapper for main.py compatibility
def es_entero(texto):
    """Wrapper that uses validarnumeros to check if text represents a non‑negative integer."""
    return validarnumeros(texto)

def texto_valido(texto):
    """Wrapper that uses validartexto to check if text is non‑empty after stripping."""
    return validartexto(texto)

def buscar_vendedor(vendedores_id, codigo):
    """Search for a vendor code using the generic busqueda function."""
    return busqueda(vendedores_id, codigo)

def buscar_producto(productos_id, codigo):
    """Search for a product code using the generic busqueda function."""
    return busqueda(productos_id, codigo)



# ---------------------------------------------------------------------------
# BÚSQUEDAS
# ---------------------------------------------------------------------------

def busqueda(lista, buscado):
    """Busca un elemento por código. Devuelve su posición o -1 si no existe."""
    return lista.index(buscado) if buscado in lista else -1


# ---------------------------------------------------------------------------
# ALTA Y BAJA DE VENDEDORES
# ---------------------------------------------------------------------------

def agregar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                      matriz_vendedores, codigo, nombre, comision):
    nombre = nombre.strip().capitalize()

    if not validartexto(nombre):
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el nombre no puede estar vacío."
    if codigo <= 0:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el código debe ser mayor que cero."
    if codigo in vendedores_id:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el código ya se encuentra registrado."
    if nombre in vendedores_nombre:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el nombre ya se encuentra registrado."
    if not validarnumeros(comision):
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: la comisión debe ser un número válido."
    if comision > 100:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: la comisión no puede ser mayor a 100%."

    id_nuevo = vendedores_id[:] + [codigo]
    nombre_nuevo = vendedores_nombre[:] + [nombre]
    comision_nueva = vendedores_comision[:] + [comision / 100]
    matriz_nueva = [fila[:] for fila in matriz_vendedores] + [[0] * 12]

    mensaje = f"Vendedor '{nombre}' agregado con éxito (código {codigo})."
    return id_nuevo, nombre_nuevo, comision_nueva, matriz_nueva, True, mensaje


def eliminar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                       matriz_vendedores, codigo):
    posicion = busqueda(vendedores_id, codigo)
    if posicion == -1:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el vendedor no existe."

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
    nombre = nombre.strip().capitalize()

    if not validartexto(nombre):
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el nombre no puede estar vacío."
    if codigo <= 0:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el código debe ser mayor que cero."
    if codigo in productos_id:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el código ya se encuentra registrado."
    if nombre in productos_nombre:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el producto ya se encuentra registrado."
    if precio <= 0:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el precio debe ser mayor que cero."

    id_nuevo = productos_id[:] + [codigo]
    nombre_nuevo = productos_nombre[:] + [nombre]
    precio_nuevo = productos_precio[:] + [precio]
    matriz_nueva = [fila[:] for fila in matriz_productos] + [[0] * 12]

    mensaje = f"Producto '{nombre}' agregado con éxito (código {codigo})."
    return id_nuevo, nombre_nuevo, precio_nuevo, matriz_nueva, True, mensaje


def eliminar_producto(productos_id, productos_nombre, productos_precio,
                       matriz_productos, codigo):
    posicion = busqueda(productos_id, codigo)
    if posicion == -1:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el producto no existe."

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
    posicion_vendedor = busqueda(vendedores_id, codigo_vendedor)
    if posicion_vendedor == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el vendedor no existe."

    posicion_producto = busqueda(productos_id, codigo_producto)
    if posicion_producto == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el producto no existe."

    if mes < 1 or mes > 12:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el mes debe estar entre 1 y 12."

    if cantidad <= 0:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: la cantidad debe ser mayor que cero."

    importe = cantidad * productos_precio[posicion_producto]

    matriz_vendedores_nueva = [fila[:] for fila in matriz_vendedores]
    matriz_productos_nueva = [fila[:] for fila in matriz_productos]
    matriz_vendedores_nueva[posicion_vendedor][mes - 1] += importe
    matriz_productos_nueva[posicion_producto][mes - 1] += cantidad

    meses_registrados_nuevo = meses_registrados[:]
    meses_registrados_nuevo[mes - 1] = True

    mensaje = f"Venta registrada: {cantidad} unidades, importe ${importe}."
    return matriz_vendedores_nueva, matriz_productos_nueva, meses_registrados_nuevo, True, mensaje