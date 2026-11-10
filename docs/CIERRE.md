# Cierre de los apuntes y programas de HP Prime

Revisión de conservación: 10 de noviembre de 2026.

## Qué queda guardado

| Material | Decisión |
|---|---|
| OPTILIN | Conservar la fuente actual completa y documentar entradas, salidas y limitaciones |
| OPTCONV | Conservar fuente y documentación actuales |
| TEOREMAS | Conservar el visor completo, incluido el material de demostraciones |
| Guía de temas 1 y 2 | Conservar PDF y fuente exactamente como estaban; leer las precisiones de abajo |
| Guíaburros solo del tema 2 | Añadir una versión independiente de dos caras con procedimientos y comprobaciones, sin demostraciones |
| Primera guía general | Conservar PDF y fuente como material histórico, separado de las versiones de estudio |
| Instrucciones de uso | Conservar la guía rápida y añadir documentación de instalación, integridad y compilación |
| `randoms.hp` y `VARIABLES.HP` | Mantener los ejemplos que ya estaban en el repositorio sin cambios |

Los tres programas se conservan sin alterar su comportamiento en este cierre. Están escritos en HP PPL; las funciones CAS de OPTCONV están incluidas en su misma fuente.

## Qué se puede dejar fuera

- Archivos `.aux`, `.log`, salidas `run*.txt` y copias de compilación: se regeneran desde LaTeX.
- Capturas, OCR y archivos temporales del diagnóstico: no son necesarios para usar los apuntes ni reinstalar los programas.
- Instaladores y volúmenes montados de HP: son herramientas del entorno, no material del repositorio.
- PDF originales del profesor: no se publican en este repositorio; se conservan en las carpetas originales del usuario.
- Backup completo de XUL: se conserva localmente y no se publica, porque puede contener otros datos de la calculadora.

No se han borrado los originales locales, los backups ni los temporales durante este cierre.

## Estado que permite cerrar la conversación

Las fuentes, los PDF y las instrucciones quedan disponibles sin depender del historial del chat. El registro previo de trabajo describe pruebas en el simulador y copia de los tres programas a XUL. La revisión de hoy comprueba los archivos locales y los apuntes; no vuelve a probar la calculadora física ni confirma su contenido actual. El detalle está en [VERIFICACION.md](VERIFICACION.md).

No se conserva una suite automatizada completa que permita afirmar cobertura de todos los casos del solver. Una ampliación futura debería empezar por añadir pruebas para infactibilidad, ilimitación, degeneración, variables libres, restricciones mixtas y sensibilidad. Esto no impide conservar y cerrar la entrega actual, pero sí limita lo que se puede afirmar sobre su verificación.

La petición de una guía separada del tema 2 queda atendida con `apuntes/pdf/guia_examen_tema_2.pdf`. La vista gráfica paramétrica integrada queda como posible ampliación, sin implementación acreditada en esta entrega. No es necesaria para usar el módulo matricial conservado.

## Precisiones de los apuntes conservados

La guía anterior de temas 1 y 2 se conserva sin cambios por trazabilidad. Al estudiar su parte de tema 2, aplica estas precisiones, ya reflejadas en el guíaburros independiente:

1. No poder aplicar un resultado por falta de hipótesis no demuestra que una afirmación sea falsa: hace falta un contraejemplo.
2. Comprobar un solo punto de un conjunto solo orienta un semiespacio; no certifica un separador para todo el conjunto. Usa la condición de proyección o una desigualdad válida globalmente.
3. Las fórmulas de bases suponen rango fila completo. La representación solo mediante puntos extremos y rayos necesita excluir rectas, como sucede en un poliedro no vacío en forma estándar con variables no negativas.
4. Una Hessiana semidefinida se estudia con todos los menores principales, no solo los líderes; hay que considerar el dominio convexo y distinguir convexidad de convexidad estricta.
5. Para obtener un soporte con el gradiente de una restricción activa, comprueba convexidad, diferenciabilidad y normal no nula.
6. Desdoblar variables libres no es una transformación inyectiva: un extremo del modelo ampliado no tiene por qué convertirse en extremo del conjunto original.

Estas precisiones no son una revisión exhaustiva del visor TEOREMAS ni de todos los ejemplos históricos. Al preparar un examen, el desarrollo escrito debe justificar las hipótesis y las comprobaciones del problema concreto.

## Retomar el trabajo

1. Leer el README y el estado de verificación.
2. Ejecutar `python3 tools/verificar_entrega.py` para comprobar que la instantánea no está dañada.
3. Para usar la calculadora, instalar las fuentes con Connectivity Kit y comprobar los ejemplos de referencia.
4. Para editar los apuntes, partir de `apuntes/latex/` y compilar en `.build/`.
