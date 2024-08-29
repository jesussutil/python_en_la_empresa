import csv

nuevo_coche = ['tesla','model 3','','electricidad','06/06/2022','negro','39.538139','-119.4484472']

with open('coches.csv', 'a', newline='') as f:

    writer = csv.writer(f, delimiter=';')
    writer.writerow(nuevo_coche)
