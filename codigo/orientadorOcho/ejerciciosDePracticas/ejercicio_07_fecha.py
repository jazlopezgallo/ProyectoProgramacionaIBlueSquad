"""
EJERCICIO 7 - Buscar una fecha
{2} indica que el elemento anterior debe aparecer
exactamente dos veces.
"""

import re

texto = "Su fecha de nacimiento fue el 07/08/17"
patron = r"[0-9]{2}/[0-9]{2}/[0-9]{2}"

# re.search() busca la primera fecha que coincida con el patrón.
resultado = re.search(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)

if resultado:
    print("Coincidencia:", resultado.group())
else:
    print("No hubo coincidencia")
