import csv

with open('coches.csv') as csv_file:
    csv_input = csv.DictReader(csv_file, delimiter=';')

    for row in csv_input:
        if row["combustible"] == "gasolina":
            print (row)

