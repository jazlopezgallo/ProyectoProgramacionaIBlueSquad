texto = "Programacion en Python"

# a) Primer y último carácter
print(texto[0])    # P
print(texto[-1])   # n

# b) mediante slicing
print(texto[0:12])


# c) Cadena invertida
print(texto[::-1])


# d) Verificar si "Python" pertenece a la cadena
print("Python" in texto)


# e) Intentar modificar texto[0]
texto[0] = "p"
#e) Al intentar texto[0] = "p", Python lanza un TypeError porque las cadenas son inmutables: 
# no se puede modificar un carácter en su posición original. Para lograr algo parecido, 
# hay que armar una cadena nueva, por ejemplo con slicing y concatenación: texto = "p" + texto[1:].