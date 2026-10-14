"""
EJERCICIO 13 - DESAFÍO INTEGRADOR

Trabajar con varios clientes y utilizar re.findall()
para obtener todos los datos de cada tipo.

Se pide obtener:
- todos los códigos
- todos los correos
- todas las fechas
- todos los montos
"""

import re

clientes = (
    "MEV-458 | maria@gmail.com | 21/09/2026 | $1250\n"
    "ABC-123 | juan_25@hotmail.com | 03/10/2026 | $850\n"
    "XYZ-999 | ana.perez@empresa.com | 15/11/2026 | $2300"
)

print("Datos a analizar:")
print(clientes)

# ------------------------------------------------------------
# 1. TODOS LOS CÓDIGOS
# ------------------------------------------------------------

patron_codigos = r""

# re.findall() es útil porque necesitamos encontrar
# todas las coincidencias dentro del texto.
# codigos = re.findall(patron_codigos, clientes)


# ------------------------------------------------------------
# 2. TODOS LOS CORREOS
# ------------------------------------------------------------

patron_correos = r""

# correos = re.findall(patron_correos, clientes)


# ------------------------------------------------------------
# 3. TODAS LAS FECHAS
# ------------------------------------------------------------

patron_fechas = r""

# fechas = re.findall(patron_fechas, clientes)


# ------------------------------------------------------------
# 4. TODOS LOS MONTOS
# ------------------------------------------------------------

patron_montos = r""

# montos = re.findall(patron_montos, clientes)


# Al finalizar, mostrar las cuatro listas obtenidas.
