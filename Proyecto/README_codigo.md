# BlueSquad SalesMatrix — documentación técnica

Este proyecto implementa una pequeña aplicación de consola para registrar ventas, administrar vendedores y productos, y consultar informes útiles para una empresa de ventas.

La estructura del trabajo está organizada en tres archivos principales:

- [Proyecto/main_corregido.py](Proyecto/main_corregido.py): módulo de interfaz y menús.
- [Proyecto/operaciones_corregido.py](Proyecto/operaciones_corregido.py): lógica de negocio, validaciones, búsquedas e informes.
- [Proyecto/datos.py](Proyecto/datos.py): datos base del sistema y configuración inicial.

La idea de esta organización es separar claramente la capa de presentación de la capa de cálculo, evitando mezclar mensajes de consola con reglas del negocio.

## 1. Estructura del proyecto

### datos.py

Este archivo contiene la carga inicial del sistema. Define:

- los meses del año;
- la lista inicial de vendedores;
- los códigos iniciales de vendedores;
- las comisiones iniciales de los vendedores;
- la lista inicial de productos;
- los códigos y precios iniciales de los productos;
- la matriz de vendedores y la matriz de productos en ceros;
- el objetivo mensual del negocio.

Su función es ser el archivo de datos base, sin pedir información ni imprimir mensajes.

### operaciones_corregido.py

Este archivo contiene la lógica del sistema. En él se resuelven:

- validaciones de texto y enteros;
- búsqueda de elementos por código;
- alta y baja de vendedores;
- alta y baja de productos;
- registro de venta;
- cálculos de reportes y rankings;
- consulta de importes, comisiones y proyecciones.

Todas estas funciones reciben datos por parámetros y devuelven un resultado con una tupla que permite al archivo de interfaz mostrar mensajes de acuerdo con el éxito o el error de la operación.

### main_corregido.py

Este archivo funciona como capa de presentación. Su rol es:

- mostrar colores para mensajes de error, éxito e información;
- mostrar menús y matrices;
- pedir información por consola;
- delegar las decisiones de negocio en operaciones_corregido.py;
- conectar el flujo principal entre la pantalla del administrador y la pantalla del vendedor.

El archivo principal no reemplaza la lógica del negocio y no debe multiplicar validaciones.

## 2. Flujo principal

Cuando el programa arranca, se construyen los datos de base a partir de `datos.creaciondatos()`:

- listas paralelas para vendedores: IDs, nombres y comisiones;
- listas paralelas para productos: IDs, nombres y precios;
- matrices para guardar importes y unidades por mes;
- lista `meses_registrados` para saber si un mes ya fue usado.

El usuario ingresa al sistema por la opción principal:

1. Administrador
2. Vendedor
3. Salir

Si el usuario elige administrador, puede:

- gestionar vendedores;
- gestionar productos;
- registrar una venta;
- consultar matrices;
- consultar el producto más vendido;
- consultar el vendedor mayor volumen;
- consultar el mes con mayor cantidad de unidades;
- consultar el ranking de vendedores y el top 3;
- consultar el cumplimiento del objetivo mensual.

Si el usuario elige vendedor, ingresa su código y luego puede:

- registrar una venta con su código ya fijo;
- consultar su importe total vendido;
- consultar su comisión;
- consultar su proyección estimada anual.

## 3. Modelo de datos

El proyecto usa una representación simple basada en listas paralelas y matrices:

- El arreglo de IDs, nombres y comisiones de los vendedores queda sincronizado con las columnas de la matriz de vendedores.
- El arreglo de IDs, nombres y precios de los productos queda sincronizado con las columnas de la matriz de productos.
- La matriz de vendedores representa el importe vendido por vendedor y por mes.
- La matriz de productos representa la cantidad de unidades vendidas por producto y por mes.
- La lista `meses_registrados` indica qué meses ya fueron usados en alguna venta.

## 4. Reglas de validación

Las principales validaciones implementadas están en el módulo de operaciones:

- los códigos deben ser válidos y no duplicados;
- los nombres no pueden quedar vacíos ni repetirse;
- la comisión debe estar entre 0 y 100;
- el precio de producto debe ser mayor que cero;
- la cantidad de unidades vendidas debe ser mayor que cero;
- el mes debe estar dentro del rango 1–12;
- el vendedor y el producto deben existir antes de registrar una venta.

La filosofía es respetar la restricción de la entrega: no usar manejo de excepciones para esta primera etapa.

## 5. Reglas de cálculo

La lógica de negocio resuelve informes usando las matrices acumuladas:

- el total anual de ventas de la empresa;
- el importe total vendido por vendedor;
- la comisión del vendedor;
- el promedio mensual y la proyección anual;
- el producto más vendido;
- el vendedor con mayor volumen de ventas;
- el mes con mayor cantidad de unidades;
- el ranking de vendedores y el top 3;
- el cumplimiento del objetivo del mes.

## 6. Interfaz y salida por consola

El archivo principal usa colores de salida para diferenciar mensajes:

- rojo para errores;
- verde para mensajes de éxito;
- azul para encabezados o menús de información.

Esto ayuda a hacer la consola más legible y a distinguir mejor el resultado de las operaciones.

## 7. Observaciones finales

El proyecto está pensado para una entrega de programación inicial y mantiene una estructura clara:

- `datos.py` define datos de arranque;
- `operaciones_corregido.py` recoge reglas y cálculos;
- `main_corregido.py` maneja la interacción con el usuario.

La solución es simple, didáctica y adecuada para una primera etapa de implementación, porque separa el problema en capas sin introducir complejidades adicionales como clases o archivos nuevos.
