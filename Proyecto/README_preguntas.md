# Preguntas sobre BlueSquad SalesMatrix

Este archivo reúne preguntas que podrían formularse sobre la lógica y la estructura del proyecto BlueSquad SalesMatrix.

## Preguntas de análisis del código

1. ¿Qué diferencia hay entre la capa de interfaz del archivo `main.py` y la capa lógica de `operaciones.py`?
2. ¿Por qué el proyecto usa listas paralelas para vendedores y productos en lugar de una sola estructura de diccionario o una clase?
3. ¿Cómo se sincronizan las listas paralelas y las matrices al agregar o eliminar un vendedor o un producto?
4. ¿Qué sucede cuando el usuario intenta registrar una venta con un vendedor o producto inexistente?
5. ¿Qué validaciones se aplican al registrar una venta?
6. ¿Qué relación existe entre `meses_registrados` y los cálculos de promedio y proyección?
7. ¿Cómo se determina el producto más vendido y qué pasa si hay un empate?
8. ¿Cómo se determina el vendedor con mayor volumen y qué pasa si hay un empate?
9. ¿Qué es un ranking de vendedores y cómo se ordena?
10. ¿Qué significa el cumplimiento del objetivo mensual y cómo se calcula?

## Preguntas de flujo de ejecución

11. ¿Qué acciones se pueden hacer desde el menú de administrador?
12. ¿Qué acciones se pueden hacer desde el menú de vendedor?
13. ¿Cómo se garantiza que un vendedor solo pueda registrar ventas para su propio código?
14. ¿Qué pasa si un vendedor ingresado en el menú no existe?
15. ¿Qué información se necesita para registrar una venta?

## Preguntas de mantenimiento y modularización

16. ¿Se podría reemplazar la lógica de validación repetida por una función general de validación?
17. ¿Qué ventajas tiene separar `datos.py`, `operaciones.py` y `main.py`?
18. ¿Qué módulo es el más apropiado para extraer futuras funciones si el proyecto crece?
19. ¿Qué problema podría aparecer si las listas paralelas y las matrices dejan de mantenerse sincronizadas?
20. ¿Qué mejora haría más legible a la solución si el proyecto creciera en cantidad de informes?

## Preguntas de comprensión de informes

21. ¿Qué diferencia existe entre el total anual de la empresa y el promedio mensual?
22. ¿Cómo se calcula la proyección anual estimada?
23. ¿Qué significa que una matriz de productos almacene unidades y una matriz de vendedores almacene importes?
24. ¿Qué información representa el mes de mayor facturación en el sistema?
25. ¿Cuáles son los datos mínimos necesarios para producir un informe de cumplimiento del objetivo?
