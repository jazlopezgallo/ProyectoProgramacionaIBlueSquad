import validaciones as val
def inputs():
    nombre = input("Ingrese su nombre: ")
    while not val.validar_nombre(nombre):
        nombre = input("Ingrese su nombre: ")
        
    legajo = input("Ingrese su legajo (5 dígitos): ")
    while not val.validar_legajo(legajo):
        legajo = input("Ingrese su legajo (5 dígitos): ")
        
    correo = input("Ingrese su correo electrónico: ")
    while not val.validar_correo(correo):
        correo = input("Ingrese su correo electrónico: ")
        
    telefono = input("Ingrese su teléfono (XXXX-XXXX): ")
    while not val.validar_telefono(telefono):
        telefono = input("Ingrese su teléfono (XXXX-XXXX): ")
        
    comision = input("Ingrese su código de comisión (ej. ABC1234): ")
    while not val.validar_comision(comision):
        comision = input("Ingrese su código de comisión (ej. ABC1234): ")
        
    return nombre, legajo, correo, telefono, comision

def prints(nombre, legajo, correo, telefono, comision):
    print("\n--- Datos Registrados Exitosamente ---")
    print(f"Nombre:   {nombre}")
    print(f"Legajo:   {legajo}")
    print(f"Correo:   {correo}")
    print(f"Teléfono: {telefono}")
    print(f"Comisión: {comision}")

def main():
    menu = input("Ingrese 1 para salir o cualquier tecla para registrar un usuario: ")
    while menu != "1":
        nombre, legajo, correo, telefono, comision = inputs()
        prints(nombre, legajo, correo, telefono, comision)
        menu = input("\nIngrese 1 para salir o cualquier tecla para registrar otro usuario: ")

if __name__ == "__main__":
    main()