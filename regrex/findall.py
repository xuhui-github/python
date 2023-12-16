import re
pat='[a-zA-Z]+'
text='"HM... Err -- are you sure?" he said, sounding insecure.'
print(re.findall(pat,text))

pat=r'[.?\-",]+'
print(re.findall(pat,text))

pat='{name}'
text='Dear {name}...'
print(re.sub(pat,'Mr. Gumby',text))

