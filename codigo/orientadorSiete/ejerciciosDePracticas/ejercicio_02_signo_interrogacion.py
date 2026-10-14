"""
EJERCICIO 2 - Uso del signo ?
El signo ? indica que el elemento anterior puede aparecer
cero o una vez.
"""

import re

texto = "suscripción subscripción"
patron = r"sub?scripción"

# re.findall() devuelve todas las coincidencias encontradas.
resultado = re.findall(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)
print("Coincidencias:", resultado)
