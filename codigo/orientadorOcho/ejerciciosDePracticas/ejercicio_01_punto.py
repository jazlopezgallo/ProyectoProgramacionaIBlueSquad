"""
EJERCICIO 1 - Uso del punto .
El punto representa cualquier carácter individual.
"""

import re

texto = "sal sol sed sin sur"
patron = r"s.l"

# re.findall() busca todas las coincidencias del patrón
# y las devuelve en una lista.
resultado = re.findall(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)
print("Coincidencias:", resultado)
