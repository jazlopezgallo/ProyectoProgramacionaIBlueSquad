import validaciones

# validar_legajo
print(validaciones.validar_legajo("12345"))   # True
print(validaciones.validar_legajo("1052"))    # False (cuatro dígitos)
print(validaciones.validar_legajo("123456"))  # False (seis dígitos)
print(validaciones.validar_legajo("abcde"))   # False
print(validaciones.validar_legajo(""))        # False

# validar_codigo
print(validaciones.validar_codigo("AB1234"))  # True
print(validaciones.validar_codigo("ab1234"))  # False (minúsculas)
print(validaciones.validar_codigo("A1234"))   # False (una sola letra)
print(validaciones.validar_codigo("ABC123"))  # False (tres letras)
print(validaciones.validar_codigo(""))        # False

# validar_telefono
print(validaciones.validar_telefono("1234-5678"))  # True
print(validaciones.validar_telefono("12345678"))   # False (sin guion)
print(validaciones.validar_telefono("123-5678"))   # False (le falta un dígito)
print(validaciones.validar_telefono("abcd-efgh"))  # False
print(validaciones.validar_telefono(""))           # False

# validar_correo
print(validaciones.validar_correo("ana@mail.com"))     # True
print(validaciones.validar_correo("ana@mail"))         # False (sin extensión)
print(validaciones.validar_correo("anamail.com"))      # False (sin @)
print(validaciones.validar_correo("ana@.com"))         # False (dominio vacío)
print(validaciones.validar_correo(""))                 # False

# validar_importe
print(validaciones.validar_importe("$100"))   # True
print(validaciones.validar_importe("100"))    # False (sin $)
print(validaciones.validar_importe("$"))      # False (sin dígitos)
print(validaciones.validar_importe("$1a0"))   # False
print(validaciones.validar_importe(""))       # False

# validar_patente
print(validaciones.validar_patente("ABC123"))  # True (formato viejo)
print(validaciones.validar_patente("AB123CD")) # True (formato nuevo)
print(validaciones.validar_patente("abc123"))  # False (minúsculas)
print(validaciones.validar_patente("AB1234"))  # False (no cumple ninguno de los dos formatos)
print(validaciones.validar_patente(""))        # False