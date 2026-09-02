#3. Creación de tuplas
dias_habiles = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
tupla_vacia = ()
un_elemento = ("Python",)
registro = (1052, "Ana Pérez", 8.5)

print(type(dias_habiles))   
print(type(tupla_vacia))    
print(type(un_elemento))    
print(type(registro))       

print(type(("Python")))     
print(type(("Python",)))    

#4. Acceso, recorrido y rebanadas para una tupla
productos = ("Teclado", "Mouse", "Monitor", "Auriculares", "Webcam")

# a) primer, último y elemento central
primer_producto = productos[0]
ultimo_producto = productos[-1]
indice_centro = len(productos) // 2
elemento_central = productos[indice_centro]
print(primer_producto, ultimo_producto, elemento_central)
# Teclado Webcam Monitor

# b) los tres primeros elementos
primeros_tres = productos[:3]
print(primeros_tres)
# ('Teclado', 'Mouse', 'Monitor')

# c) desde "Monitor" hasta el final
desde_monitor = productos[2:]
print(desde_monitor)
# ('Monitor', 'Auriculares', 'Webcam')

# d) nueva tupla con el orden invertido
productos_invertidos = productos[::-1]
print(productos_invertidos)
# ('Webcam', 'Auriculares', 'Monitor', 'Mouse', 'Teclado')

# e) recorrer con for
for producto in productos:
    print(f"*{producto}")

# f) intentar modificar
# productos[0] = "Notebook"
# TypeError: 'tuple' object does not support item assignment

print(productos)  # se mantiene igual: la tupla no cambió

# 5. Operadores, funciones y métodos
ventas = (120, 85, 230, 150, 90, 150)

# a) cantidad, mayor, menor y suma total
cantidad = len(ventas)
mayor = max(ventas)
menor = min(ventas)
total = sum(ventas)
print("cantidad de ventas", cantidad)
print("mayor venta", mayor)
print("menor venta", menor)
print("suma total", total)

# b) verificar pertenencia y ausencia
pertenece_150 = 150 in ventas
no_pertenece_500 = 500 not in ventas
print("esta el valor 150 en ventas?", pertenece_150)
print("esta ausente el valor 500 en ventas?", no_pertenece_500)

# c) contar cuántas veces aparece 150
contar = ventas.count(150)
print("cantidad de veces que aparece el 150", contar)

# d) buscar la primera posición de 230
valor_buscado = 230
if valor_buscado in ventas:
    posicion = ventas.index(valor_buscado)
    print(f"la primera posicion del valor buscado {valor_buscado} es el indice: {posicion}")
else:
    print("no se encuentra el valor buscado")

# e) concatenar y comprobar que se obtiene una nueva tupla
ventas_combinadas = ventas + (300, 250)
print("nueva tupla concatenada", ventas_combinadas)
print("tupla original", ventas)

# f) replicar una tupla tres veces
repeticion = (0, 1) * 3
print("resultado de la replicacion", repeticion)

# 6. Empaquetado y desempaquetado
dia = 25
mes = "Septiembre"
anio = 2026
fecha = dia, mes, anio
print(fecha)          
print(type(fecha))    

dia_nac, mes_nac, anio_nac = fecha
print(dia_nac)    
print(mes_nac)    
print(anio_nac)   

# Para desempaquetar la tupla se necesitan tres variables.
variable1, variable2, variable3 = fecha

# 7. Tuplas anidadas
alumnos = (
    ("Ana", (12, "Marzo", 2005)),
    ("Bruno", (8, "Julio", 2004)),
    ("Carla", (21, "Enero", 2005))
)

# a) nombre del segundo alumno
nombre_segundo = alumnos[1][0]
print(nombre_segundo)
# Bruno

# b) fecha completa del tercer alumno
fecha_tercero = alumnos[2][1]
print(fecha_tercero)
# (21, 'Enero', 2005)

# c) mes de nacimiento del primer alumno
mes_primero = alumnos[0][1][1]
print(mes_primero)
# Marzo

# d) recorrer y mostrar con formato legible
for nombre, (dia, mes, anio) in alumnos:
    print(f"estudiante: {nombre:<6}, nacimiento: {dia} de {mes} de {anio}")

# 8. Integracion con matrices
codigos = ("P101", "P205", "P330")
ventas_semanales = [
    [12, 15, 10, 18],
    [8, 11, 9, 14],
    [20, 17, 22, 19]
]

# a) Informar el total vendido por producto
def total_por_producto(codigos, ventas_semanales):
    print("total vendido por producto")
    for i in range(len(codigos)):
        total_acumulado = sum(ventas_semanales[i])
        print(f"producto {codigos[i]}: {total_acumulado} unidades vendidas")
# b) Informar el total de una semana indicada
def total_por_semana(ventas_semanales, nro_semana):
    if nro_semana < 1 or nro_semana > 4:
        print("error: la semana debe estar entre 1 y 4")
        return None
    columna = nro_semana - 1
    total_semana = 0
    for fila in ventas_semanales:
        total_semana += fila[columna]
    return total_semana
# c) Determinar el código del producto con mayor venta acumulada
def producto_mayor_venta(codigos, ventas_semanales):
    mayor_venta = -1
    codigo_mayor = ""
    for i in range(len(codigos)):
        total_acumulado = sum(ventas_semanales[i])
        if total_acumulado > mayor_venta:
            mayor_venta = total_acumulado
            codigo_mayor = codigos[i]
    return codigo_mayor
# d) Validar la semana sin provocar excepciones
def validar_semana(nro_semana):
    if not isinstance(nro_semana, int):
        print("error: la semana debe ser un numero entero")
        return False
    if nro_semana < 1 or nro_semana > 4:
        print("error: la semana debe estar entre 1 y 4")
        return False
    return True
total_por_producto(codigos, ventas_semanales)
semana = 2
if validar_semana(semana):
    print(f"total vendido en la semana {semana}: {total_por_semana(ventas_semanales, semana)} unidades")
print(f"producto con mayor venta acumulada: {producto_mayor_venta(codigos, ventas_semanales)}")
semana_invalida = 5
if not validar_semana(semana_invalida):
    print("no se puede calcular el total de una semana invalida")
