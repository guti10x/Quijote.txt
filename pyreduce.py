#!/usr/bin/env python2

import sys

current_word = None
contador = 0

# Leer líneas
for line in sys.stdin:
    # Quitar espacios en blanco y saltos de línea
    line = line.strip()
    # Dividir la línea en palabra 
    word, count = line.split("\t")
    count = int(count)
    
    # Aumentamos el contador si se repite la palabra
    if current_word == word:
        contador = count
    else:
        if current_word:
            # Emitir la palabra y contador asociado
            print(f"{current_word}\t{current_count}")
        current_word = word
        contador = count

# Emitir la última palabra si corresponde
if current_word:
    print(f"{current_word}\t{current_count}")