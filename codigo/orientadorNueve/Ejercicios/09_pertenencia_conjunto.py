# EJERCICIO 9 - Verificar pertenencia
#
# Dado el siguiente conjunto:
usuarios_registrados = {"ana", "pedro", "maria", "juan"}

# Pedir al usuario un nombre de usuario.
# Informar si el usuario está registrado o no.

# Escribí tu solución debajo de esta línea:
usuario = input("Ingrese un nombre de usuario: ").strip().lower()

if usuario in usuarios_registrados:
	print(f"El usuario {usuario} está registrado.")
elif usuario not in usuarios_registrados:
	print(f"El usuario {usuario} no está registrado.")
