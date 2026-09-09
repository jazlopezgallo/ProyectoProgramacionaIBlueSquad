DEFAULT_VENDEDORES = ["Julián", "Andrés", "Valentina"]
DEFAULT_PRODUCTOS = ["Remera", "Pantalón", "Campera"]
DEFAULT_PRECIOS = [10000, 23333, 12000]


def creacionmatrices(vendedores, productos):
    """Crear matrices de ceros según tamaños de vendedores y productos."""
    matriz_vendedores = [[0 for _ in range(12)] for _ in range(len(vendedores))]
    matriz_productos = [[0 for _ in range(12)] for _ in range(len(productos))]
    return matriz_vendedores, matriz_productos


def agregar_vendedor(vendedores, matriz_vendedores, nuevo):
    """Devuelve (vendedores_nuevo, matriz_vendedores_nueva, mensaje).
    No modifica las estructuras originales (devuelve copias)."""
    nuevo = nuevo.capitalize()
    if nuevo in vendedores:
        return vendedores[:], [fila[:] for fila in matriz_vendedores], f"Vendedor '{nuevo}' ya existe."
    v_copy = vendedores[:] + [nuevo]
    m_copy = [fila[:] for fila in matriz_vendedores] + [[0] * 12]
    return v_copy, m_copy, f"Vendedor '{nuevo}' agregado con éxito."


def eliminar_vendedor(vendedores, matriz_vendedores, nombre):
    nombre = nombre.capitalize()
    if nombre not in vendedores:
        return vendedores[:], [fila[:] for fila in matriz_vendedores], f"Error: El vendedor '{nombre}' no existe."
    idx = vendedores.index(nombre)
    v_copy = vendedores[:idx] + vendedores[idx + 1 :]
    m_copy = [fila[:] for i, fila in enumerate(matriz_vendedores) if i != idx]
    return v_copy, m_copy, f"Vendedor '{nombre}' eliminado del sistema."


def agregar_producto(productos, matriz_productos, nuevo):
    nuevo = nuevo.capitalize()
    if nuevo in productos:
        return productos[:], [fila[:] for fila in matriz_productos], f"Producto '{nuevo}' ya existe."
    p_copy = productos[:] + [nuevo]
    m_copy = [fila[:] for fila in matriz_productos] + [[0] * 12]
    return p_copy, m_copy, f"Producto '{nuevo}' agregado con éxito."


def eliminar_producto(productos, matriz_productos, nombre):
    nombre = nombre.capitalize()
    if nombre not in productos:
        return productos[:], [fila[:] for fila in matriz_productos], f"Error: El producto '{nombre}' no existe."
    idx = productos.index(nombre)
    p_copy = productos[:idx] + productos[idx + 1 :]
    m_copy = [fila[:] for i, fila in enumerate(matriz_productos) if i != idx]
    return p_copy, m_copy, f"Producto '{nombre}' eliminado del sistema."


def imprimir_matriz_productos(productos, matriz_productos):
    lines = ["--- MATRIZ DE PRODUCTOS ---"]
    for i in range(len(productos)):
        lines.append(f"{productos[i]}: {matriz_productos[i]}")
    return "\n".join(lines)


def imprimir_matriz_vendedores(vendedores, matriz_vendedores):
    lines = ["--- MATRIZ DE VENDEDORES ---"]
    for i in range(len(vendedores)):
        lines.append(f"{vendedores[i]}: {matriz_vendedores[i]}")
    return "\n".join(lines)


def total_anual_empresa(matriz_vendedores):
    total_anual = sum(sum(fila) for fila in matriz_vendedores)
    return total_anual


def promedio_ventas_mensuales_empresa(matriz_vendedores, vendedores):
    total_anual = sum(sum(fila) for fila in matriz_vendedores)
    meses_totales = len(vendedores) * 12
    if meses_totales == 0:
        return None
    return total_anual / meses_totales


def modificar_ingreso_mes(matriz_vendedores, indice, mes, nuevo_valor):
    """Devuelve copia actualizada de matriz_vendedores."""
    if not (0 <= indice < len(matriz_vendedores)):
        raise IndexError("Índice de vendedor fuera de rango")
    if not (1 <= mes <= 12):
        raise ValueError("Mes debe estar entre 1 y 12")
    m_copy = [fila[:] for fila in matriz_vendedores]
    m_copy[indice][mes - 1] = nuevo_valor
    return m_copy


def revisar_promedio_vendedor(matriz_vendedores, indice):
    if not (0 <= indice < len(matriz_vendedores)):
        raise IndexError("Índice de vendedor fuera de rango")
    return sum(matriz_vendedores[indice]) / 12


def revisar_total_vendedor(matriz_vendedores, indice):
    if not (0 <= indice < len(matriz_vendedores)):
        raise IndexError("Índice de vendedor fuera de rango")
    return sum(matriz_vendedores[indice])


def anadir_proyeccion(matriz_vendedores, indice, meses_proy):
    promedio = revisar_promedio_vendedor(matriz_vendedores, indice)
    return promedio * meses_proy


def producto_mas_vendido(productos, matriz_productos):
    if len(productos) == 0:
        return None, 0
    ventas_por_producto = [sum(fila) for fila in matriz_productos]
    max_ventas = max(ventas_por_producto)
    indice_max = ventas_por_producto.index(max_ventas)
    return productos[indice_max], max_ventas
