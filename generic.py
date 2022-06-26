#!/usr/bin/python

def compute(data):
    for element in data:
        yield element**2

def square(numbers):
    for number in numbers:
        yield number ** 2

for n in compute([2,3,4]):
    print n

for n in square([2,3,5]):
    print n
