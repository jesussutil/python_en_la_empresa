import json

json_string = {"marca": "tesla", "modelo": "model 3", "cilindrada": "", "combustible": "electricidad", "ultima_posicion": "06/06/2022", "color": "negro", "latitud": 39.538139, "longitud": -119.4484472}

with open('coches.json', 'r+') as json_file:
    json_input = json.load(json_file)
    json_input.append(json_string)
    json_file.seek(0)
    json.dump(json_input, json_file, indent = 4)
