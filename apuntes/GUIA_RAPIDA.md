# Guía rápida — programas de la HP Prime (Optimización Continua)

En la calculadora (XUL) hay tres programas:

| Programa | Para qué |
|---|---|
| `OPTCONV` | Temas 1 y 2: PL gráfica con sensibilidad, forma estándar, soluciones básicas, Carathéodory, envolventes, proyección e hiperplanos, convexidad (CAS) |
| `OPTILIN` | Temas 3 y 4: simplex paso a paso, dual y sensibilidad |
| `TEOREMAS` | Teoremas y resultados de los temas 1 y 2, paso a paso |

## Cómo se ejecutan

- En **Home**: escribe el nombre **sin paréntesis** (`OPTCONV`, `OPTILIN`, `TEOREMAS`, `T2CARATH`…) y pulsa `Enter`.
- O bien `Shift` + `1` (Program) → elige el programa → **Run**.
- Las funciones CAS de OPTCONV (`CVHESS`, `CVOPT2`, `CVPROY`, `CVSOP`) se escriben en la vista **CAS**.
- La salida de texto queda en el **Terminal**: se recorre deslizando el dedo por la pantalla (o con ↑/↓) y se sale con `Esc`.

## Formato de los datos (OPTCONV y OPTILIN)

- **Restricciones**: matriz, una fila por restricción `[a1, …, an, b, rel]`, con `rel` = `-1` (≤), `0` (=), `1` (≥).
- **Signo de las variables**: lista con `1` (≥ 0), `0` (libre), `-1` (≤ 0).
- **Sentido**: `1` máx., `-1` mín.

Ejemplo, máx 40x1 + 30x2 con 0.4x1 + 0.5x2 ≤ 20, 0.1x1 + 0.25x2 ≤ 5 y x ≥ 0:

```
datos  = [[0.4,0.5,20,-1],[0.1,0.25,5,-1]]
coste  = {40,30}
signos = {1,1}
```

## OPTCONV (temas 1 y 2)

Variables: `CVDatos`, `CVCoste`, `CVTipo`, `CVSentido` (modelo); `CVPuntos` (un punto por fila), `CVLambda`, `CVX` (punto a estudiar), `CVDirs` (direcciones).

| Opción | Hace | Ejercicios |
|---|---|---|
| 1 | Editar el modelo PL | — |
| 2 | Cortes de rectas, vértices con z, decisión (único / múltiple / no acotado), holguras | T1: 3, 9, 11, 14, 16 |
| 3 | Sensibilidad: rangos de c1 y c2, precios sombra y rangos de b | T1: 3c, 11c, 14c, 16b |
| 4 | Dibujo de la región (cualquier tecla para salir) | — |
| 5 | Forma estándar `Ax=b, x≥0` (x⁺−x⁻, −x′, s⁺, s⁻) | T2: 5 |
| 6 | Todas las matrices B, B⁻¹b, puntos y direcciones extremas | T2: 6 |
| 7 | `CVX` = Σλᵢvᵢ + Σμⱼdⱼ | T2: 6.6 |
| 8 | Carathéodory paso a paso | T2: 3.1b, 3.3b |
| 9 | ¿`CVX` ∈ conv(A)? | T2: 3 |
| 10 | Puntos extremos de conv(A) | T2: 2.9, 3 |
| 11 | Semiespacio por dos puntos + punto interior | T2: 1.4, 6.1, 8.1 |
| 12 | Proyección de `CVX` sobre el poliedro + hiperplano separador | T2 |
| 13 | Hiperplano soporte del poliedro en `CVX` | T2 |
| 14 | Editar `CVPuntos`, `CVLambda`, `CVX`, `CVDirs` | — |

Las opciones 2, 3, 4, 12 y 13 son para 2 variables; las 5 y 6 sirven para cualquier número.

Funciones CAS (`g` = lista de restricciones `g ≤ 0`, `v` = variables):

```
CVHESS(f,[x,y])          Hessiano, menores, autovalores, convexidad   (T2 Ej 7)
CVOPT2(f,g,[x,y])        mín./máx. de f en {g ≤ 0}                    (T1 Ej 17, T2 Ej 8)
CVPROY([x0,y0],g,[x,y])  proyección y separador                       (T2 Ej 4.2–4.6)
CVSOP([c1,c2],g,[x,y])   hiperplano soporte                           (T2 Ej 4.7–4.10)
```

Ejemplo T2 Ej 4: `CVPROY([0,1],[2-x-y,x^2+y^2-4,x^2-y],[x,y])` → proyección (1/2, 3/2).

## OPTILIN (temas 3 y 4)

Variables: `PLDatos`, `PLCoste`, `PLTipo`, `PLSentido` (mismo formato de arriba).

| Opción | Hace |
|---|---|
| 1 | Editar o crear el modelo |
| 2 | Dual del problema original |
| 3 | Resolver / recalcular, y mostrar solución y sensibilidad |
| 4 | Forma estándar (con artificiales; filas con b < 0 se multiplican por −1) |
| 5 | Pasos del simplex, de uno en uno: B⁻¹, B⁻¹A, xB, π, costes reducidos, variable que entra (Bland), cocientes, variable que sale |
| 6 | Solución y sensibilidad: x, z, holguras, precios sombra y, complementariedad, rangos de Δb y Δc, valor dual |
| 7 | Salir |

Cada opción muestra su resultado en el Terminal y **termina el programa**; para otra consulta vuelve a ejecutar `OPTILIN`. El modelo resuelto se guarda, así que 4, 5 y 6 no recalculan (solo 3 lo hace).

Pasos del simplex (opción 5): sale un submenú con **Primer paso**, **Siguiente (paso k)**, **Anterior** e **Ir al paso…**. Recuerda en qué paso ibas, así que para avanzar basta con `OPTILIN` → 5 → Enter.

Ejemplo que trae cargado (máx 3x1 + 2x2): óptimo x1 = 10/3, x2 = 4/3, z = 38/3.

## TEOREMAS (temas 1 y 2)

Cada función abre una **pantalla en blanco**. Pulsa **`1`** para mostrar el siguiente paso; **cualquier otra tecla** cierra. Al llegar al último paso aparece `fin` abajo a la derecha. `TEOREMAS` abre un índice para elegir.

| Función | Contenido |
|---|---|
| `T1OPTIMO` | Solución factible, óptimo local y global |
| `T1MODELO` | Etapas y elementos de la modelización |
| `T1ABS` | Valor absoluto en objetivo, restricciones y variables |
| `T1BINAR` | Variables binarias: implicaciones, activación, big-M |
| `T1MAXMIN` | Maximin y minimax |
| `T1GRAF` | Resolución gráfica (continua, entera, no lineal) |
| `T1SENSIB` | Sensibilidad gráfica (c y b) |
| `T2CONVEX` | Conjuntos afines y convexos y sus propiedades |
| `T2EXTREM` | Puntos extremos, direcciones y direcciones extremas |
| `T2HIPER` | Hiperplanos y semiespacios |
| `T2ENVOLT` | Combinaciones, envolturas, politopo, símplice |
| `T2CARATH` | Teorema de Carathéodory + demostración |
| `T2PROYEC` | Teorema de proyección + demostración y propiedades |
| `T2SEPARA` | Hiperplano separador + demostración y corolario |
| `T2SOPORT` | Hiperplano soporte |
| `T2FARKAS` | Lema de Farkas + demostración |
| `T2GORDAN` | Lema de Gordan |
| `T2POLIED` | Conjuntos poliédricos, holguras, soluciones básicas |
| `T2PEXTPO` | Puntos extremos de un poliedro (caracterización, número, existencia) |
| `T2DEXTPO` | Direcciones extremas de un poliedro |
| `T2REPRES` | Teorema de representación |
| `T2FCONV` | Funciones convexas y cóncavas y sus propiedades |
| `T2EPIGRA` | Epígrafo e hipógrafo |
| `T2ANALIT` | Caracterizaciones analíticas (gradiente, hessiana) |
| `T2SYLVES` | Criterio de Sylvester |
| `T2OPTGLO` | Optimalidad global 1, 2 y 3 |
| `T2CONDOP` | Condiciones de optimalidad global (gradiente) |
| `T2OPTPOL` | Optimalidad en conjuntos poliédricos |

En `T1BINAR` se corrige una errata de los apuntes: yi = 1 ⇒ yj = 1 equivale a yj ≥ yi (no a yj ≥ 1 − yi).

## Si algo falla

- Si sale `Error: Syntax Error` al escribir un nombre en Home, escríbelo sin paréntesis.
- Las fracciones que muestran los programas son aproximaciones de cálculos numéricos.
- En sensibilidad, cada rango vale cambiando **un solo dato** cada vez.
