def crear_entregas():
    try:
        arch = open("entregas.csv", mode="at")
    except OSError:
        print("No se pudo crear el archivo entregas.csv")
        return False
    else:
        if arch.tell() == 0:
            arch.write("grupo;proyecto;responsable;avance\n")
        arch.close()
        print("Archivo entregas.csv preparado")
        return True

# funcion auxiliar para cargar entregas
def procesar_entrega(linea):
    campos = linea.rstrip("\n").split(";")

    if len(campos) != 4:
        return None

    grupo, proyecto, responsable, avance = campos

    if proyecto.strip() == "" or responsable.strip() == "":
        return None

    try:
        grupo = int(grupo)
        avance = float(avance)
    except ValueError:
        return None

    if grupo <= 0:
        return None

    if not (0 <= avance <= 100):
        return None

    return [grupo, proyecto, responsable, avance]

#a) y b). Cargar entregas sin repetir el número de grupo
def cargar_entregas():
    try:
        arch = open("entregas.csv", mode="rt")
    except OSError:
        print("No se pudo abrir el archivo entregas.csv")
        return
    else:
        grupos = {}
        arch.readline()
        numero_linea = 1

        for linea in arch:
            numero_linea += 1
            entrega = procesar_entrega(linea)

            if entrega is None:
                print("Registro invalido en la linea:", numero_linea)
            else:
                grupos[entrega[0]] = True

        arch.close()

    try:
        arch = open("entregas.csv", mode="at")
    except OSError:
        print("No se pudo abrir el archivo para agregar entregas")
    else:
        grupo_texto = input("Ingrese el numero de grupo (-1 para terminar): ")

        while grupo_texto != "-1":
            try:
                grupo = int(grupo_texto)
            except ValueError:
                print("El numero de grupo debe ser numerico")
            else:
                if grupo <= 0:
                    print("El numero de grupo debe ser positivo")
                elif grupo in grupos:
                    print("El numero de grupo ya existe")
                else:
                    proyecto = input("Ingrese el nombre del proyecto: ").strip()
                    responsable = input("Ingrese el responsable: ").strip()
                    avance_texto = input("Ingrese el porcentaje de avance: ")

                    if proyecto == "" or responsable == "":
                        print("Los campos de texto no pueden estar vacios")
                    else:
                        try:
                            avance = float(avance_texto)
                        except ValueError:
                            print("El avance debe ser numerico")
                        else:
                            if not (0 <= avance <= 100):
                                print("El avance debe estar entre 0 y 100")
                            else:
                                arch.write(
                                    str(grupo) + ";" + proyecto + ";" +
                                    responsable + ";" + str(avance) + "\n"
                                )
                                grupos[grupo] = True
                                print("Entrega guardada")

            grupo_texto = input(
                "Ingrese el numero de grupo (-1 para terminar): "
            )

        arch.close()
        print("Carga de entregas finalizada")
#c) Mostrar todas las entregas válidas
def mostrar_entregas():
    try:
        arch = open("entregas.csv", mode="rt")
    except OSError:
        print("No se pudo abrir el archivo entregas.csv")
    else:
        arch.readline()
        numero_linea = 1
        hay_entregas = False

        for linea in arch:
            numero_linea += 1
            entrega = procesar_entrega(linea)

            if entrega is None:
                print("Registro invalido en la linea:", numero_linea)
            else:
                grupo, proyecto, responsable, avance = entrega
                hay_entregas = True

                print("Grupo:", grupo)
                print("Proyecto:", proyecto)
                print("Responsable:", responsable)
                print("Avance:", avance, "%")

        arch.close()

        if not hay_entregas:
            print("El archivo no contiene entregas validas")

#d) Buscar una entrega por número de grupo
def buscar_entrega():
    grupo_texto = input("Ingrese el numero de grupo a buscar: ")

    try:
        grupo_buscado = int(grupo_texto)
    except ValueError:
        print("El numero de grupo debe ser numerico")
        return

    try:
        arch = open("entregas.csv", mode="rt")
    except OSError:
        print("No se pudo abrir el archivo entregas.csv")
    else:
        arch.readline()
        numero_linea = 1
        encontrado = False

        for linea in arch:
            numero_linea += 1
            entrega = procesar_entrega(linea)

            if entrega is None:
                print("Registro invalido en la linea:", numero_linea)
            else:
                grupo, proyecto, responsable, avance = entrega

                if grupo == grupo_buscado:
                    print("Proyecto:", proyecto)
                    print("Responsable:", responsable)
                    print("Avance:", avance, "%")
                    encontrado = True

        arch.close()

        if not encontrado:
            print("Grupo inexistente")

#e) Informar proyectos con avance inferior al 50 %
def mostrar_menores_50():
    try:
        arch = open("entregas.csv", mode="rt")
    except OSError:
        print("No se pudo abrir el archivo entregas.csv")
    else:
        arch.readline()
        numero_linea = 1
        hay_proyectos = False

        for linea in arch:
            numero_linea += 1
            entrega = procesar_entrega(linea)

            if entrega is None:
                print("Registro invalido en la linea:", numero_linea)
            else:
                grupo, proyecto, responsable, avance = entrega

                if avance < 50:
                    print("Grupo:", grupo, "- Proyecto:", proyecto)
                    print("Avance:", avance, "%")
                    hay_proyectos = True

        arch.close()

        if not hay_proyectos:
            print("No hay proyectos con avance inferior al 50%")
#f) Calcular el promedio de avance sin dividir por cero
def calcular_promedio_avance():
    try:
        arch = open("entregas.csv", mode="rt")
    except OSError:
        print("No se pudo abrir el archivo entregas.csv")
    else:
        arch.readline()
        suma_avances = 0
        cantidad_entregas = 0
        numero_linea = 1

        for linea in arch:
            numero_linea += 1
            entrega = procesar_entrega(linea)

            if entrega is None:
                print("Registro invalido en la linea:", numero_linea)
            else:
                avance = entrega[3]
                suma_avances += avance
                cantidad_entregas += 1

        arch.close()

        if cantidad_entregas > 0:
            promedio = suma_avances / cantidad_entregas
            print("Promedio de avance:", promedio)
        else:
            print("No hay entregas validas para calcular el promedio")


def main():
    if crear_entregas():
        cargar_entregas()
        mostrar_entregas()
        buscar_entrega()
        mostrar_menores_50()
        calcular_promedio_avance()


if __name__ == "__main__":
    main()