import json
with open('output.txt') as file:
    for line in file:
        s = json.loads(line)
        print(s['auprc'])

