import re

# a) reemplazar teléfonos con formato 123-456-7890
texto_contacto = "Llamar a Oliver al 123-456-7890 o a Gabriela al 987-654-3210."
texto_ofuscado = re.sub(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", "XXX-XXX-XXXX", texto_contacto)
print(texto_ofuscado)
# Llamar a Oliver al XXX-XXX-XXXX o a Gabriela al XXX-XXX-XXXX.

# b) dividir un texto usando puntos, comas, signos de pregunta y espacios
frase = "Hola, ¿cómo estás? Espero que bien."
partes = re.split(r"[.,?\s]+", frase)
print(partes)

# c) compilar un patrón y reutilizarlo
patron_anio = re.compile(r"[0-9]{4}")
fechas = "07/08/2017|03/02/1984|17/03/2001"

anios = patron_anio.findall(fechas)
print(anios)

primer_anio = patron_anio.match(fechas)
print(primer_anio)

texto_reemplazado = patron_anio.sub("AAAA", fechas)
print(texto_reemplazado)
