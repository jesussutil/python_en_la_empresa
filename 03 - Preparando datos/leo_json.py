import json

with open('coches.json', 'r') as json_file:
    json_input = json.load(json_file)

print(json_input)

print ('----')

with open('coches.json', 'r') as json_file:
    json_input = json.loads(json_file.read())

print(json_input)
