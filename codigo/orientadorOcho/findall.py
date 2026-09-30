import re

texto = ("Contactos: Ana (ana@mail.com), tel 1234-5678, código AB1234. "
          "Bruno (bruno@mail.com), tel 8765-4321, código CD5678.")

# a) todas las secuencias numéricas con findall
numeros = re.findall(r"[0-9]+", texto)
print(numeros)

# b) recorrer coincidencias con finditer, informando contenido y posiciones
print("\nCoincidencias con finditer:")
for coincidencia in re.finditer(r"[0-9]+", texto):
    print(f"Valor: {coincidencia.group()} - Inicio: {coincidencia.start()} - Fin: {coincidencia.end()}")

# c) comparación de tipos de resultado
print(type(numeros))                           # <class 'list'>
print(type(re.finditer(r"[0-9]+", texto)))      # <class 'callable_iterator'>

# d) patrón con grupos de captura: findall devuelve tuplas
telefonos = re.findall(r"([0-9]{4})-([0-9]{4})", texto)
print(telefonos)