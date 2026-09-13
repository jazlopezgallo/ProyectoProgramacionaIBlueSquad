# Preguntas guía para BlueSquad SalesMatrix

Este archivo propone preguntas de análisis y comprensión sobre el proyecto BlueSquad SalesMatrix. El objetivo es estudiar la estructura, el flujo de ejecución y las decisiones de programación que aparecen en la solución.

## 1. Preguntas de análisis del proyecto

1. ¿Qué problema resuelve la aplicación BlueSquad SalesMatrix?
2. ¿Qué rol cumple el archivo de datos y cuál es su importancia en la ejecución del programa?
3. ¿Qué diferencia hay entre la capa de presentación y la capa de lógica del negocio?
4. ¿Por qué el proyecto usa listas paralelas para vendedores y productos?
5. ¿Cuál es el vínculo entre las listas paralelas y las matrices de ventas?

## 2. Preguntas sobre validaciones

6. ¿Qué validaciones realizan las funciones de alta y baja en el sistema?
7. ¿Qué ocurre si el usuario intenta agregar un producto con un nombre vacío?
8. ¿Qué pasa si el usuario intenta registrar una venta con un código de vendedor o producto que no existe?
9. ¿Por qué la cantidad de unidades vendidas debe ser mayor que cero?
10. ¿Qué se valida al revisar el mes de la venta?

## 3. Preguntas sobre el flujo de administración

11. ¿Qué opciones ofrece el menú de administrador?
12. ¿Cuál es la diferencia entre gestionar vendedores y gestionar productos?
13. ¿Cómo se implementa la búsqueda dentro del flujo de administración?
14. ¿Qué indica el menú de consultar matrices en la práctica?
15. ¿Qué es el propósito del registro de venta desde el perfil de administrador?

## 4. Preguntas sobre el flujo de vendedor

16. ¿Qué información pide el menú del vendedor para entrar al sistema?
17. ¿Qué diferencia existe entre registrar una venta desde el vendedor y el administrador?
18. ¿Qué significa que el vendedor ingrese con un código fijo y no necesite elegir el vendedor en la venta?
19. ¿Cómo se consultan el importe total vendido y la comisión de un vendedor?
20. ¿Qué se entiende por proyección estimada anual del vendedor?

## 5. Preguntas sobre informes y reportes

21. ¿Qué función cumple cada una de las consultas principales del sistema?
22. ¿Cómo se define el producto más vendido mediante las matrices?
23. ¿Cómo se determina el vendedor con mayor volumen de ventas?
24. ¿Qué relación existe entre la matriz de productos y el mes con mayor cantidad de unidades?
25. ¿Qué se calcula al hacer el ranking y el top 3 de vendedores?
26. ¿Qué significa cumplir el objetivo mensual y cómo se compara con el registro del mes?

## 6. Preguntas de mantenimiento y modularización

27. ¿Qué ventajas tiene tener los datos iniciales en un archivo separado?
28. ¿Qué ventajas tiene separar la lógica de la interfaz en archivos distintos?
29. ¿Qué pasaría si la matriz de vendedores o los identificadores no permanecieran sincronizados?
30. ¿Por qué es importante que un módulo de operaciones reciba entradas y devuelva resultados, sin imprimir mensajes por sí mismo?

## 7. Preguntas de reflexión

31. ¿Cómo se podría mejorar la solución para hacerla más escalable sin perder claridad?
32. ¿Qué funciones de la entrega representan una buena separación entre interfaz y lógica?
33. ¿Qué criterio usarían para definir si una operación debe ir en `main_corregido.py` o en `operaciones_corregido.py`?
34. ¿Qué relación tiene el objetivo mensual con la idea de cumplimiento de ventas?
35. ¿Qué muestra el sistema cuando una operación tiene éxito y qué muestra cuando se equivoca el usuario?
