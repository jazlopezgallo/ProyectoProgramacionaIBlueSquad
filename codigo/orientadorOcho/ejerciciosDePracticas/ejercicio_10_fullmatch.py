"""
EJERCICIO 10 - Validación completa
re.fullmatch() verifica si TODO el texto cumple el patrón.
"""

import re

codigo = "ABC123"
patron = r"[A-Z]{3}[0-9]{3}"

# re.fullmatch() es útil para validar datos completos.
resultado = re.fullmatch(patron, codigo)

print("Código:", codigo)
print("Patrón:", patron)

if resultado:
    print("El código es válido")
else:
    print("El código NO es válido")
