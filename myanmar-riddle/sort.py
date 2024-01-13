
import json

with open('myanmar-riddle.json', 'r') as f:

    js = json.loads(f.read())

    riddles = list(js['riddles'])

    riddles_sorted =  sorted(riddles, key=lambda x: x['riddle'])

    data = {
        'riddles': riddles_sorted
    }

    with open('sorted.json', 'w', encoding='utf8') as f2:

        f2.write(json.dumps(data, ensure_ascii=False))

    