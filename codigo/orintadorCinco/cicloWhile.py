#2. Ciclos controlados con while True
suma = 0
cantidad = 0

while True:
    nro = int(input("Ingrese un número entero (-1 para finalizar): "))
    if nro == -1:
        break
    suma = suma + nro
    cantidad = cantidad + 1

if cantidad > 0:
    promedio = suma / cantidad
    print(f"Cantidad: {cantidad}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No hay datos para calcular el promedio")