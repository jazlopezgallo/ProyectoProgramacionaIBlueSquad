def busqueda(ids, codigo):
    for indice, valor in enumerate(ids):
        if valor == codigo:
            return indice
    return -1

def validarnumeros(numero):
    if numero is None:
        return False
    texto = str(numero).strip()
    return texto.isdigit()

def validartexto(texto):
    if texto is None:
        return False
    return texto.strip() != ""

# Wrapper for main.py compatibility
def es_entero(texto):
    return validarnumeros(texto)

def texto_valido(texto):
    return validartexto(texto)

def buscar_vendedor(vendedores_id, codigo):
    return busqueda(vendedores_id, codigo)

def buscar_producto(productos_id, codigo):
    return busqueda(productos_id, codigo)

def agregar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                     matriz_vendedores, codigo, nombre, comision):
    nombre = nombre.strip().title()
    if not validartexto(nombre):
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el nombre no puede estar vacío."
    if codigo <= 0 or codigo in vendedores_id:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el código debe ser mayor que cero y no estar registrado."
    if nombre in vendedores_nombre:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el nombre ya se encuentra registrado."
    if comision <= 0 or comision > 100:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: la comisión debe ser mayor a 0% y menor o igual a 100%."

    columnas = len(matriz_vendedores[0]) if matriz_vendedores else 12
    return (vendedores_id + [codigo], vendedores_nombre + [nombre],
            vendedores_comision + [comision / 100],
            matriz_vendedores + [[0] * columnas], True,
            f"Vendedor '{nombre}' agregado con éxito.")

def eliminar_vendedor(vendedores_id, vendedores_nombre, vendedores_comision,
                      matriz_vendedores, codigo):
    posicion = busqueda(vendedores_id, codigo)
    if posicion == -1:
        return vendedores_id, vendedores_nombre, vendedores_comision, matriz_vendedores, False, "Error: el vendedor no existe."

    nombre = vendedores_nombre[posicion]
    return (vendedores_id[:posicion] + vendedores_id[posicion + 1:],
            vendedores_nombre[:posicion] + vendedores_nombre[posicion + 1:],
            vendedores_comision[:posicion] + vendedores_comision[posicion + 1:],
            [fila[:] for i, fila in enumerate(matriz_vendedores) if i != posicion],
            True, f"Vendedor '{nombre}' eliminado del sistema.")

def agregar_producto(productos_id, productos_nombre, productos_precio,
                     matriz_productos, codigo, nombre, precio):
    nombre = nombre.strip().title()
    if not validartexto(nombre):
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el nombre no puede estar vacío."
    if codigo <= 0 or codigo in productos_id:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el código debe ser mayor que cero y no estar registrado."
    if nombre in productos_nombre:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el producto ya se encuentra registrado."
    if precio <= 0:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el precio debe ser mayor que cero."

    columnas = len(matriz_productos[0]) if matriz_productos else 12
    return (productos_id + [codigo], productos_nombre + [nombre],
            productos_precio + [precio],
            matriz_productos + [[0] * columnas], True,
            f"Producto '{nombre}' agregado con éxito.")

def eliminar_producto(productos_id, productos_nombre, productos_precio,
                      matriz_productos, codigo):
    posicion = busqueda(productos_id, codigo)
    if posicion == -1:
        return productos_id, productos_nombre, productos_precio, matriz_productos, False, "Error: el producto no existe."

    nombre = productos_nombre[posicion]
    return (productos_id[:posicion] + productos_id[posicion + 1:],
            productos_nombre[:posicion] + productos_nombre[posicion + 1:],
            productos_precio[:posicion] + productos_precio[posicion + 1:],
            [fila[:] for i, fila in enumerate(matriz_productos) if i != posicion],
            True, f"Producto '{nombre}' eliminado del sistema.")

def registrar_venta(vendedores_id, productos_id, productos_precio,
                    matriz_vendedores, matriz_productos, meses_registrados,
                    codigo_vendedor, codigo_producto, mes, cantidad):
    vendedor = busqueda(vendedores_id, codigo_vendedor)
    producto = busqueda(productos_id, codigo_producto)

    if vendedor == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el vendedor no existe."
    if producto == -1:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el producto no existe."
    if mes < 1 or mes > len(meses_registrados):
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: el mes no es válido."
    if cantidad <= 0:
        return matriz_vendedores, matriz_productos, meses_registrados, False, "Error: la cantidad debe ser mayor que cero."

    importe = cantidad * productos_precio[producto]
    nuevos_vendedores = [fila[:] for fila in matriz_vendedores]
    nuevos_productos = [fila[:] for fila in matriz_productos]
    nuevos_vendedores[vendedor][mes - 1] += importe
    nuevos_productos[producto][mes - 1] += cantidad
    nuevos_meses = meses_registrados[:]
    nuevos_meses[mes - 1] = True

    return nuevos_vendedores, nuevos_productos, nuevos_meses, True, f"Venta registrada: {cantidad} unidades, importe ${importe:.2f}."

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