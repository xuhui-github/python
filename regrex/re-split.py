import re

some_text = "alpha,beta,,,,gamma   delta"
result = re.split("[, ]+", some_text)
print(result)

# whith maxsplit
result = re.split("[, ]+", some_text, maxsplit=2)
print(result)

result = re.split("[, ]+", some_text, maxsplit=1)
print(result)
