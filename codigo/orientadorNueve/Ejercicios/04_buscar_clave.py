# EJERCICIO 4 - Buscar una clave
#
# Dado el siguiente diccionario:
capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
# Pedir al usuario que ingrese un país.
# Si el país existe en el diccionario, mostrar su capital.
# Si no existe, mostrar "País no encontrado".

# Escribí tu solución debajo de esta línea:


def buscar_capital(pais):
    pais_buscado = pais.strip().casefold()
    resultado = capitales.get(pais_buscado)
    if resultado is None:
        print("País no encontrado.")
        return

    nombre_pais, capital = resultado
    print(f"La capital de {nombre_pais} es {capital}.")


pais = input("Ingrese un país: ").strip()
buscar_capital(pais)