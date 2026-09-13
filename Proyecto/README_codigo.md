# BlueSquad SalesMatrix — documentación técnica

Este proyecto implementa una aplicación de consola para registrar ventas, administrar vendedores y productos y consultar reportes de cumplimiento operativos. La lógica está organizada en tres archivos principales que representan una separación clara entre datos, lógica de negocio e interfaz:

- `datos.py`: carga la estructura inicial del sistema.
- `operaciones.py`: contiene las validaciones, búsquedas, altas, bajas, registro de ventas y cálculos estadísticos.
- `main.py`: integra la interfaz por consola y delega las operaciones en `operaciones.py`.

La intención del proyecto es mantener una solución simple, legible y educativa, siguiendo el estilo de una primera entrega de programación en Python.

## 1. Objetivo del sistema

BlueSquad SalesMatrix es una pequeña aplicación de gestión comercial para una empresa de ventas. El sistema permite:

- registrar vendedores y productos;
- dar de alta y baja vendedores y productos;
- registrar ventas con vendedor, producto, mes y cantidad;
- consultar matrices de acumulación por vendedor y producto;
- identificar el producto más vendido;
- identificar el vendedor de mayor volumen;
- identificar el mes con mayor cantidad de unidades vendidas;
- construir rankings de vendedores;
- comparar el cumplimiento del objetivo mensual del negocio.

## 2. Estructura actual del proyecto

### `datos.py`

Este archivo es el módulo de datos base. Su función es preparar el estado inicial de la aplicación, sin pedir información ni imprimir mensajes. En la versión actual, la función principal es:

- `creaciondatos()`

La función construye:

- `meses`: tupla con los doce meses del año;
- `vendedores`: nombres de los vendedores iniciales;
- `vendedores_id_inicial`: códigos iniciales de vendedores;
- `vendedores_comision_inicial`: comisiones iniciales de cada vendedor expresadas como porcentaje decimal;
- `productos`: nombres iniciales de productos;
- `productos_id_inicial`: códigos de productos;
- `precios`: precios unitarios de cada producto;
- `matriz_vendedores`: matriz de importes acumulados por vendedor y mes;
- `matriz_productos`: matriz de unidades acumuladas por producto y mes;
- `objetivo_mensual`: meta comercial mensual.

El paquete de datos es una fuente de inspiración para el arranque del programa. Mantener estos valores en un archivo separado ayuda a que el proyecto sea más limpio y reutilizable.

### `operaciones.py`

Este archivo contiene la lógica central del negocio. Aquí se resuelven:

- validaciones sencillas de texto, enteros y rangos;
- búsqueda secuencial de listas;
- alta y baja de vendedores;
- alta y baja de productos;
- registro de ventas;
- cálculo de total de ventas por vendedor;
- cálculo de comisión por vendedor;
- cálculo de proyección anual;
- búsqueda del producto más vendido;
- búsqueda del vendedor con mayor volumen;
- cálculo del mes con mayor número de unidades;
- ranking de vendedores y top 3;
- cumplimiento del objetivo mensual.

Además, el diseño utiliza una convención útil: cada función de validación o alta retorna una tupla con el estado de la operación, por ejemplo `[ok, datos, mensaje]` o una variante con más valores, y así permite que la interfaz muestre mensajes uniformes sin mezclar la lógica con la salida por consola.

### `main.py`

Este archivo es la capa de presentación y se encarga de:

- mostrar los menús por consola;
- pedir entradas de usuario;
- mostrar mensajes con colores para información, error y éxito;
- recibir resultados de `operaciones.py` y presentarlos correctamente;
- permitir el flujo principal con dos perfiles: administrador y vendedor.

La función `main()` arranca el sistema a partir de `datos.creaciondatos()` y luego entrega el control a dos menús principales:

1. `menu_administrador()` — gestiona vendedores, productos, ventas y reportes.
2. `menu_vendedor()` — valida el código del vendedor y permite registrar ventas y consultar indicadores propios.

## 3. Modelo de datos

El proyecto usa una representación simple basada en listas paralelas y dos matrices:

- `vendedores_id`, `vendedores_nombre`, `vendedores_comision` están sincronizados con las filas o columnas de la matriz de ventas de vendedores.
- `productos_id`, `productos_nombre`, `productos_precio` están sincronizados con las filas o columnas de la matriz de productos.
- `matriz_vendedores` guarda el importe acumulado por vendedor y mes.
- `matriz_productos` guarda la cantidad de unidades vendidas por producto y mes.
- `meses_registrados` indica qué meses ya recibieron al menos una venta.

Esta manera de representar los datos es suficiente para un proyecto académico y refleja la idea de separar estructura de datos de operación y cálculo.

## 4. Flujo principal de ejecución

Cuando se ejecuta `main.py`, el flujo es:

1. Cargar los datos base con `datos.creaciondatos()`.
2. Crear la lista `meses_registrados` con `False` para cada mes.
3. Mostrar el menú principal:
   - Administrador
   - Vendedor
   - Salir
4. Dependiendo de la opción elegida:
   - El administrador accede a gestión de vendedores, productos, ventas y reportes.
   - El vendedor ingresa su código y puede registrar ventas y consultar su importe, comisión y proyección.

## 5. Reglas de validación

Las validaciones se centralizan en `operaciones.py` y hacen referencia a:

- código entero válido y mayor a cero;
- texto no vacío;
- nombre y código no duplicado;
- rango de comisión entre 0 y 100;
- precio válido y positivo;
- cantidad de unidades mayor a cero;
- mes entre 1 y 12;
- existencia de vendedor y producto antes de registrar una venta.

La lógica evita el uso de manejo de excepciones como mecanismo principal para controlar errores, porque la entrega pedía resolver validaciones de forma estructurada y directa.

## 6. Reglas de cálculo

El sistema usa las matrices para producir reportes de negocio. Algunos cálculos importantes son:

- total anual de ventas por vendedor o producto;
- comisión de cada vendedor según el porcentaje y el importe acumulado;
- promedio mensual y proyección anual de cada vendedor;
- producto más vendido por cantidad de unidades;
- vendedor con mayor volumen de ventas por importe acumulado;
- mes con mayor cantidad de unidades registradas;
- ranking y top 3 de vendedores;
- cumplimiento del objetivo mensual comparando ventas por vendedor y mes.

## 7. Interfaz y experiencia de consola

El archivo `main.py` implementa una interfaz textual con:

- mensajes de error en rojo;
- mensajes de éxito en verde;
- mensajes informativos en azul;
- menú de opciones y matrices legibles por consola.

Estos elementos permiten que el usuario comprenda rápidamente la diferencia entre una operación rechazada, una operación aceptada y una consulta de información.

## 8. Observaciones de diseño

La solución aprovecha una arquitectura simple de tres capas:

- `datos.py` aporta la semilla de información;
- `operaciones.py` contiene la lógica y los cálculos;
- `main.py` orquesta la interacción humano-sistema.

Esto es una buena base para explicar la esencia del proyecto en una defensa oral: el alumno puede demostrar que entiende la diferencia entre datos, validaciones y flujo de interacción. También se puede discutir cómo el proyecto podría ampliarse en una segunda versión con clases, persistencia en archivos o base de datos y una interfaz más robusta.

## 9. Cómo explicar el proyecto en la defensa oral

Durante la defensa, conviene responder con una estructura clara:

1. ¿Qué problema resuelve la aplicación?
2. ¿Qué hace `datos.py`?
3. ¿Qué hace `operaciones.py`?
4. ¿Qué hace `main.py`?
5. ¿Cómo se registra una venta?
6. ¿Cómo se calculan los reportes?
7. ¿Qué validaciones protegen la integridad del sistema?

## 10. Conclusión

BlueSquad SalesMatrix es una entrega educativa que combina manejo de listas paralelas, matrices, validaciones y reportes de ventas en una sola aplicación de consola. La versión actual de los archivos `main.py`, `operaciones.py` y `datos.py` refleja un diseño lineal, claro y manejable para una defensa oral de programación inicial.

