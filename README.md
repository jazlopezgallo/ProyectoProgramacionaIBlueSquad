# Portafolio de entrega

## Programación I

**Carrera:** Licenciatura en Análisis  
**Institución:** UADE  
**Año:** Primer año  
**Materia:** Programación I  
**Clase:** 4 - Git, GitHub y cadenas de caracteres

### Grupo: BlueSquad

**GitHub:** [ProyectoProgramacionaIBlueSquad](https://github.com/jazlopezgallo/ProyectoProgramacionaIBlueSquad)

**Integrantes:** Agustina Mendoza, Jazmin Lopez Gallo y Mauricio Abel Cuellar

## Descripción

Este repositorio contiene los ejercicios y actividades prácticas realizados
por el grupo BlueSquad durante la materia Programación I. El portfolio se
completará progresivamente con los trabajos de los orientadores 1, 2, 3 y 4.

Los ejercicios están desarrollados principalmente en Python y se organizan por
orientador para facilitar la lectura, la ejecución y la revisión de cada
actividad.

## Organización del portfolio

### Orientador 1

En esta sección se incorporarán los primeros ejercicios de programación. Se
organizarán por actividad y permitirán consultar los conceptos iniciales, los
algoritmos y las soluciones trabajadas en clase.

**Estado:** pendiente de incorporar.

### Orientador 2

En esta sección se incorporarán los ejercicios correspondientes al segundo
orientador, manteniendo la separación por actividad y archivo fuente.

**Estado:** pendiente de incorporar.

### Orientador 3

Esta sección reúne ejercicios de cadenas de caracteres, funciones, métodos y
procesamiento de texto. Cada archivo contiene la resolución de una actividad y,
cuando corresponde, sus casos de prueba.

**Ubicación:** [`codigo/orientadorTres`](codigo/orientadorTres)

### Orientador 4

Esta sección trabaja con tuplas, tuplas anidadas, operadores, funciones,
métodos, matrices y un desafío integrador de catálogo de productos.

La segmentación de actividades es la siguiente:

- **Actividad 3:** creación de tuplas y reconocimiento de tuplas de uno o más elementos.
- **Actividad 4:** acceso por índice, recorrido y rebanadas de tuplas.
- **Actividad 5:** operadores, funciones y métodos como `len()`, `max()`, `min()`, `sum()`, `in`, `not in`, `count()` e `index()`.
- **Actividad 6:** empaquetado y desempaquetado de valores.
- **Actividad 7:** tuplas anidadas con datos de alumnos y fechas.
- **Actividad 8:** integración de códigos almacenados en una tupla con una matriz de ventas semanales.
- **Actividad 9:** catálogo de productos con registros representados mediante tuplas y un catálogo almacenado en una lista.
- **Actividad 10:** verificación y análisis mediante casos de prueba.

**Ubicación:** [`codigo/orientadorCuatro`](codigo/orientadorCuatro)

## Estructura esperada

A medida que se incorporen los trabajos faltantes, el repositorio tendrá una
organización similar a la siguiente:

```text
codigo/
├── orientadorUno/
├── orientadorDos/
├── orientadorTres/
└── orientadorCuatro/
```

Cada carpeta puede incluir los archivos `.py`, los casos de prueba y un README
específico con la explicación de sus actividades.

## Contenido del portfolio

El documento grupal incluirá:

- Código fuente de todos los ejercicios.
- Capturas de ejecución.
- Tablas de casos de prueba.
- Explicación de las diferencias entre listas y tuplas.
- Justificación del uso de tuplas para los registros y de listas para el catálogo.
- Reflexión individual de cada integrante sobre cuándo elegir una tupla en lugar de una lista.

## Listas y tuplas

Las listas son estructuras mutables: permiten agregar, eliminar y modificar
elementos. Las tuplas son estructuras inmutables: una vez creadas, sus
posiciones no pueden modificarse.

En el desafío del orientador 4, cada registro se representa mediante una tupla
porque tiene una estructura fija formada por código, descripción y precio. El
catálogo completo se representa mediante una lista porque puede crecer durante
la carga y permite agregar nuevos registros.

## Ejecución

Para ejecutar un ejercicio, ingresar a la carpeta correspondiente y utilizar:

```text
python nombre_del_archivo.py
```

Por ejemplo, para ejecutar las pruebas del catálogo del orientador 4:

```text
cd codigo/orientadorCuatro
python pruebas.py
```
