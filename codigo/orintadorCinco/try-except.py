#4. Captura con try-except
valores_validos = []

while True:
    dato = input("Ingrese un número entero (FIN para terminar): ")
    if dato == "FIN":
        break

    try:
        numero = int(dato)
        valores_validos.append(numero)
    except ValueError:
        print("Error: debe ingresar un número entero")

print("Valores cargados:", valores_validos)
#5. Múltiples excepciones y reglas del problema
numeros = [10, 20, 30, 40]
#6. Cláusulas else y finally
try:
    posicion = int(input("Posición: "))
    if posicion < 0 or posicion > len(numeros) - 1:
        raise ValueError("La posición debe estar entre 0 y " + str(len(numeros) - 1))
    print(numeros[posicion])
except ValueError as error:
    print("Error:", error)
except IndexError:
    print("La lista no tiene tantos elementos")

try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    resultado = numero1 / numero2
except ValueError:
    print("Error: debe ingresar valores numéricos")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
else:
    print(f"El resultado de la división es: {resultado:.2f}")
finally:
    print("Fin del intento de cálculo")

#7. Provocar una excepción con raise
def calcular_importe(cantidad, precio):
    """Retorna cantidad * precio. Lanza ValueError si algún dato no es válido."""
    if cantidad <= 0 or precio <= 0:
        raise ValueError("Cantidad y precio deben ser mayores a cero")
    return cantidad * precio


try:
    cantidad = float(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    importe = calcular_importe(cantidad, precio)
    print(f"El importe es: {importe:.2f}")
except ValueError as error:
    print("Error:", error)

#8. Comprobaciones internas con assert 
importe = calcular_importe(3, 1200)
assert importe == 3600, "El importe calculado no es el esperado"
# Aserción que verifica un caso correcto
importe2 = calcular_importe(5, 200)
assert importe2 == 1000, "El importe de 5 x 200 debería ser 1000"
# Aserción que falla intencionalmente
assert importe2 == 2000, "Fallo intencional: el importe no es 2000"
