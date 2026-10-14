"""
EJERCICIO 9 - Acumulacion por clave y generacion de reporte

Archivo disponible: movimientos.txt
Formato:
cuenta;tipo;importe

tipo puede ser DEPOSITO o EXTRACCION.

Consigna:
Calcular el saldo neto de cada cuenta:
- DEPOSITO suma.
- EXTRACCION resta.

Luego generar el archivo resumen_cuentas.txt con:
cuenta;saldo

Ejemplo:
1001;25000

Ademas, mostrar por pantalla la cuenta con mayor saldo final.

Requisitos:
- Leer movimientos.txt una sola vez.
- Usar un diccionario para acumular saldos.
- Generar el archivo de salida al finalizar.
"""

# Escriba su solucion debajo de esta linea.

try:
    arch_entrada = open("movimientos.txt", mode="rt")
except OSError:
    print("No se pudo abrir el archivo movimientos.txt")
else:
    saldos = {}

    for linea in arch_entrada:
        cuenta, tipo, importe = linea.rstrip("\n").split(";")
        importe = int(importe)

        if cuenta not in saldos:
            saldos[cuenta] = 0

        if tipo == "DEPOSITO":
            saldos[cuenta] += importe
        elif tipo == "EXTRACCION":
            saldos[cuenta] -= importe

    arch_entrada.close()

    try:
        arch_salida = open("resumen_cuentas.txt", mode="wt")
    except OSError:
        print("No se pudo crear el archivo resumen_cuentas.txt")
    else:
        for cuenta in saldos:
            arch_salida.write(cuenta + ";" + str(saldos[cuenta]) + "\n")
        arch_salida.close()

        cuenta_mayor = ""
        saldo_mayor = 0
        for cuenta in saldos:
            if cuenta_mayor == "" or saldos[cuenta] > saldo_mayor:
                cuenta_mayor = cuenta
                saldo_mayor = saldos[cuenta]

        if cuenta_mayor != "":
            print("Cuenta con mayor saldo final:", cuenta_mayor)
            print("Saldo:", saldo_mayor)
        else:
            print("El archivo no contiene movimientos")
