#!/usr/bin/env python3

import sys

# Leer líneas desde stdin
for line in sys.stdin:
    # Eliminar espacios en blanco y saltos de línea
    line = line.strip()
    # Dividir la línea en palabras
    words = line.split()
    # Emitir cada palabra con un valor de 1
    for word in words:
        print(f"{word}\t1")