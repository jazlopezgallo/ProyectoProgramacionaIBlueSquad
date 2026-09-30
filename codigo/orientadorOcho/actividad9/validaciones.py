import re

def validar_nombre(nombre):
    if re.fullmatch(r"[A-Za-zÁ-Úá-úñÑ\s]{2,50}", nombre) is not None:
        return True
    else:
        print("Error: El nombre solo debe contener letras y espacios (entre 2 y 50 caracteres).")
        return False

def validar_legajo(legajo):
    if re.fullmatch(r"[0-9]{5}", legajo) is not None:
        return True
    else:
        print("Error: El legajo debe tener exactamente 5 números.")
        return False

def validar_correo(correo):
    if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", correo) is not None:
        return True
    else:
        print("Error: Formato de correo inválido (ejemplo: usuario@dominio.com).")
        return False

def validar_telefono(telefono):
    if re.fullmatch(r"[0-9]{4}-[0-9]{4}", telefono) is not None:
        return True
    else:
        print("Error: Teléfono inválido. Debe tener el formato XXXX-XXXX.")
        return False

def validar_comision(comision):
    if re.fullmatch(r"[A-Z]{3}[0-9]{4}", comision) is not None:
        return True
    else:
        print("Error: El código debe tener 3 letras mayúsculas seguidas de 4 números (ej. ABC1234).")
        return False