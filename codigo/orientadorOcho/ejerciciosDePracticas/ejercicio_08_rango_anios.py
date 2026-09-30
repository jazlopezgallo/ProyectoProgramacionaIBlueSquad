"""
EJERCICIO 8 - Rango de años
[2-5] permite cualquiera de los dígitos 2, 3, 4 o 5
en esa posición.
"""

import re

texto = "2010 2011 2012 2013 2014 2015 2016 2017"
patron = r"201[2-5]"

# re.findall() devuelve todos los años que cumplen el patrón.
resultado = re.findall(patron, texto)

print("Texto:", texto)
print("Patrón:", patron)
print("Coincidencias:", resultado)
