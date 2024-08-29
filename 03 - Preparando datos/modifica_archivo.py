with open("archivo.csv") as f:       # abrimos el archivo
    for line in f:                   # iteramos línea a línea
        if line.endswith(';\n'):     ## condición sobre la línea a actuar
            line = line[:-2]         ## si se cumple la condición, actuamos
            print(line.rstrip())     # imprimimos la línea por pantalla
