import validaciones as val


def probar_validacion(nombre_campo, funcion, ejemplos):
    print(f"\n{nombre_campo}")
    for dato, resultado_esperado in ejemplos:
        resultado = funcion(dato)
        estado = "CORRECTO" if resultado == resultado_esperado else "REVISAR"
        print(
            f"  {dato!r}: resultado={resultado}, "
            f"esperado={resultado_esperado} [{estado}]"
        )


def main():
    print("Ejemplos de prueba para las validaciones del formulario")
    probar_validacion(
        "Nombre",
        val.validar_nombre,
        [("Ana Pérez", True), ("José Luis", True), ("Ana3", False)],
    )
    probar_validacion(
        "Legajo",
        val.validar_legajo,
        [("12345", True), ("00015", True), ("1234", False)],
    )
    probar_validacion(
        "Correo",
        val.validar_correo,
        [("ana@mail.com", True), ("alumno.25@correo.org", True), ("ana@mail", False)],
    )
    probar_validacion(
        "Teléfono",
        val.validar_telefono,
        [("1234-5678", True), ("0001-2345", True), ("12345678", False)],
    )
    probar_validacion(
        "Comisión",
        val.validar_comision,
        [("ABC1234", True), ("MAT0007", True), ("abc1234", False)],
    )


if __name__ == "__main__":
    main()
