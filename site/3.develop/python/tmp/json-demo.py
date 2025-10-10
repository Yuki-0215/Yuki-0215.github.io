import json

data = {
    'name': 'Alice',
    'age': 30
}

json_str = json.dumps(data)
print(json_str)

data = json.load(json_str)
print(data)
