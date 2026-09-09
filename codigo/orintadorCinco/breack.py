#1. Finalización anticipada de un ciclo: break
def es_primo(numero):
    """Retorna True si el número es primo, False en caso contrario."""
    if numero < 2:
        return False

    primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

    return primo
# a) Pruebas
print(es_primo(-3))   # False
print(es_primo(0))    # False
print(es_primo(1))    # False
print(es_primo(2))    # True
print(es_primo(9))    # False
print(es_primo(17))   # True
print(es_primo(25))   # False
#d) Comparación con una versión que recorra todos los divisores:
def es_primo_sin_break(numero):
    """Misma lógica, pero recorre todos los divisores posibles."""
    if numero < 2:
        return False

    primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False

    return primo
