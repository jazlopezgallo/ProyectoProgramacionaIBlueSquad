"""
EJERCICIO 4 - Uso del signo +
El signo + indica que el elemento anterior debe aparecer
una o más veces.
"""

import re

texto = "car carr carrr ca"
patron = r"car+"

# re.findall() devuelve todas las coincidencias encontradas.
resultado = re.findall(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)
print("Coincidencias:", resultado)
