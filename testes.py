import bson
import json



with open('leads.bson','rb') as f:
    data = bson.loads(f.read())


print(data)
for k,v in data['user'].items():
    # print(v)
    pass

with open('a.json', 'w') as f:
    json.dump(data, f)
