"""
EJERCICIO 5 - Comienzo ^ y final $
^ indica comienzo del texto.
$ indica final del texto.
"""

import re

texto1 = "el gato se llama Tomy"
patron1 = r"^el"

# re.search() busca la primera coincidencia.
# En este caso debe estar al comienzo del texto.
resultado1 = re.search(patron1, texto1)

print("Texto:", texto1)
if resultado1:
    print("Coincidencia:", resultado1.group())
else:
    print("No hubo coincidencia")


texto2 = "El abanico"
patron2 = r"co$"

# re.search() busca la primera coincidencia.
# En este caso debe estar al final del texto.
resultado2 = re.search(patron2, texto2)

print("\nTexto:", texto2)
if resultado2:
    print("Coincidencia:", resultado2.group())
else:
    print("No hubo coincidencia")
