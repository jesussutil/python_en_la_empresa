import csv                                # importamos el módulo csv

with open('coches.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for row in csv_reader:
        if str(row[3]) == "gasolina":     # busco el tipo de combustible
            print (row)
