# Orientador 5 - Ruptura de ciclos y manejo de excepciones

Este orientador trabaja con los conceptos de:

- finalización anticipada de ciclos con `break`
- ciclos controlados con `while True`
- manejo de excepciones con `try`, `except`, `else`, `finally`
- uso de `raise` para rechazar datos inválidos
- control interno con `assert`
- desafío integrador de carga segura de productos

## Estructura de la carpeta

La carpeta está organizada de la siguiente forma:

- `breack.py` → archivo de ejemplo para introducir `break` y la ruptura anticipada de ciclo.
- `cicloWhile.py` → ejercicio con `while True` para solicitar valores y finalizar con una condición interna.
- `try-except.py` → ejemplos de `try-except` y manejo de excepciones específicas.
- `productos_modulo.py` → módulo con funciones para calcular importe, cargar productos y mostrar estadísticas.
- `main_carga_segura.py` → archivo principal del desafío integrador.
- `validacion_producto.py` → archivo de prueba para verificar los casos del ejercicio 10.

## Temario

### 1. Finalización anticipada de un ciclo con `break`

Se usa `break` para salir del ciclo más cercano cuando se encuentra una condición de corte.

### 2. Ciclos controlados con `while True`

Se usa `while True` cuando la condición de salida no se conoce de antemano y se controla con una validación dentro del bloque. La finalización debe producirse con `break`.

### 3. Concepto de excepción

Las excepciones son errores detectados en tiempo de ejecución. Si no se capturan, la ejecución se interrumpe y se ve un traceback.

### 4. Captura con `try-except`

El bloque `try` contiene las instrucciones que pueden producir un error, y cada `except` captura una excepción específica.

### 5. Múltiples excepciones y reglas del problema

Se practican `ValueError` e `IndexError` para distintos errores de ingreso y validación.

### 6. Cláusulas `else` y `finally`

Se usa `else` para ejecutar una acción solamente si el bloque `try` no falló, y `finally` para ejecutar un cierre o mensaje de finalización siempre.

### 7. Provocar una excepción con `raise`

`raise` se usa para informar que los datos ingresados no cumplen la regla del problema, incluso si el tipo es correcto.

### 8. Comprobaciones internas con `assert`

`assert` verifica una condición que el programador espera que sea verdadera. Si es falsa, aparece `AssertionError`.

### 9. Desafío integrador: carga segura de productos

El sistema registra productos en una lista, donde cada producto se guarda como una lista con:

- código
- descripción
- cantidad
- precio
- importe

La carga termina cuando el código ingresado es `FIN`.

Reglas del problema:

- usar `while True` y `break`
- capturar `ValueError` al convertir cantidad y precio
- usar `raise ValueError` cuando cantidad o precio sean menores o iguales a cero
- no incorporar producto cuando los datos sean inválidos
- calcular el importe mediante una función
- usar `assert` solo como comprobación interna del cálculo
- controlar el caso de lista vacía para evitar división por cero

### 10. Verificación y análisis

Se prueban los siguientes casos:

1. Finalización inmediata con `FIN`
2. Producto válido
3. Cantidad escrita con letras
4. Precio igual a cero
5. Varios productos válidos antes de `FIN`
6. Aserción fallida intencional

## Ejecución del desafío integrador

Se puede ejecutar desde el archivo principal:

```python
from productos_modulo import cargar_productos, informar_totales

productos = cargar_productos()
informar_totales(productos)
```

O directamente con:

```python
python main_carga_segura.py
```

## Observaciones

El trabajo está organizado de manera modular para separar:

- la lógica de cálculo
- la carga del catálogo
- la presentación de estadísticas

Esto permite reutilizar el módulo `productos_modulo.py` en otros programas de práctica.
