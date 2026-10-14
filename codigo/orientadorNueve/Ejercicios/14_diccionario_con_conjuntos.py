# EJERCICIO 14 - Diccionario con conjuntos
#
# Dado el siguiente diccionario:
estudiantes = {
    "Ana": {"Python", "SQL", "HTML"},
    "Luis": {"Python", "Java"},
    "Marta": {"SQL", "HTML"},
    "Pedro": {"Python", "SQL"}
}

# Mostrar:
# 1. Los lenguajes o tecnologías que conoce Ana.
# 2. Los conocimientos que tienen en común Ana y Pedro.
# 3. Todos los conocimientos distintos presentes entre todos los estudiantes.

# Escribí tu solución debajo de esta línea:
print("Conocimientos de Ana:", estudiantes["Ana"])

conocimientos_comunes = estudiantes["Ana"] & estudiantes["Pedro"]
print("Conocimientos en común entre Ana y Pedro:", conocimientos_comunes)

conocimientos_totales = set()
for conocimientos in estudiantes.values():
    conocimientos_totales |= conocimientos
print("Conocimientos de todos los estudiantes:", conocimientos_totales)
