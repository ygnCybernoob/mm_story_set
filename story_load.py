import json

with open('json_file.json', 'r', encoding='utf8') as f:

    js = json.loads(f.read())

    print(len(js))