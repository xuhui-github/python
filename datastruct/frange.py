#!/usr/bin/python

def frange(start,stop,increment):
    x=start
    while(x<stop):
        yield x
        x=x+increment

if __name__=='__main__':
    for n in frange(1,10,0.5):
        print n

