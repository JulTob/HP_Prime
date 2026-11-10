# Estado de verificación

Fecha de esta revisión: 10 de noviembre de 2026.

## Comprobaciones de conservación y documentos

- Los tres archivos HP PPL, la documentación previa y las dos guías recuperadas se compararon byte a byte con sus originales locales al copiarlos.
- La fuente conservada de temas 1 y 2 se recompiló con `pdflatex` sin errores: dos páginas A4 apaisadas. El PDF publicado en `apuntes/pdf/` conserva los bytes del original recuperado.
- El nuevo guíaburros del tema 2 se compiló a dos páginas A4 apaisadas, se comprobó su contenido extraído y se revisaron las dos páginas renderizadas.
- El manifiesto SHA-256 y `tools/verificar_entrega.py` permiten comprobar la integridad de los archivos seleccionados. Comprobar integridad no equivale a ejecutar el solver.
- El backup local de XUL se abrió como ZIP y pasó su comprobación de integridad. No se incorporó al repositorio ni se restauró sobre la calculadora.
- No se incluye una suite automática de ejecución de HP PPL ni un port a Python del solver.

## Ejecución registrada anteriormente

El registro de trabajo anterior describe estos resultados. Se recuperan como antecedentes; no se han repetido las sesiones del simulador ni la transferencia física durante esta revisión.

| Programa | Evidencia registrada |
|---|---|
| OPTILIN | Compilación y ejecución en el simulador; modelo de referencia con `x=(10/3,4/3)`, `z=38/3`; consultas de dual, forma estándar y pasos; corrección de salida al Terminal y del formato de fracciones; copia al programa existente de XUL |
| OPTCONV | Ejemplos de PL gráfica, sensibilidad, forma estándar, diez bases, Carathéodory, proyección y funciones CAS; copia a XUL |
| TEOREMAS | Índice y varios visores, incluidos Carathéodory, Farkas, proyección, optimalidad y Sylvester; copia a XUL |

La guía rápida y el README original de OPTCONV contienen los ejemplos y resultados esperados para repetir las comprobaciones. No existe aquí una transcripción completa ni evidencia de cobertura exhaustiva de todos los casos.

## Referencia analítica de OPTILIN

Para su modelo inicial, las dos restricciones activas son `x1+2*x2=6` y `2*x1+x2=8`. De ahí se obtiene `x=(10/3,4/3)` y `z=38/3`. El dual `y=(1/3,4/3,0,0)` cumple `A^T*y=c` y `b^T*y=38/3`.

Manteniendo esa base, los intervalos individuales esperados son:

| Cambio | Intervalo de variación |
|---|---|
| `Delta b1` | `[-2,1]` |
| `Delta b2` | `[-2,4]` |
| `Delta b3` | `[-3,+infinito]` |
| `Delta b4` | `[-2/3,+infinito]` |
| `Delta c1` | `[-2,1]` |
| `Delta c2` | `[-1/2,4]` |

Estos valores se deducen de la base del ejemplo. Documentarlos no constituye una nueva ejecución de `PLRangoB` o `PLRangoC` en la HP.

## Límites relevantes

- Home usa aritmética numérica; imprimir una fracción no convierte el algoritmo en aritmética exacta.
- Cada intervalo de sensibilidad modifica un solo dato; la degeneración puede producir varios multiplicadores y cambios de base en los extremos.
- Varias herramientas geométricas de OPTCONV se limitan a dos variables. Consulta la tabla de opciones de su README.
- Las comprobaciones de candidatos de los asistentes CAS dependen de que se hayan encontrado todos los casos pertinentes y de las hipótesis del problema.
- Este cierre conserva el código existente: no introduce una actualización de firmware, un nuevo backup de la HP ni una nueva instalación física.
