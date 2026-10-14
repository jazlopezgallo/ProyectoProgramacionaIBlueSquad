"""
EJERCICIO 3 - Uso del signo *
El signo * indica que el elemento anterior puede aparecer
cero o más veces.
"""

import re

texto = "cama campa camppa campppa"
patron = r"camp*a"

# re.findall() busca todas las palabras que cumplen el patrón.
resultado = re.findall(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)
print("Coincidencias:", resultado)
