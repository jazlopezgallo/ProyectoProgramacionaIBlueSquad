import re

texto = (
    "Contacto de ventas: Ana Gómez (ana.gomez@mail.com), teléfono 1234-5678, código AB1234. "
    "Contacto de soporte: Bruno Díaz (bruno.diaz@mail.com), teléfono 8765-4321, código CD5678. "
    "El local abre a las 9:00 y cierra a las 21:00."
)

patron_correo = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
patron_telefono = r"[0-9]{4}-[0-9]{4}"
patron_codigo = r"[A-Z]{2}[0-9]{4}"

# a) todas las coincidencias de cada tipo
correos = re.findall(patron_correo, texto)
telefonos = re.findall(patron_telefono, texto)
codigos = re.findall(patron_codigo, texto)

print("Correos encontrados:", correos)
print("Teléfonos encontrados:", telefonos)
print("Códigos encontrados:", codigos)

# b) cantidad encontrada de cada tipo
print(f"\nCantidad de correos: {len(correos)}")
print(f"Cantidad de teléfonos: {len(telefonos)}")
print(f"Cantidad de códigos: {len(codigos)}")

# c) posición inicial y final con finditer
print("\nDetalle de teléfonos encontrados:")
for coincidencia in re.finditer(patron_telefono, texto):
    print(f"Teléfono: {coincidencia.group()} - Inicio: {coincidencia.start()} - Fin: {coincidencia.end()}")