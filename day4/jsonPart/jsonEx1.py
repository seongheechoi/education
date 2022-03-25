import json

file = open('json_example.json', 'r', encoding='utf-8')
content = file.read()
jdata = json.loads(content)
print(jdata)
print(type(jdata))
print()

for data in jdata['employees']:
    print(data['firstName']+' : '+ data['lastName'])

print(jdata.keys)