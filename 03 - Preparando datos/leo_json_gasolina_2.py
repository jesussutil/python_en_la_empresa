import json

json_string = '[{"marca": "audi", "modelo": "a3", "cilindrada": 2, "combustible": "diesel", "ultima_posicion": "01/05/2022", "color": "azul", "latitud": 42.601129, "longitud": -5.5824023}, {"marca": "citroen", "modelo": "c4", "cilindrada": 1.2, "combustible": "gasolina", "ultima_posicion": "02/06/2022", "color": "rojo", "latitud": 53.18945, "longitud": -2.8896847}, {"marca": "toyota", "modelo": "corolla", "cilindrada": 1.8, "combustible": "gasolina", "ultima_posicion": "20/04/2022", "color": "blanco", "latitud": 34.6573875, "longitud": 135.1385848}]'

json_input = json.loads(json_string)

for row in json_input:
    if row["combustible"] == "gasolina":
        print (row)
