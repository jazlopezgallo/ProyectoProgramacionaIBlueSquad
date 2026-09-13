# Preguntas guía para BlueSquad SalesMatrix

Este archivo sirve como preparación para defender oralmente el proyecto BlueSquad SalesMatrix. Está pensado para que el estudiante no solo recuerde qué funciones existen, sino que pueda explicar, con claridad y orden, cómo se relacionan los archivos `datos.py`, `operaciones.py` y `main.py`, cómo se validan las entradas y cómo se construyen los reportes del negocio.

## 1. Preguntas de análisis del proyecto

1. ¿Qué problema resuelve BlueSquad SalesMatrix y para qué tipo de empresa está pensado?
2. ¿Cuál es el papel de `datos.py` dentro de la ejecución del programa?
3. ¿Qué función cumple `operaciones.py` y qué diferencia tiene con `main.py`?
4. ¿Por qué el proyecto usa listas paralelas para vendedores y productos?
5. ¿Qué relación existe entre las listas paralelas y las matrices de ventas?
6. ¿Cómo se representa el estado inicial del sistema al empezar la ejecución?

## 2. Preguntas sobre validaciones

7. ¿Qué validaciones se realizan al agregar un vendedor?
8. ¿Qué validaciones se realizan al agregar un producto?
9. ¿Qué ocurre si el usuario intenta dar de alta un vendedor con un código ya registrado?
10. ¿Qué ocurre si intenta crear un producto con nombre vacío?
11. ¿Qué pasa si el usuario intenta registrar una venta con un vendedor o producto inexistente?
12. ¿Por qué la cantidad de unidades vendidas debe ser mayor que cero?
13. ¿Qué se verifica al leer el mes ingresado en una venta?
14. ¿Qué relación existe entre las validaciones y la integridad de las matrices?

## 3. Preguntas sobre el flujo de administración

15. ¿Qué opciones ofrece el menú de administrador?
16. ¿Qué diferencia principal existe entre gestionar vendedores y gestionar productos?
17. ¿Cómo se implementa una búsqueda por código en el proyecto?
18. ¿Qué representa la opción de consultar matrices en la práctica?
19. ¿Qué se logra cuando el administrador registra una venta?
20. ¿Cómo se usa la matriz de vendedores para comparar el rendimiento entre vendedores?

## 4. Preguntas sobre el flujo del vendedor

21. ¿Qué información debe ingresar el vendedor para entrar al sistema?
22. ¿Qué diferencia hay entre registrar una venta desde el perfil de administrador y hacerlo desde el perfil de vendedor?
23. ¿Por qué el vendedor no elige su código en la venta cuando ya fue ingresado al sistema?
24. ¿Cómo se consulta el importe total vendido por un vendedor?
25. ¿Cómo se calcula la comisión de un vendedor?
26. ¿Qué significa la proyección anual y cómo se estima en el proyecto?

## 5. Preguntas sobre informes y reportes

27. ¿Qué informa la consulta `producto_mas_vendido()`?
28. ¿Cómo se determina el vendedor con mayor volumen de ventas?
29. ¿Cómo se identifica el mes con mayor cantidad de unidades?
30. ¿Qué relación existe entre `matriz_productos` y la consulta del mes con mayor cantidad de unidades?
31. ¿Qué hace el ranking de vendedores y qué finalidad tiene el `top_3`?
32. ¿Qué significa cumplir el objetivo mensual y cómo se compara ese cumplimiento con el mes registrado?
33. ¿Qué diferencia hay entre cantidad vendida, importe vendido y objetivo mensual en el modelo del sistema?

## 6. Preguntas de diseño y modularización

34. ¿Qué ventajas tiene mantener los datos iniciales en `datos.py` separado del resto del programa?
35. ¿Qué ventajas tiene separar la lógica de negocio en `operaciones.py` de la interfaz en `main.py`?
36. ¿Qué pasaría si los identificadores y las matrices dejaran de estar sincronizados?
37. ¿Por qué `operaciones.py` debe recibir datos y devolver resultados, en lugar de imprimir mensajes directamente?
38. ¿Cómo explica la separación de responsabilidades el diseño del proyecto?

## 7. Preguntas de reflexión para defender oralmente

39. ¿Se podría hacer el proyecto más escalable usando clases, archivos persistentes o una base de datos?
40. ¿Qué funciones son claramente de interfaz y cuáles son claramente de lógica de negocio?
41. ¿Qué criterio usarían para decidir si una operación va en `main.py` o en `operaciones.py`?
42. ¿Qué relación hay entre el objetivo mensual y la idea de cumplimiento de ventas?
43. ¿Qué mensaje muestra el sistema cuando la operación es exitosa y qué mensaje cuando falla?
44. ¿Qué parte del proyecto más les resultó importante y por qué?
45. ¿Qué aprendizaje te llevás de haber separado datos, funciones y salida por consola?
46. ¿Cómo podría explicar el proyecto a una persona que no sabe de programación?

## 8. Preguntas de presentación oral recomendadas

47. ¿Cómo se inicia el programa y qué menú aparece primero?
48. ¿Qué usaría para demostrar la lógica del registro de una venta?
49. ¿Cómo se relaciona una venta con la actualización de dos matrices distintas?
50. ¿Qué información se toma de `datos.py` para construir la marcha inicial del sistema?

## 9. Resumen para la defensa

En la defensa oral es útil hablar en este orden:

1. Explicar el problema y el objetivo del sistema.
2. Describir la organización en `datos.py`, `operaciones.py` y `main.py`.
3. Mostrar cómo se registra una venta y cómo eso afecta las matrices.
4. Explicar una validación importante y su propósito.
5. Explicar al menos un reporte: producto más vendido, vendedor con mayor volumen, ranking o cumplimiento del objetivo.
6. Señalar una mejora posible del proyecto para la siguiente versión.

La fórmula más segura para responder oralmente es: “El archivo `datos.py` arma el estado inicial, `operaciones.py` aplica la lógica y `main.py` presenta los resultados al usuario.”
