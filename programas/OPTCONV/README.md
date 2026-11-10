# OPTCONV — HP Prime, Temas 1 y 2

Programa para la HP Prime que resuelve con pasos los ejercicios de:

- **Tema 1**: PL de 2 variables por el método gráfico (vértices, óptimo, no acotado, óptimos múltiples) y análisis de sensibilidad.
- **Tema 2**: forma estándar `Ax=b, x>=0`, soluciones básicas, puntos y direcciones extremas, representación de un punto, Carathéodory, envolvente convexa, semiespacios, proyección, hiperplano separador y soporte, convexidad (Hessiano).

Usa las mismas convenciones de datos que `OPTILIN`.

## 1. Instalar en la calculadora (HP Connectivity Kit)

1. Conecta la HP Prime encendida y abre **HP Connectivity Kit**.
2. En el panel **Calculadoras**, despliega tu HP Prime → clic derecho en **Programas** → **Nuevo** → nombre `OPTCONV`.
3. En el editor que se abre: `Cmd+A`, pega el contenido de `OPTCONV.hpprgm` con `Cmd+V` y guarda con `Cmd+S`.
   - Si el Kit marca un error de sintaxis, apunta la línea y el mensaje y pásamelo.
4. En la calculadora: `Shift` + `1` (Program) → `OPTCONV` → **Run**, o escribe `OPTCONV` (sin paréntesis) en Home y pulsa Enter.

Las funciones CAS (`CVHESS`, `CVOPT2`, `CVPROY`, `CVSOP`) se usan desde la **vista CAS**, escribiéndolas como cualquier comando. Escriben los pasos en el Terminal y, al cerrarlo (Esc), dejan el resultado en la historia del CAS.

## 2. Datos (variables globales, se conservan entre ejecuciones)

| Variable | Qué es | Ejemplo |
|---|---|---|
| `CVDatos` | Matriz, una fila por restricción: `[a1, …, an, b, rel]`, con `rel`: `-1` ≤, `0` =, `1` ≥ | `[[0.4,0.5,20,-1],[0.1,0.25,5,-1]]` |
| `CVCoste` | Lista de coeficientes del objetivo | `{40,30}` |
| `CVTipo` | Signo de cada variable: `1` ≥0, `0` libre, `-1` ≤0 | `{1,1}` |
| `CVSentido` | `1` máx., `-1` mín. | `1` |
| `CVPuntos` | Matriz, un punto por fila (conjunto A) | `[[-1,2],[1,1],[1,-1]]` |
| `CVLambda` | Pesos de la combinación (Carathéodory) | `{0.2,0.2,0.2}` |
| `CVX` | Punto a estudiar (pertenencia, proyección, representación, soporte) | `{4,4}` |
| `CVDirs` | Direcciones, una por fila (las filas de ceros se ignoran) | `[[1,2],[0,1]]` |

Se editan con las opciones 1 y 14 del menú, o desde Home (p. ej. `CVX:={1,1}`).

## 3. Menú y para qué ejercicio sirve cada opción

| Opción | Qué hace | Ejercicios |
|---|---|---|
| 1 | Editar el modelo PL | — |
| 2 | **PL 2D**: cortes de todas las rectas (factible o qué restricción viola), vértices con z, direcciones de recesión, decisión (óptimo único, múltiple o no acotado) y holguras | T1: 3, 9, 11, 14, 15, 16 |
| 3 | **Sensibilidad**: aristas desde el óptimo, rango de c1 y c2, precio sombra y rango de cada b, coste reducido de x≥0 activa | T1: 3c, 11c, 14c, 15, 16b |
| 4 | Dibuja la región (puntos azules), las rectas, la recta de nivel óptima (verde) y el óptimo (rojo) | comprobar el dibujo |
| 5 | **Forma estándar**: cambios de variable (x=x⁺−x⁻, x=−x′), holguras s⁺ y excesos s⁻, sistema y matriz A | T2: 5, 6.2, ejemplo 8 |
| 6 | **Todas las matrices B**: det, B⁻¹b, factible o no, punto extremo, B⁻¹, direcciones extremas (B⁻¹a_j ≤ 0) | T2: 6.3–6.5, ejemplo 9 |
| 7 | Escribir `CVX` = Σλᵢvᵢ + Σμⱼdⱼ (usa lo calculado en 6 o `CVPuntos`/`CVDirs`) | T2: 6.6 |
| 8 | **Carathéodory** paso a paso (aᵢ−a₁, μ, α, λ nuevos, punto que sale) | T2: 3.1b, 3.3b |
| 9 | ¿`CVX` ∈ conv(A)? Si sí, da la combinación convexa | T2: 3.1a, 3.2, 3.3a, 3.4 |
| 10 | Puntos extremos de conv(A) | T2: 2.9, 3 |
| 11 | Semiespacio a partir de dos puntos de la frontera y un punto interior (`n·x ≤ b`) | T2: 1.4, 6.1, 8.1 |
| 12 | Proyección de `CVX` sobre el poliedro de `CVDatos` e hiperplano separador `n = x0 − c*` | T2: proyección en poliedros |
| 13 | Hiperplano soporte del poliedro en `CVX` | T2: soporte en poliedros |
| 14 | Editar `CVPuntos`, `CVLambda`, `CVX`, `CVDirs` | — |

Las opciones 2, 3, 4, 12 y 13 necesitan 2 variables (`CVDatos` con 4 columnas). Las opciones 5 y 6 sirven para cualquier número de variables.

La salida se muestra en el Terminal; se recorre con las flechas ↑/↓.

## 4. Funciones CAS (vista CAS)

`v` es la lista de variables y `g` la lista de restricciones escritas como `g_k ≤ 0`.

```
CVHESS(f, v)        Hessiano, menores líderes, todos los menores principales,
                    autovalores y conclusión (si H es constante)
CVOPT2(f, g, v)     mín./máx. de f en {g ≤ 0} con 2 variables: candidatos interiores,
                    con una g activa (Lagrange, devuelve λ) y vértices g_i=g_j=0
CVPROY(x0, g, v)    proyección de x0 sobre {g ≤ 0}, distancia, n = x0 − proy, b = n·proy
CVSOP(c, g, v)      hiperplano soporte en c: n = ∇g_k(c) de cada g_k activa
```

Ejemplos de los ejercicios:

```
CVHESS(1/x^2+3*x^2-x+3,[x])                      T2 Ej 7.1
CVHESS(ln(x*y)+3*x-2*y+7,[x,y])                  T2 Ej 7.2
CVHESS(2*x^2+2*x*y-2*x*z+3*y^2-z^2,[x,y,z])      T2 Ej 7.3
CVHESS(x^4+y^2+z^4,[x,y,z])                      T2 Ej 7.4
CVHESS(e^(x^2-y),[x,y])                          T2 Ej 7.6
CVHESS(ln(3*y-x^2),[x,y])                        T2 Ej 7.7

g:=[2-x-y, x^2+y^2-4, x^2-y]                     conjunto F del T2 Ej 4
CVPROY([2,2],g,[x,y])                            T2 Ej 4.2 (igual para 4.3–4.6)
CVSOP([1,1],g,[x,y])                             T2 Ej 4.7 (igual para 4.8–4.10)

CVOPT2((x-3)^2+(y-2)^2,[x^2+y-6,x^2-y],[x,y])    T1 Ej 17
```

Si `CVOPT2`/`CVPROY` no encuentra candidatos (por ejemplo, con logaritmos que `solve` no resuelve), haz el cálculo a mano con los comandos de la sección 6.

## 5. Comprobación rápida tras instalar (resultados esperados)

Con los datos que trae por defecto (T1 Ej 11):

- **Opción 2**: `V1=(75/2, 5) z=1650`, óptimo único; R2 y R3 activas, R1 con holgura 5/2.
- **Opción 3**: `c1 en [12, 60]`, `c2 en [20, 100]`; R2: `y=50`, `b en [4, 20/3]`; R3: `y=175/3`, `b en [6, 30]`.
- **Opción 9** (`CVX={4,4}`): NO pertenece. **Opción 8**: queda `1/2·a2 + 3/10·a3 + 1/5·a5`.

Con el ejemplo 9 del T2 (`CVDatos:=[[1,1,2,1],[1,-1,1,-1],[2,-1,4,-1]]`, `CVTipo:={1,1}`):

- **Opción 6**: 10 matrices B; factibles las 1, 3 y 9 → puntos extremos (3,2), (3/2,1/2), (0,2); direcciones d=(1,2,3,1,0) → (1,2) y d=(0,1,1,1,1) → (0,1). Coincide con las soluciones del profesor.

En CAS:

- `CVHESS(2*x^2+2*x*y-2*x*z+3*y^2-z^2,[x,y,z])` → menores líderes 4, 20, −64 → INDEFINIDA.
- `CVHESS(ln(x*y)+3*x-2*y+7,[x,y])` → H=[[−1/x², 0],[0, −1/y²]], D1=−1/x², D2=1/(x²y²) → estrictamente cóncava en su dominio.
- `CVPROY([0,1],g,[x,y])` → proy (1/2, 3/2).
- T1 Ej 17 → mínimo ≈ (1.567, 2.457) con f ≈ 2.261, tangente a la parábola y=x².

## 6. Comandos CAS de la calculadora por si algo falla

```
hessian(f,[x,y])               matriz Hessiana
det(M)                         determinante (menores)
eigenvals(M)                   autovalores
solve([e1,e2],[x,y])           sistema de ecuaciones
diff(f,[x,y])                  gradiente
```

## 7. Avisos

- Los cálculos de la parte Home son numéricos; las fracciones son la representación más cercana (denominador ≤ 5000).
- En Carathéodory, otra elección de μ da otra combinación igualmente válida; el programa elige la variable libre de la RREF.
- En la sensibilidad, cada rango vale cambiando **un solo dato** cada vez. En vértices degenerados los precios sombra no son únicos y el programa lo avisa.
- Probado en el emulador HP Prime (opciones 2–10, 12 y las cuatro funciones CAS) con los ejercicios de los temas 1 y 2, y copiado a la calculadora XUL.
