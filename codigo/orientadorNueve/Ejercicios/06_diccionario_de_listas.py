# EJERCICIO 6 - Diccionario con listas
#
# Dado el siguiente diccionario:
cursos = {
    "Programacion": ["Ana", "Luis"],
    "Matematica": ["Pedro", "Sofia"],
    "Ingles": ["Juan"]
}

# 1. Agregar "Marta" al curso de Programacion.
# 2. Mostrar todos los alumnos de Matematica.
# 3. Mostrar cuántos alumnos tiene cada curso.

# Escribí tu solución debajo de esta línea:
cursos["Programacion"].append("Marta")
print("Alumnos de Matematica:", cursos["Matematica"])
for curso, alumnos in cursos.items():
    print(f"El curso de {curso} tiene {len(alumnos)} alumnos.")

