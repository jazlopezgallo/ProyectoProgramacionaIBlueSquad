texto = "Programacion en Python"

print(texto.upper())          
print(texto.lower())          
print(texto.title())          
print(texto.capitalize())     
print(texto.replace("Python", "IA"))   
print(texto.count("a"))      
print(texto.find("Python"))   
print(len(texto))             
#Métodos de validación, con distintas cadenas:
print("Programacion".isalpha())              # True
print("2026".isdigit())                      # True
print("Python3".isalnum())                   # True
print("Programacion en Python".isalpha())     # False

#7. Conversión de tipos y formateo
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad

# a) f-string con dos decimales
print(f"El importe total de {producto} es ${total:.2f}")

# b) Concatenación, convirtiendo con str()
print("El importe total de " + producto + " es $" + str(round(total, 2)))