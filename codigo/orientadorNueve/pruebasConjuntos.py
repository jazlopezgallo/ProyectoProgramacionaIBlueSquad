paise = {"Argentina", "Brasil", "Chile", "Colombia", "México"}

print("Países en el conjunto:", paise)

repetidos = ["Argentina", "Brasil", "Chile", "Colombia"]

print("Países repetidos:", repetidos)

#Ejemplo de uso de conjuntos
#Funciones : len(). max(), min(), sum().
#Operadores: in, not in, matematicos.
#Metodos: add(), remove(), discard(), clear(), issubset(), set(), list(), tuple()
a = set((1,2,3))
b = tuple((4,5,6))
lista = list((7,8,9))
fechas = set(("2023-01-01", "2023-02-01", "2023-03-01"))
             
# En  conjunto solamente no puedo tener duplicado, y no importa cuando subas los valores de conjunto, siempre va a tener un solo valor.

#interseccion 
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a & b
print("Intersección de a y b:", c)

#union
d = a | b
print("Unión de a y b:", d)

#diferencia
e = a - b
print("Diferencia de a y b:", e)

diferencia_simetrica = a ^ b
print("Diferencia simétrica de a y b:", diferencia_simetrica) #"sincurflejo"

#Diccionarios son estructuras de datos para relacionar clave-valor, tambien se los conoce como mapas o tablas hash. 
#Son mutables, no permiten claves duplicadas y no mantienen un orden específico de los elementos.

#conjunto = set()  # Crear un conjunto vacío
#diccionario = {}  # Crear un diccionario vacío

#ejeplo de diccionario
edad_estudiantes = {
    "Ana": 20,
    "Luis": 22,
    "María": 19
}
print(edad_estudiantes())


# 