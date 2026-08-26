def contiene_digitos(texto):
    """Retorna True si el texto tiene al menos un dígito."""
    val = False
    for caracter in texto:
        if caracter.isdigit():
            val = True
    return val


def generar_sigla(nombre_equipo):
    """Retorna la sigla formada por la inicial de cada palabra."""
    palabras = nombre_equipo.split()
    sigla = ""
    for palabra in palabras:
        sigla = sigla + palabra[0]
    sigla = sigla.upper()
    return sigla


def normalizar_nombre(nombre):
    """Retorna el nombre con cada palabra capitalizada."""
    return nombre.title()


# Programa principal
nombre_equipo = input("Nombre del equipo: ")
comision = input("Comisión: ")
cantidad_integrantes = int(input("Cantidad de integrantes: "))

integrantes = []
roles = []

for i in range(cantidad_integrantes):
    nombre = input(f"Nombre del integrante {i + 1}: ")
    rol = input(f"Rol inicial del integrante {i + 1}: ")
    integrantes.append(normalizar_nombre(nombre))
    roles.append(rol)

nombre_equipo_mayus = nombre_equipo.upper()
sigla = generar_sigla(nombre_equipo)
tiene_digitos = contiene_digitos(nombre_equipo)

print(f"\nEquipo: {nombre_equipo_mayus}")
print(f"Comisión: {comision}")
print(f"Cantidad de caracteres del nombre: {len(nombre_equipo)}")
print(f"Sigla: {sigla}")
print(f"¿El nombre del equipo contiene dígitos?: {tiene_digitos}")

print("\nIntegrantes:")
for i in range(cantidad_integrantes):
    print(f"- {integrantes[i]} ({roles[i]})")