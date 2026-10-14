import re

patron = r"[A-Za-z][0-9]{3}"
codigo = "A123XYZ"

inicio = re.match(patron, codigo)
completo = re.fullmatch(patron, codigo)

# c) buscar la primera secuencia numérica dentro de una frase
frase = "El pedido número 4521 llega el jueves"
resultado_busqueda = re.search(r"[0-9]+", frase)

# d) mostrar group, start, end y span solo si hay coincidencia
if resultado_busqueda is not None:
    print("Coincidencia:", resultado_busqueda.group())
    print("Inicio:", resultado_busqueda.start())
    print("Fin:", resultado_busqueda.end())
    print("Span:", resultado_busqueda.span())
else:
    print("No se encontró ninguna coincidencia")

# e) repetir la búsqueda ignorando mayúsculas/minúsculas
texto = "El Producto tiene stock, el PRODUCTO se agotó"
resultado_ignorecase = re.search(r"producto", texto, re.IGNORECASE)

if resultado_ignorecase is not None:
    print("Encontrado:", resultado_ignorecase.group(), "en la posición", resultado_ignorecase.start())
else:
    print("No se encontró")