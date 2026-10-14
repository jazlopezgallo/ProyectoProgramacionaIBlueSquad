"""
EJERCICIO 12 - INTEGRADOR

Una empresa recibe un dato de cliente con este formato:

MEV-458 | maria@gmail.com | 21/09/2026 | $1250

Resolver utilizando expresiones regulares.

Se pide:
1. Obtener el código del cliente.
   Formato: 3 letras mayúsculas, guion y 3 números.

2. Obtener el correo electrónico.

3. Obtener la fecha con formato dd/mm/aaaa.

4. Obtener el monto, que comienza con $.

5. Mostrar todos los datos encontrados.

6. Validar con re.fullmatch() si "MEV-458"
   cumple exactamente con el formato del código.
"""

import re

cliente = "MEV-458 | maria@gmail.com | 21/09/2026 | $1250"

print("Dato a analizar:")
print(cliente)


# ------------------------------------------------------------
# 1. CÓDIGO
# ------------------------------------------------------------

patron_codigo = r""

# re.search() puede usarse porque queremos encontrar
# el código dentro de una cadena más grande.
# resultado_codigo = re.search(patron_codigo, cliente)


# ------------------------------------------------------------
# 2. CORREO
# ------------------------------------------------------------

patron_correo = r""

# re.search() puede usarse para localizar
# el correo dentro del texto.
# resultado_correo = re.search(patron_correo, cliente)


# ------------------------------------------------------------
# 3. FECHA
# ------------------------------------------------------------

patron_fecha = r""

# re.search() puede usarse para localizar
# la fecha dentro del texto.
# resultado_fecha = re.search(patron_fecha, cliente)


# ------------------------------------------------------------
# 4. MONTO
# ------------------------------------------------------------

patron_monto = r""

# re.search() puede usarse para localizar
# el monto dentro del texto.
# resultado_monto = re.search(patron_monto, cliente)


# ------------------------------------------------------------
# 5. VALIDACIÓN COMPLETA DEL CÓDIGO
# ------------------------------------------------------------

codigo = "MEV-458"
patron_validacion = r""

# re.fullmatch() verifica que TODO el código
# cumpla exactamente con el patrón.
# resultado_validacion = re.fullmatch(patron_validacion, codigo)
