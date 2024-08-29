with open(archivo_enorme.csv', 'rb') as file_in:
    with open("archivo_filtrado.csv", "wb") as file_out:  
        file_out.writelines(filter(lambda line: b'filtro' in line, file_in))
