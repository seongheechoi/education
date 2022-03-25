import re

# greedy
fdata1 = re.findall(r'<b>.+</b>', '<b>blog</b>is a<b>website</b>containing a body')
print(fdata1)

# lazy
fdata2 = re.findall(r'<b>.+?</b>', '<b>blog</b>is a<b>website</b>containing a body')
print(fdata2)