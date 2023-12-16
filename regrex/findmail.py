import re
import fileinput
pat=re.compile('From: (.*) <.*?>$')
for line in fileinput.input('headers.txt'):
    m=pat.match(line)
    if m: print(m.group(1))




