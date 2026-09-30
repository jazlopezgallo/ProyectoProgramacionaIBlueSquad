# a) dos letras mayúsculas y cuatro números
patron_codigo = r"^[A-Z]{2}[0-9]{4}$"

# b) legajo de exactamente cinco dígitos
patron_legajo = r"^[0-9]{5}$"

# c) importe: símbolo $ y uno o más dígitos
patron_importe = r"^\$[0-9]+$"

# d) palabra que empieza con mayúscula y sigue solo con letras
patron_palabra = r"^[A-Z][a-z]*$"

# e) fecha con formato DD/MM/AAAA (solo la forma, no la validez real de la fecha)
patron_fecha = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"