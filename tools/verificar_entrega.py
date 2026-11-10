"""Comprueba integridad de la entrega; no ejecuta ni valida HP PPL."""

from hashlib import sha256
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def verificar_manifiesto():
    """Exige que cada entrada sea local y coincida con su SHA-256."""
    entradas = (ROOT / "MANIFEST.sha256").read_text(encoding="utf-8")
    nombres = set()

    for linea in entradas.splitlines():
        esperado, nombre = linea.split("  ", 1)
        ruta = ROOT / nombre

        if (
                nombre in nombres
                or ruta.is_symlink()
                or not ruta.resolve().is_relative_to(ROOT)
                ):
            raise ValueError(f"Entrada no válida: {nombre}")

        nombres.add(nombre)
        observado = sha256(ruta.read_bytes()).hexdigest()

        if observado != esperado:
            raise ValueError(f"Contenido diferente: {nombre}")

    if not nombres:
        raise ValueError("El manifiesto está vacío.")

    return nombres


def verificar_programas(nombres):
    """Detecta fuentes ausentes, codificación dañada o entradas perdidas."""
    for programa in ("OPTILIN", "OPTCONV", "TEOREMAS"):
        nombre = f"programas/{programa}/{programa}.hpprgm"

        if nombre not in nombres:
            raise ValueError(f"Programa fuera del manifiesto: {nombre}")

        fuente = (ROOT / nombre).read_text(encoding="utf-8")
        entrada = rf"\bEXPORT\s+{programa}\s*\(\s*\)"

        if "\ufffd" in fuente or not re.search(entrada, fuente):
            raise ValueError(f"Fuente incompleta o dañada: {nombre}")


def main():
    nombres = verificar_manifiesto()
    verificar_programas(nombres)
    print(f"Integridad correcta: {len(nombres)} archivos; 3 entradas HP PPL.")
    print("Esta comprobación no ejecuta el solver en la HP Prime.")


if __name__ == "__main__":
    main()
