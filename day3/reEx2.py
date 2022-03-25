import re

robj1 = re.match(r'[a-zA-Z0-9]+', 'Hello1234')
print(robj1)

robj2 = re.match(r'([0-9]+) ([0-9]+)', '322 777 good')
print(robj2)
print(robj2.group(0))
print(robj2.group(1))
print(robj2.group(2))
print(robj2.groups())

print()
robj3 = re.match(r'(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(4323423)')
print(robj3)
print(robj3.groups())
print(robj3.group('func'))
print(robj3.group('arg'))