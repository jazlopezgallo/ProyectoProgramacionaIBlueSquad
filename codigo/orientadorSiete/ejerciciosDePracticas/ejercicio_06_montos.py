"""
EJERCICIO 6 - Buscar montos
\$ permite buscar el símbolo $ literalmente.
[0-9]+ representa uno o más dígitos.
"""

import re

texto = "El monto total es de $100 y el IVA es de $21"
patron = r"\$[0-9]+"

# re.findall() obtiene todos los montos encontrados.
resultado = re.findall(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)
print("Coincidencias:", resultado)
