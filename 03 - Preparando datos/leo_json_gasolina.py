import json

with open('coches.json', 'r') as json_file:
    json_input = json.load(json_file)

    for row in json_input:
        if row["combustible"] == "gasolina":
            print (row)
