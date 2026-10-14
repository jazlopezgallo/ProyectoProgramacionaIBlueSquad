# Orientador Diez: Archivos de texto

Este orientador practica la lectura y escritura de archivos de texto, el
procesamiento secuencial de registros, la validacion de datos y el uso de
funciones para organizar un programa.

## Ejercicios de practica

La carpeta `ejerciciosDePracticas` contiene diez programas que trabajan con
archivos de texto y datos delimitados por punto y coma:

1. Crear un archivo y guardar nombres ingresados por teclado.
2. Leer mensajes registro por registro y contar lineas.
3. Filtrar alumnos por numero de legajo.
4. Acumular importes y unidades de ventas.
5. Buscar un producto mediante busqueda secuencial.
6. Leer notas y generar el archivo de alumnos aprobados.
7. Descartar registros invalidos de stock y sumar las cantidades validas.
8. Contar reclamos por categoria usando un diccionario.
9. Calcular saldos por cuenta y generar un archivo de resumen.
10. Procesar mediciones por zona y crear un informe con promedios y maximos.

Los programas leen sus archivos de entrada registro por registro y cierran los
archivos al finalizar. Los ejercicios que generan archivos de salida los crean
en el directorio desde el que se ejecuta el programa.

## Desafio aplicado al Proyecto Integrador

`crearEntregas.py` gestiona las entregas de grupos mediante `entregas.csv`.
Cada registro contiene numero de grupo, nombre del proyecto, responsable y
porcentaje de avance, separados por punto y coma.

El programa esta dividido en funciones para:

- Crear el archivo y escribir el encabezado solo si el archivo esta vacio.
- Cargar entregas, validando los campos y evitando repetir numeros de grupo.
- Mostrar las entregas validas.
- Buscar una entrega por numero de grupo.
- Mostrar proyectos con avance inferior al 50 por ciento.
- Calcular el promedio de avance si existen registros validos.
- Informar y omitir registros mal formados.

Para ejecutar el desafio, ubicarse en `codigo/orientadorDiez` y ejecutar:

```text
python crearEntregas.py
```

La ejecucion prepara el archivo sin borrar entregas existentes, permite cargar
nuevos registros hasta ingresar `-1` como numero de grupo y luego muestra las
entregas, solicita un grupo para buscar, informa los proyectos con menos del
50 por ciento de avance y calcula el promedio.

El archivo se procesa secuencialmente en cada operacion; no se carga completo en
memoria. Los registros validos requieren cuatro campos, un numero de grupo
positivo, campos de proyecto y responsable no vacios y un avance entre 0 y 100.

## Conceptos trabajados

- Modos de apertura de texto: lectura (`rt`), escritura (`wt`) y agregado (`at`).
- Lectura secuencial con `for linea in arch`.
- Separacion de campos con `split(";")` y eliminacion del salto de linea con
  `rstrip("\n")`.
- Conversion de cadenas a `int` y `float`, con manejo de `ValueError`.
- Validacion de registros antes de procesarlos.
- Uso de diccionarios para evitar grupos repetidos durante la carga.
- Cierre explicito de los archivos.
