"""
EJERCICIO 10 - Integrador de archivos de texto

Archivo disponible: mediciones.txt
Formato:
zona;sector;humedad

Consigna:
Desarrollar un programa modular que:

1. Lea mediciones.txt registro por registro.
2. Obtenga por cada zona:
   - cantidad de mediciones
   - suma de humedad
   - humedad maxima
3. Genere informe_humedad.txt con una linea por zona:
   zona;promedio;maxima
4. Muestre por pantalla la zona con menor promedio de humedad.

Requisitos:
- Implementar al menos 3 funciones:
  a) leer/procesar el archivo
  b) calcular los resultados
  c) guardar el informe
- No usar readlines().
- No leer el archivo mas de una vez.
- Manejar posibles errores de apertura.
- Como desafio final, puede usar with open(...) y comparar esta forma
  con la apertura/cierre explicitos vistos en clase.
"""

# Escriba su solucion debajo de esta linea.

def leer_mediciones(nombre_archivo):
    try:
        arch = open(nombre_archivo, mode="rt")
    except OSError:
        print("No se pudo abrir el archivo", nombre_archivo)
        return None
    else:
        mediciones_por_zona = {}

        for linea in arch:
            zona, sector, humedad = linea.rstrip("\n").split(";")
            humedad = float(humedad)

            if zona not in mediciones_por_zona:
                mediciones_por_zona[zona] = {
                    "cantidad": 0,
                    "suma": 0,
                    "maxima": humedad,
                }

            mediciones_por_zona[zona]["cantidad"] += 1
            mediciones_por_zona[zona]["suma"] += humedad
            if humedad > mediciones_por_zona[zona]["maxima"]:
                mediciones_por_zona[zona]["maxima"] = humedad

        arch.close()
        return mediciones_por_zona


def calcular_resultados(mediciones_por_zona):
    resultados = {}
    for zona in mediciones_por_zona:
        cantidad = mediciones_por_zona[zona]["cantidad"]
        suma = mediciones_por_zona[zona]["suma"]
        maxima = mediciones_por_zona[zona]["maxima"]
        promedio = suma / cantidad
        resultados[zona] = [promedio, maxima]
    return resultados


def guardar_informe(nombre_archivo, resultados):
    try:
        arch = open(nombre_archivo, mode="wt")
    except OSError:
        print("No se pudo crear el archivo", nombre_archivo)
        return False
    else:
        for zona in resultados:
            promedio, maxima = resultados[zona]
            arch.write(zona + ";" + str(promedio) + ";" + str(maxima) + "\n")

        arch.close()
        return True


mediciones = leer_mediciones("mediciones.txt")
if mediciones is not None:
    resultados = calcular_resultados(mediciones)
    if guardar_informe("informe_humedad.txt", resultados):
        zona_menor_promedio = ""
        promedio_menor = 0

        for zona in resultados:
            promedio = resultados[zona][0]
            if zona_menor_promedio == "" or promedio < promedio_menor:
                zona_menor_promedio = zona
                promedio_menor = promedio

        if zona_menor_promedio != "":
            print("Zona con menor promedio de humedad:", zona_menor_promedio)
            print("Promedio:", promedio_menor)
        else:
            print("El archivo no contiene mediciones")
