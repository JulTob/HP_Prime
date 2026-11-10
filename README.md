# HP_Prime

Programas en HP PPL y apuntes de Optimización Continua para HP Prime.

## Empezar

- [Guía rápida de la calculadora](apuntes/GUIA_RAPIDA.md): instalación, datos y menús.
- [Guíaburros solo del tema 2](apuntes/pdf/guia_examen_tema_2.pdf): dos caras A4, por situaciones y pasos, sin demostraciones.
- [Guía conservada de temas 1 y 2](apuntes/pdf/guia_examen_T1_T2.pdf): versión anterior con enunciados de resultados; consulta las [precisiones](docs/CIERRE.md#precisiones-de-los-apuntes-conservados).
- [Resumen de cierre](docs/CIERRE.md): qué se guarda, qué se deja fuera y qué comprobaciones quedan disponibles.
- [Estado de verificación](docs/VERIFICACION.md): distingue las pruebas registradas en la Prime de las comprobaciones de esta entrega.

## Programas

| Programa | Uso | Fuente |
|---|---|---|
| OPTILIN | PL matricial, dos fases, pasos del símplex, dual y sensibilidad | [Código y contrato](programas/OPTILIN/README.md) |
| OPTCONV | PL gráfica 2D y herramientas de conjuntos y funciones convexas | [Código y documentación](programas/OPTCONV/README.md) |
| TEOREMAS | Visor de 28 resultados y sus pasos | [Código y uso](programas/TEOREMAS/README.md) |

Las fuentes `.hpprgm` de este repositorio son texto UTF-8 para pegar en el editor de HP Connectivity Kit. No son un backup completo de la calculadora.

Para instalar, crea o abre el programa con el mismo nombre en el Kit, pega la fuente y guarda. Actualizar el programa existente evita duplicados con sufijo `_1`. Ejecuta los programas Home desde el catálogo `Shift` + `1`; las funciones CAS de OPTCONV se usan en la vista CAS. Las instrucciones oficiales están en el [manual de HP Prime](https://h10032.www1.hp.com/ctg/Manual/c05332710.pdf), capítulo 28, y en la ayuda del Kit.

## Fuentes editables y conservación

Las guías tienen sus fuentes en [apuntes/latex](apuntes/latex). La primera guía general se conserva en [archivo_historico](archivo_historico/README.md). `randoms.hp` y `VARIABLES.HP` son ejemplos que ya existían en el repositorio y se mantienen sin cambios.

No se incluyen backups personales, PDF originales del profesor, instaladores, imágenes de diagnóstico ni archivos auxiliares de LaTeX.

## Verificar y recompilar

Python 3.9 o posterior, sin dependencias adicionales, para comprobar la integridad de esta entrega:

```sh
python3 tools/verificar_entrega.py
```

Con una distribución LaTeX que incluya `pdflatex`:

```sh
sh tools/compilar_guias.sh
```

La compilación escribe en `.build/`, ignorado por Git. La comprobación de integridad no ejecuta HP PPL ni certifica resultados matemáticos del solver.
