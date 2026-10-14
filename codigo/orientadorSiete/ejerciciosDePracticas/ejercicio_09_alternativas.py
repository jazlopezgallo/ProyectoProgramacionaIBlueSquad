"""
EJERCICIO 9 - Alternativas
El símbolo | significa "o".
"""

import re

texto = "21 de septiembre - 21 de setiembre"
patron = r"(?:septiembre|setiembre)"

# re.findall() devuelve todas las alternativas encontradas.
# (?: ) agrupa sin crear un grupo capturado.
resultado = re.findall(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)
print("Coincidencias:", resultado)
