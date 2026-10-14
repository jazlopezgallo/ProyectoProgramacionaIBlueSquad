# EJERCICIO 8 - Agregar y eliminar elementos de un conjunto
#
# Dado el siguiente conjunto:
materias = {"Programacion", "Matematica", "Fisica"}

# 1. Agregar "Ingles".
# 2. Eliminar "Fisica".
# 3. Mostrar el conjunto resultante.

# Escribí tu solución debajo de esta línea:
materias.add("Ingles")
materias.remove("Fisica")
print("Materias luego de agregar y eliminar:", materias)

# discard() no produce error si el elemento no está en el conjunto.
materias.discard("Quimica")

# clear() vacía el conjunto; se usa una copia para conservar materias.
materias_temporal = materias.copy()
materias_temporal.clear()
print("Conjunto temporal luego de clear():", materias_temporal)
