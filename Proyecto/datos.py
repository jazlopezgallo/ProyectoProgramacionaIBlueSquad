"""
datos.py
--------
Contiene únicamente las constantes y los datos iniciales del sistema
BlueSquad SalesMatrix. No contiene lógica de negocio ni funciones que
interactúen con el usuario (sin input, sin print).
"""

# Tupla de meses: es un dato fijo que no debe modificarse durante la ejecución.
MESES = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

# Objetivo mensual de ventas exigido a cada vendedor.
OBJETIVO_MENSUAL = 500000

# --- Datos iniciales de vendedores (listas paralelas) ---
# Posición 0 -> Julián | Posición 1 -> Andrés | Posición 2 -> Valentina
VENDEDORES_ID_INICIAL = [201, 202, 203]
VENDEDORES_NOMBRE_INICIAL = ["Julián", "Andrés", "Valentina"]
VENDEDORES_COMISION_INICIAL = [0.05, 0.05, 0.05]  # 5% ya convertido a decimal

# --- Datos iniciales de productos (listas paralelas) ---
# Posición 0 -> Remera | Posición 1 -> Pantalón | Posición 2 -> Campera
PRODUCTOS_ID_INICIAL = [101, 102, 103]
PRODUCTOS_NOMBRE_INICIAL = ["Remera", "Pantalón", "Campera"]
PRODUCTOS_PRECIO_INICIAL = [10000, 23333, 12000]
