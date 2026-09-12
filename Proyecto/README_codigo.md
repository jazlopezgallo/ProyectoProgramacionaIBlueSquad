# BlueSquad SalesMatrix — explicación del código

Este proyecto implementa una pequeña aplicación de consola para gestionar ventas, vendedores y productos de una empresa. La estructura del programa está separada en tres capas:

- [Proyecto/main.py](Proyecto/main.py): interactúa con el usuario mediante menús, inputs y prints.
- [Proyecto/operaciones.py](Proyecto/operaciones.py): contiene toda la lógica, validaciones, búsquedas, cálculos e informes.
- [Proyecto/datos.py](Proyecto/datos.py): guarda las constantes y los datos iniciales del sistema.

La idea central es mantener la interfaz gráfica o de texto separada de la lógica del negocio para que el código sea más legible y más fácil de mantener.

## 1. Estructura funcional

### datos.py

Este archivo define:

- `MESES`: tupla con los doce meses del año.
- `OBJETIVO_MENSUAL`: objetivo de ventas mensual por vendedor.
- `VENDEDORES_ID_INICIAL`, `VENDEDORES_NOMBRE_INICIAL` y `VENDEDORES_COMISION_INICIAL`: datos iniciales de vendedores.
- `PRODUCTOS_ID_INICIAL`, `PRODUCTOS_NOMBRE_INICIAL` y `PRODUCTOS_PRECIO_INICIAL`: datos iniciales de productos.

Este archivo solamente guarda valores de configuración y datos de arranque. No imprime ni pide información al usuario.

### operaciones.py

Este archivo contiene toda la lógica del sistema. Se encarga de:

- validar textos y enteros (`es_entero`, `texto_valido`);
- crear la matriz de ventas y el estado de meses (`crear_matriz`, `crear_meses_registrados`);
- buscar vendedores y productos (`buscar_vendedor`, `buscar_producto`);
- agregar y eliminar vendedores/productos (`agregar_vendedor`, `eliminar_vendedor`, `agregar_producto`, `eliminar_producto`);
- registrar ventas (`registrar_venta`);
- calcular informes y rankings (`total_anual_empresa`, `promedio_general_empresa`, `proyeccion_general`, `producto_mas_vendido`, `vendedor_mayor_volumen`, `mes_mayor_unidades`, `mes_mayor_facturacion`, `cumplimiento_objetivo_mes`, `ranking_vendedores`, `top_vendedores`).

La convención del archivo es clara: recibe datos por parámetros y devuelve resultados usando `return`, sin mezclar entrada/salida de consola.

### main.py

Este archivo es la capa de presentación. Tiene:

- funciones auxiliares de entrada (`pedir_entero`, `pedir_texto_no_vacio`, `mostrar_meses`);
- funciones para gestionar vendedores y productos (`gestionar_vendedores`, `gestionar_productos`);
- función para pedir los datos de una venta y registrarla (`pedir_datos_venta_y_registrar`);
- funciones de informes (`informe_general`, `informe_producto_mas_vendido`, `informe_vendedor_mayor_volumen`, `informe_mes_mayor_unidades`, `informe_ranking`, `informe_cumplimiento_objetivo`);
- menús de administrador y vendedor (`menu_administrador`, `menu_vendedor`);
- flujo principal de ejecución (`main`).

## 2. Cómo funciona el flujo principal

Cuando se ejecuta el programa, `main()` inicializa:

- listas paralelas para vendedores: IDs, nombres y comisiones;
- listas paralelas para productos: IDs, nombres y precios;
- matrices para registrar ventas por vendedor y unidades por producto;
- una lista de meses registrados para saber qué meses ya fueron usados.

Luego el usuario elige entre:

1. Administrador
2. Vendedor
3. Salir

Si elige administrador, puede:

- gestionar vendedores;
- gestionar productos;
- registrar una venta;
- consultar varias matrices e informes;
- revisar el ranking y objetivo del mes.

Si elige vendedor, se solicita el código de vendedor y luego puede:

- registrar su propia venta;
- consultar su total vendido;
- consultar su comisión;
- consultar su promedio mensual;
- consultar su mejor mes;
- consultar cumplimiento del objetivo;
- consultar su proyección anual.

## 3. Modelo de datos

El proyecto usa listas paralelas y matrices:

- Las listas paralelas sincronizan ID, nombre y comisión/precio.
- La matriz de vendedores tiene una fila por vendedor y 12 columnas, una por mes. Se guarda el importe vendido por cada mes.
- La matriz de productos tiene una fila por producto y 12 columnas para registrar unidades vendidas por mes.
- `meses_registrados` es una lista de booleanos donde cada posición representa un mes del año, indicando si ese mes ya fue procesado.

## 4. Validaciones implementadas

El sistema valida:

- Códigos positivos y no duplicados.
- Nombres no vacíos y no repetidos.
- Comisiones entre 1 y 100.
- Precios positivos.
- Cantidades positivas.
- Meses entre 1 y 12.
- Vendedores y productos existentes.

Las validaciones están resueltas con condiciones y retornos, en lugar de usar `try/except`.

## 5. Reglas de negocio

El sistema permite:

- registrar una venta solo si el vendedor y el producto existen;
- actualizar la matriz del vendedor con el importe total de la venta;
- actualizar la matriz del producto con la cantidad de unidades vendidas;
- marcar el mes como registrado en `meses_registrados`;
- emitir informes basados en los datos acumulados en las matrices.

## 6. Informes principales

El proyecto genera una variedad de informes:

- total anual de la empresa;
- promedio mensual y proyección anual;
- mes de mayor facturación;
- producto más vendido;
- vendedor con mayor volumen;
- mes con mayor cantidad de unidades;
- ranking de vendedores y top 3;
- cumplimiento del objetivo mensual.

## 7. Observación de modularización

La separación actual ya está bastante bien pensada:

- `datos.py` contiene solo datos constantes.
- `operaciones.py` contiene lógica reutilizable.
- `main.py` coordina la interfaz y la navegación.

Si se quisiera simplificar todavía más, el siguiente paso natural sería extraer los informes y validaciones de `main.py` a un módulo adicional, por ejemplo `informes.py` o `ui.py`, pero para este proyecto la división existente es suficiente y ordenada.
