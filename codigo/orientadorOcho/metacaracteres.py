import re

# a) ^ y $ : inicio y final de la cadena
print(re.search(r"^Hola", "Hola mundo"))      # coincide, empieza con "Hola"
print(re.search(r"mundo$", "Hola mundo"))     # coincide, termina con "mundo"

# b) . : cualquier carácter excepto salto de línea
print(re.findall(r"a.a", "aroma arena alaba"))  # ['aro', ... ] -> en realidad matches tipo "a.a"

# c) [ ] : clase de caracteres, con rangos
print(re.findall(r"[0-9]", "Tengo 3 gatos y 2 perros"))   # ['3', '2']
print(re.findall(r"[A-Z]", "Hola Mundo"))                 # ['H', 'M']

# d) [^ ] : negación dentro de una clase
print(re.findall(r"[^0-9]", "a1b2c3"))   # ['a', 'b', 'c']

# e) | : alternativas
print(re.search(r"septiembre|setiembre", "21 de setiembre"))  # coincide

# f) ( ) : agrupación
print(re.findall(r"(ab)+", "ababab cd"))   # ['ab'] (agrupa "ab" para repetirlo)

# g) ? * + : repeticiones
print(re.findall(r"lobos?", "lobo lobos"))     # ['lobo', 'lobos'] -> la s es opcional
print(re.findall(r"ab*c", "ac abc abbbc"))     # ['ac', 'abc', 'abbbc']
print(re.findall(r"ab+c", "ac abc abbbc"))     # ['abc', 'abbbc'] (ac no entra, falta al menos una b)

# h) {m} {m,n} {m,} : cantidad exacta o rango
print(re.findall(r"[0-9]{4}", "año 2026"))         # ['2026']
print(re.findall(r"[0-9]{2,4}", "12 y 3456"))      # ['12', '3456']
print(re.findall(r"1{2,}", "111 1 11"))            # ['111', '11']

# i) \ : escape de un metacaracter
print(re.findall(r"\$[0-9]+", "El total es $100 y el IVA $21"))  # ['$100', '$21']