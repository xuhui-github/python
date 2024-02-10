try:
    x = 4 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")


lst = [1, 2, 3]
try:
    print(lst[3])
except IndexError as e:
    print(e)

try:
    lst + 2
except TypeError as e:
    print(e)

d = dict()
try:
    print(d["b"])
except KeyError as e:
    print(e)
