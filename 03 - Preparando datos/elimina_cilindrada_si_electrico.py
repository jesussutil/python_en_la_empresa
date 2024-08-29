import json

with open('coches.json', 'r+') as json_file:
    json_input = json.load(json_file)
    json_file.seek(0)
    for row in json_input:
        if row["combustible"] == "electricidad":
            #del row["cilindrada"]
            row.pop("cilindrada")

    json.dump(json_input, json_file, indent = 4)
    json_file.truncate() # hay que truncar el archivo
