# OPTILIN

Solver educativo de programación lineal continua, en HP PPL para Home. Conserva el modelo y permite recorrer el símplex de dos fases por pasos, además de mostrar el dual y sensibilidad respecto a un dato cada vez.

## Entrada

| Dato | Contrato |
|---|---|
| `PLDatos` | Matriz de `m` filas y `n+2` columnas: coeficientes de la restricción, término independiente y relación |
| Última columna | `-1`: menor o igual; `0`: igualdad; `1`: mayor o igual |
| `PLCoste` | Lista de `n` coeficientes del objetivo |
| `PLTipo` | Lista de `n` signos: `1` no negativa, `0` libre, `-1` no positiva |
| `PLSentido` | `1` máximo, `-1` mínimo |

Se requieren coeficientes numéricos reales y dimensiones compatibles. No resuelve restricciones enteras o binarias. La normalización usa variables no negativas, holguras, excesos y artificiales; las filas con término independiente negativo se multiplican por menos uno.

## Uso desde el catálogo de programas

1. Ejecuta `OPTILIN` y edita los datos en la opción 1.
2. La opción 2 escribe el dual del modelo original.
3. La opción 3 resuelve o recalcula y conserva el resultado en `PLRes`.
4. La opción 4 muestra la forma estándar.
5. La opción 5 permite primer paso, siguiente, anterior o ir a un paso. `PLPaso` recuerda la posición.
6. La opción 6 muestra solución, holguras, dual, complementariedad e intervalos individuales de sensibilidad.

Las consultas dejan su salida en el Terminal y terminan. Vuelve a ejecutar el programa para otra consulta. Recorre la salida con el dedo o las flechas y sal con `Esc`.

Si modificas directamente las variables globales desde Home, usa después la opción 3: las opciones de consulta pueden conservar un resultado anterior.

## Funciones exportadas

`PLSolve(data,cost,types,sense)` recibe el modelo con el formato anterior. Devuelve una lista cuyo primer elemento es el estado:

| Estado | Significado |
|---|---|
| `1` | Óptimo con comprobación numérica primal-dual |
| `-1` | Infactible: valor positivo al terminar la fase I |
| `-2` | Dirección de mejora ilimitada |
| `-3` | Límite de 300 pivotes por fase; no certifica óptimo |
| `-4` | Datos no válidos; el segundo elemento contiene el mensaje |
| `-5` | Fallo en las comprobaciones numéricas; no certifica óptimo |

Para estado `1`, los ocho elementos son:

1. Estado.
2. Modelo estándar: `{A,b,c_interno,base_inicial,artificiales,origen,signos,cambios_fila}`.
3. Índices de la base final.
4. Lista de pasos `{fase,base,entrante,fila_saliente,paso,metricas}`.
5. Métricas finales `{B_inversa,B_inversa_A,xB,costes_reducidos,pi_interna,z_interno}`.
6. Solución en variables originales.
7. Valor del objetivo original.
8. Multiplicadores duales en el modelo original.

El objetivo interno es siempre minimizar `-sentido*c*x`; la condición de optimalidad interna es coste reducido no negativo. La selección de pivotes sigue Bland. La fase `3` de una traza identifica la retirada de una artificial básica de valor cero.

`PLRangoB(resultado,fila)` devuelve `{delta_min,delta_max}` para modificar únicamente ese término independiente manteniendo la base óptima. `PLRangoC(resultado,variable,sentido)` hace lo mismo para un coste; el sentido debe coincidir con el del modelo resuelto. El valor absoluto `1E99` representa una cota infinita. Solo se interpretan estos rangos cuando el estado es `1`.

Las funciones usan aritmética numérica con tolerancias. Un error al invertir una matriz o un dato de tipo no previsto puede generar una excepción; el menú principal la captura. Las fracciones mostradas son representaciones de esos resultados numéricos, no una ejecución simbólica exacta.

## Ejemplo conservado

Máximo de `3*x1+2*x2`, con `x1+2*x2<=6`, `2*x1+x2<=8`, `-x1+x2<=1`, `x2<=2` y variables no negativas:

- Óptimo esperado: `(10/3,4/3)`, valor `38/3`.
- Dual esperado: `(1/3,4/3,0,0)`.
- Variaciones de los cuatro términos independientes: `[-2,1]`, `[-2,4]`, `[-3,+infinito]`, `[-2/3,+infinito]`.
- Variaciones de los dos costes: `[-2,1]`, `[-1/2,4]`.

Los intervalos son cambios respecto al dato actual, no los valores absolutos del dato. Cada rango modifica un solo componente; los extremos y la degeneración requieren interpretar la base y el lado del cambio. Véase el [estado de verificación](../../docs/VERIFICACION.md).
