def procesar_alumno(linea):
    campos = linea.rstrip("\n").split(";")

    if len(campos) != 3:
        return None

    legajo, nombre, comision = campos

    try:
        legajo = int(legajo)
        comision = int(comision)
    except ValueError:
        return None

    if legajo <= 0:
        return None

    if nombre.strip() == "":
        return None

    if comision < 1 or comision > 10:
        return None

    return [legajo, nombre, comision]


#01pruebas
def mostrar_alumnos():
    try:
        arch = open("alumnos.txt", mode="rt")
    except OSError:
        print("No se pudo abrir el archivo alumnos.txt")
    else:
        alumnos_por_comision = {}
        cantidad_validos = 0
        numero_linea = 0

        print("Alumnos validos:")

        for linea in arch:
            numero_linea += 1
            alumno = procesar_alumno(linea)

            if alumno is None:
                print("Registro invalido en la linea:", numero_linea)
            else:
                legajo, nombre, comision = alumno
                cantidad_validos += 1

                print("Legajo:", legajo)
                print("Nombre:", nombre)
                print("Comision:", comision)

                if legajo > 10000:
                    print("Alumno con legajo mayor a 10000:", nombre)

                if comision not in alumnos_por_comision:
                    alumnos_por_comision[comision] = 0

                alumnos_por_comision[comision] += 1

        arch.close()

        if cantidad_validos == 0:
            print("El archivo no contiene alumnos validos")

        print("Cantidad de alumnos por comision:")

        for comision in alumnos_por_comision:
            print("Comision", comision, ":",
                  alumnos_por_comision[comision])


mostrar_alumnos()