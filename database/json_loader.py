import json

json_file = open('json_database.json',)
data = json.load(json_file)

for line in data:
    print(line)
