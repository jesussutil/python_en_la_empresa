import csv

with open('coches.csv', mode='a', newline='') as csv_file:
fieldnames = ['marca', 'modelo', 'cilindrada', 'combustible', 'ultima_posicion', 'color', 'latitud', 'longitud']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')

writer.writerow({'marca':'tesla', 'modelo':'model 3', 'combustible':'electricidad', 'ultima_posicion':'06/06/2022', 'color':'negro', 'latitud':'39.538139', 'longitud':'-119.4484472'})
