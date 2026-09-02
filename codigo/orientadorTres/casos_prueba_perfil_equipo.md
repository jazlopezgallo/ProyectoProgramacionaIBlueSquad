# 10. Verificación y análisis

Casos de prueba realizados para verificar el comportamiento del programa y de las operaciones trabajadas en la actividad.

| Caso | Entrada u operación | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| a) Nombre con varias palabras | `"Los Programadores"` | Sigla `"LP"` | `"LP"` |
| b) Nombre con letras y números | `"Equipo 2026"` | `contiene_digitos` = `True` | `True` |
| c) Datos numéricos válidos | Precio `1500.50`, cantidad `3` | Total `$4501.50` | `$4501.50` |
| d) Concatenar sin `str()` | `"Total: " + total` | Se produce `TypeError` | `TypeError: can only concatenate str (not "float") to str` |
| e) `find()` de texto inexistente | `texto.find("Java")` | `-1` | `-1` |

## Análisis del caso d)

Sin convertir el número con `str()`, Python no puede unir una cadena con un `float` usando `+`, porque son tipos distintos. Por eso lanza el error:

```text
TypeError: can only concatenate str (not "float") to str
```
