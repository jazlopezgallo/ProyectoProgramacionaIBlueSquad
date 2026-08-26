  # Orientador tres- BlueSquad

## Descripción

Este repositorio contiene las actividades prácticas del orientador de clase **Git, GitHub y cadenas de caracteres**, correspondiente a la materia **Programación I / Algoritmos y Estructuras I**.

El trabajo integra:

- Fundamentos de Git y GitHub.
- Cadenas de caracteres en Python.
- Operadores, funciones y métodos de cadenas.
- Conversión de tipos y formateo de datos.
- Organización de un programa mediante funciones.
- Trabajo colaborativo y registro de cambios.

## Estructura del proyecto

```text
ProyectoProgramacionaIBlueSquad/
├── cadenaDeCaracteres.py
├── funcionesMetodos.py
├── perfil_equipo.py
├── principal.py
├── casos_prueba_perfil_equipo.md
└── README.md
```

## Relación entre la actividad y los archivos

### `principal.py`

Contiene el primer programa del Proyecto Integrador:

```python
print("Primer programa del Proyecto Integrador")
```

Este archivo representa el inicio del proyecto y la primera estructura creada por el equipo.

### `cadenaDeCaracteres.py`

Desarrolla el punto 5 del PDF, **Cadenas de caracteres**. Incluye:

- Acceso al primer y al último carácter.
- Slicing para obtener `Programacion`.
- Inversión de una cadena.
- Verificación de pertenencia con el operador `in`.
- Demostración de la inmutabilidad de las cadenas.

La instrucción `texto[0] = "p"` produce un `TypeError`, porque una cadena no permite reemplazar directamente uno de sus caracteres. El archivo deja esta operación como demostración del error solicitado en la actividad.

### `funcionesMetodos.py`

Desarrolla los puntos 6 y 7 del PDF.

En la primera parte se prueban métodos de cadenas:

- Transformación: `upper()`, `lower()`, `title()`, `capitalize()` y `replace()`.
- Consulta: `count()`, `find()` y `len()`.
- Validación: `isalpha()`, `isdigit()` e `isalnum()`.

Los métodos de transformación retornan una nueva cadena y no modifican el texto original. Los métodos de validación, en cambio, devuelven un valor booleano (`True` o `False`).

En la segunda parte se solicita el nombre de un producto, su precio unitario y la cantidad. El precio se convierte a `float`, la cantidad a `int` y luego se calcula el importe total. El resultado se muestra mediante:

1. Una f-string con dos decimales.
2. Concatenación, convirtiendo el valor numérico con `str()`.

### `perfil_equipo.py`

Desarrolla el punto 8, **Actividad integradora: perfil del equipo**. El programa solicita:

- Nombre del equipo.
- Comisión.
- Cantidad de integrantes.
- Nombre y rol inicial de cada integrante.

Luego procesa y muestra la información del equipo. Para ello:

- Normaliza los nombres usando `title()`.
- Convierte el nombre del equipo a mayúsculas.
- Cuenta sus caracteres con `len()`.
- Genera una sigla con la inicial de cada palabra.
- Recorre el nombre del equipo para verificar si contiene algún dígito mediante `isdigit()`.
- Muestra los resultados usando f-strings.

Las operaciones principales están organizadas en funciones:

- `normalizar_nombre()`
- `generar_sigla()`
- `contiene_digitos()`

La entrada y salida general se mantiene en el programa principal.

### `casos_prueba_perfil_equipo.md`

Documenta el punto 10 del PDF, **Verificación y análisis**. Incluye los resultados esperados y obtenidos para:

- Un nombre de equipo formado por varias palabras.
- Un nombre con letras y números.
- Datos válidos de precio y cantidad.
- La concatenación de una cadena con un número sin utilizar `str()`.
- La búsqueda de un texto inexistente con `find()`.

## Conceptos aprendidos

### Inmutabilidad de las cadenas

Las cadenas son secuencias ordenadas de caracteres, pero son inmutables. Se pueden consultar, recorrer y obtener partes mediante slicing, pero no se puede cambiar un carácter usando su índice. Para modificar un texto es necesario crear una cadena nueva.

### Transformar y validar

Los métodos de transformación generan un nuevo texto, por ejemplo `texto.upper()`. Los métodos de validación analizan el contenido y devuelven un booleano, por ejemplo `texto.isalpha()`.

`isalpha()` devuelve `False` para `"Programacion en Python"` porque la cadena contiene espacios. Aunque cada palabra tenga solamente letras, el texto completo también contiene caracteres que no son alfabéticos.

### Conversión y concatenación

`input()` siempre devuelve cadenas. Por eso es necesario convertir los datos numéricos:

```python
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
```

No se puede concatenar directamente una cadena con un número. Para hacerlo mediante `+`, el número debe convertirse explícitamente con `str()`.

## Cómo ejecutar los programas

Desde la carpeta del proyecto, utilizar Python 3:

```bash
python principal.py
python cadenaDeCaracteres.py
python funcionesMetodos.py
python perfil_equipo.py
```

`cadenaDeCaracteres.py` genera intencionalmente un `TypeError` al llegar a la línea que intenta modificar una cadena. Esto permite observar y explicar la inmutabilidad solicitada en el punto 5.

`funcionesMetodos.py` y `perfil_equipo.py` solicitan datos por consola, por lo que deben ejecutarse en una terminal interactiva.

## Mensajes de commit sugeridos

- `Crea la estructura inicial del proyecto`
- `Agrega ejercicios de cadenas`
- `Implementa el perfil inicial del equipo`
- `Documenta los casos de prueba`

