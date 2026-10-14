# EJERCICIO 15 - Integrador de diccionarios y conjuntos
#
# Se dispone del siguiente diccionario.
# Cada clave es el nombre de un alumno y el valor es un conjunto
# con las materias que aprobó.

aprobadas = {
    "Ana": {"Programacion", "Matematica", "Ingles"},
    "Luis": {"Programacion", "Ingles"},
    "Marta": {"Programacion", "Matematica", "Fisica"},
    "Pedro": {"Matematica", "Fisica"},
    "Sofia": {"Programacion", "Matematica", "Ingles", "Fisica"}
}

# Resolver:
#
# 1. Mostrar todas las materias diferentes que aparecen.
# 2. Mostrar qué alumnos aprobaron "Programacion".
# 3. Mostrar qué materias aprobaron tanto Ana como Sofia.
# 4. Mostrar qué materias aprobó Ana pero no Luis.
# 5. Crear un diccionario nuevo donde la clave sea una materia y
#    el valor sea la cantidad de alumnos que la aprobaron.
# 6. Comprobar si las materias de Ana están incluidas en las de Sofia.
#
# Ejemplo parcial del punto 5:
# {
#     "Programacion": 4,
#     "Matematica": 4,
#     ...
# }
#

# Escribí tu solución debajo de esta línea:
todas_las_materias = set()
for materias in aprobadas.values():
    todas_las_materias |= materias
print("1. Materias diferentes:", sorted(todas_las_materias))

alumnos_programacion = [
    alumno
    for alumno, materias in aprobadas.items()
    if "Programacion" in materias
]
print("2. Aprobaron Programacion:", alumnos_programacion)

materias_ana_y_sofia = aprobadas["Ana"] & aprobadas["Sofia"]
print("3. Ana y Sofia aprobaron:", sorted(materias_ana_y_sofia))

materias_ana_no_luis = aprobadas["Ana"] - aprobadas["Luis"]
print("4. Ana aprobó y Luis no:", sorted(materias_ana_no_luis))

cantidad_por_materia = {}
for materias in aprobadas.values():
    for materia in materias:
        cantidad_por_materia[materia] = cantidad_por_materia.get(materia, 0) + 1

cantidad_por_materia = dict(sorted(cantidad_por_materia.items()))
print("5. Cantidad de alumnos por materia:", cantidad_por_materia)

ana_esta_incluida_en_sofia = aprobadas["Ana"].issubset(aprobadas["Sofia"])
print("6. Las materias de Ana están incluidas en las de Sofia:", ana_esta_incluida_en_sofia)

cantidades = cantidad_por_materia.values()
print("Cantidad de materias distintas:", len(todas_las_materias))
print("Mayor cantidad de aprobaciones:", max(cantidades))
print("Menor cantidad de aprobaciones:", min(cantidades))
print("Total de aprobaciones registradas:", sum(cantidades))
