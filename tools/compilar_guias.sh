#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

compilar() {
    nombre=$1
    destino="$repo_dir/.build/$nombre"
    mkdir -p "$destino"

    pdflatex \
        -interaction=nonstopmode \
        -halt-on-error \
        -output-directory="$destino" \
        "$repo_dir/apuntes/latex/$nombre.tex" \
        > "$destino/compilacion.txt"

    printf 'PDF generado: %s/%s.pdf\n' "$destino" "$nombre"
}

compilar guia_tema_2
compilar guia_T1_T2
