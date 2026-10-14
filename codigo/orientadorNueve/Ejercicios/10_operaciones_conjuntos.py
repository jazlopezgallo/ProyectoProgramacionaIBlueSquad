# EJERCICIO 10 - Unión e intersección
#
# Dados los siguientes conjuntos:
python = {"Ana", "Luis", "Marta", "Juan"}
java = {"Pedro", "Luis", "Juan", "Sofia"}

# Mostrar:
# 1. Todos los alumnos que cursan al menos uno de los dos lenguajes.
# 2. Los alumnos que cursan ambos lenguajes.

# Escribí tu solución debajo de esta línea:
alumnos_uno_o_ambos = python | java
alumnos_ambos = python & java
alumnos_un_solo_lenguaje = python ^ java

print("Cursan al menos uno de los lenguajes:", alumnos_uno_o_ambos)
print("Cursan ambos lenguajes:", alumnos_ambos)
print("Cursan un solo lenguaje:", alumnos_un_solo_lenguaje)
