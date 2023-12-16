f=open('./filetest.py')
print(f.read(7))

print(f.read(4))
f.close()

with open('./filetest.py') as somefile:
    print(somefile.read(10))
    print(somefile.read(20))


file f=open('./filetest.py')
try:
    print(f.read(50))
    print(f.read(1))
finally:
    f.close()

