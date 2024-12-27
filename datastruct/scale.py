#!/usr/bin/python

def scale(data,factor):
    for j in xrange(len(data)):
        data[j]*=factor
data=[1,2,3]
print data
scale(data,2.0)
print data

