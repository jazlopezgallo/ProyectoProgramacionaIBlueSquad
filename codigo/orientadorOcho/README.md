# Orientador Ocho: Expresiones regulares

Este orientador practica la construcción de patrones con `re`, la búsqueda de coincidencias, la extracción de información y la validación completa de datos. Los patrones de las actividades son didácticos: una coincidencia de formato no demuestra que un dato exista o sea correcto en el mundo real.

## Archivos del orientador

### Ejemplos principales

| Archivo | Contenido |
| --- | --- |
| `metacaracteres.py` | Prueba `^`, `$`, `.`, clases y rangos, negación, alternativas, grupos, cuantificadores y escapes. |
| `patrones.py` | Reúne patrones para códigos, legajos, importes, palabras y fechas. |
| `full.py` | Compara `re.match()` con `re.fullmatch()` y muestra una búsqueda con `re.search()`, posiciones y `re.IGNORECASE`. |
| `findall.py` | Extrae números con `findall()`, recorre coincidencias con `finditer()` y muestra posiciones y grupos de captura. |
| `extraccion.py` | Encuentra correos, teléfonos y códigos en un texto, cuenta resultados e informa posiciones. |
| `sub-split-compile.py` | Demuestra reemplazo con `re.sub()`, separación con `re.split()` y reutilización de un patrón compilado. |
| `validaciones.py` | Contiene funciones de validación completas para legajo de cinco dígitos, código, teléfono, correo, importe y patente. |
| `pruebasDeValidaciones.py` | Ejecuta casos válidos e inválidos para las funciones del módulo `validaciones.py`. |

### Ejercicios de práctica

| Archivo | Contenido |
| --- | --- |
| `ejerciciosDePracticas/ejercicio_01_punto.py` | El punto como cualquier carácter individual. |
| `ejerciciosDePracticas/ejercicio_02_signo_interrogacion.py` | `?`: el elemento anterior aparece cero o una vez. |
| `ejerciciosDePracticas/ejercicio_03_asterisco.py` | `*`: el elemento anterior aparece cero o más veces. |
| `ejerciciosDePracticas/ejercicio_04_signo_mas.py` | `+`: el elemento anterior aparece una o más veces. |
| `ejerciciosDePracticas/ejercicio_05_inicio_fin.py` | Anclas `^` y `$` para buscar al comienzo o al final. |
| `ejerciciosDePracticas/ejercicio_06_montos.py` | Búsqueda de importes con `$` escapado y uno o más dígitos. |
| `ejerciciosDePracticas/ejercicio_07_fecha.py` | Búsqueda de una fecha con día, mes y año de dos dígitos. |
| `ejerciciosDePracticas/ejercicio_08_rango_anios.py` | Clases de caracteres para seleccionar un rango de años. |
| `ejerciciosDePracticas/ejercicio_09_alternativas.py` | Alternativas con `|` y agrupación no capturante. |
| `ejerciciosDePracticas/ejercicio_10_fullmatch.py` | Validación de una cadena completa con `re.fullmatch()`. |
| `ejerciciosDePracticas/ejercicio_11_para_resolver.py` | Consigna para extraer códigos de dos mayúsculas y tres dígitos. |
| `ejerciciosDePracticas/ejercicio_12_integrador.py` | Esqueleto para extraer código, correo, fecha e importe de un cliente. |
| `ejerciciosDePracticas/ejercicio_13_desafio_integrador.py` | Esqueleto para extraer varios tipos de datos de múltiples clientes. |
| `ejerciciosDePracticas/ejercicio_13_desafio_integrador copy.py` | Copia alternativa del esqueleto del ejercicio 13; contiene la misma consigna y estructura. |

### Actividad 9 resuelta

La actividad solicita nombre, legajo, correo, teléfono y código de comisión. El programa vuelve a pedir cada dato cuando su formato no es válido y permite registrar más de una persona.

| Archivo | Contenido |
| --- | --- |
| `actividad9/validaciones.py` | Funciones independientes basadas en `re.fullmatch()` para validar los cinco campos. Cada función informa el error correspondiente cuando el dato no cumple. |
| `actividad9/main.py` | Programa principal: solicita los datos, repite cada solicitud hasta validar y muestra el registro completo. También ofrece registrar más de una persona. |
| `actividad9/pruebas.py` | Ejecuta y muestra ejemplos válidos e inválidos para cada función del módulo `validaciones.py`. |

Para ejecutar los archivos, ubicarse en la carpeta `actividad9` y ejecutar:

```bash
python main.py
python pruebas.py
```

## Formatos definidos para el formulario

`main.py` solicita los campos en orden y vuelve a pedir cada uno hasta que su función de validación lo acepte. `validaciones.py` emplea `re.fullmatch()`, por lo que no permite texto adicional antes o después del patrón.

| Dato | Patrón | Interpretación y alcance | Válidos | Inválidos |
| --- | --- | --- | --- | --- |
| Nombre | `[A-Za-zÁ-Úá-úñÑ\s]{2,50}` | Entre 2 y 50 caracteres de letras contempladas por la clase y espacios. No acepta números. | `Ana Pérez`, `José Luis` | `A`, `Ana3` |
| Legajo | `[0-9]{5}` | Exactamente cinco dígitos; no valida asignación o existencia del legajo. | `12345`, `00015` | `1234`, `12A45` |
| Correo | `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}` | Usuario y dominio con los caracteres indicados, `@` y una extensión de al menos dos letras. Es una aproximación didáctica y no verifica que el correo exista. | `ana@mail.com`, `alumno.25@correo.org` | `anamail.com`, `ana@mail` |
| Teléfono | `[0-9]{4}-[0-9]{4}` | Cuatro dígitos, guion y cuatro dígitos. Valida la forma escrita, no que el número esté asignado. | `1234-5678`, `0001-2345` | `12345678`, `123-5678` |
| Comisión | `[A-Z]{3}[0-9]{4}` | Tres letras mayúsculas seguidas de cuatro dígitos. | `ABC1234`, `MAT0007` | `abc1234`, `AB1234` |

## Búsqueda parcial y validación completa

`re.search(patron, texto)` localiza una coincidencia en cualquier parte del texto. Por ejemplo, puede encontrar `4567` dentro de `Pedido 4567 listo`; no afirma que toda la frase sea un número. En cambio, `re.fullmatch(patron, dato)` solo acepta si todos los caracteres de `dato` cumplen el patrón. Por eso las validaciones del formulario usan `fullmatch()`.

`re.match()` verifica desde el comienzo, pero puede dejar caracteres sobrantes al final. `findall()` devuelve una lista de coincidencias; `finditer()` permite recorrer objetos de coincidencia con contenido y posiciones. `sub()` reemplaza coincidencias y `split()` divide el texto usando un patrón separador.

Los ejemplos de `match()`, `search()`, `fullmatch()`, `findall()`, `finditer()`, `sub()` y `split()` se encuentran en los archivos principales del orientador, como `full.py`, `findall.py` y `sub-split-compile.py`. La carpeta `actividad9` se concentra en el formulario y en las validaciones de sus campos.

## Reflexión individual

Las expresiones regulares permiten describir formatos de manera compacta y automatizar búsquedas, extracciones y validaciones. Pueden volverse difíciles de leer cuando combinan muchos grupos, alternativas y cuantificadores; además, validar solo la forma no garantiza que el dato tenga sentido o exista. Para mantenerlas, conviene usar nombres descriptivos, dividir reglas complejas, probar casos válidos e inválidos y documentar claramente sus límites.