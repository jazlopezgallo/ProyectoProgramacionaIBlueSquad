# Orientador Cuatro: Tuplas y catálogo de productos

## Segmentación de actividades

### Actividad 3: Creación de tuplas

Se crean tuplas con varios elementos, una tupla vacía, una tupla de un solo
elemento y un registro. También se comprueba la diferencia entre `("Python")`
y `("Python",)`.

### Actividad 4: Acceso, recorrido y rebanadas

Se accede a posiciones de una tupla, se recorren sus elementos con `for` y se
usan rebanadas para obtener partes y para invertir el orden.

### Actividad 5: Operadores, funciones y métodos

Se aplican `len()`, `max()`, `min()`, `sum()`, `in`, `not in`, `count()` e
`index()`. También se muestran la concatenación y la replicación de tuplas.

### Actividad 6: Empaquetado y desempaquetado

Se agrupan valores en una tupla y luego se recuperan en variables separadas.

### Actividad 7: Tuplas anidadas

Se trabaja con alumnos y fechas de nacimiento almacenados dentro de tuplas
anidadas.

### Actividad 8: Integración con matrices

Una tupla almacena los códigos de producto y una matriz de listas almacena las
ventas semanales. Se calculan totales por producto, totales por semana y el
producto con mayor venta acumulada. La semana se valida antes de acceder a la
matriz.

### Actividad 9: Desafío integrador

`cargaDeProducto.py` implementa un catálogo dinámico. Cada registro es una
tupla `(codigo, descripcion, precio)` y el catálogo completo es una lista.
Incluye carga, visualización, búsqueda, mayor precio y promedio.

### Actividad 10: Verificación y análisis

`pruebas.py` verifica finalización con `FIN`, producto válido, precio escrito
con letras, precio cero, códigos repetidos, búsquedas, lista vacía y varios
productos. La ejecución usa solamente `print()` y muestra una tabla de
resultados lista para capturar. La validación del precio evita convertir texto
inválido y, por lo tanto, no necesita excepciones.

## Diferencias entre listas y tuplas

Una lista es mutable: permite agregar, quitar o modificar elementos. Una tupla
es inmutable: después de crearla no se pueden cambiar sus posiciones. Ambas
permiten guardar datos ordenados, acceder por índice, recorrer con `for` y usar
rebanadas.

## Reflexión individual

Elegiría una tupla cuando los datos deben permanecer constantes, por ejemplo
coordenadas, días de la semana o un registro fijo. Elegiría una lista cuando
necesite modificar, ordenar, agregar o eliminar elementos durante la ejecución.

## Ejecución

Desde esta carpeta ejecutar:

```text
python pruebas.py
```

Para usar el catálogo de forma interactiva:

```text
python cargaDeProducto.py
```