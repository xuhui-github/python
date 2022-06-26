#!/usr/bin/python
class CountDown:
    def __init__(self,start):
        self.start=start

    def __iter__(self):
        n=self.start
        while n>0:
            yield n
            n=n-1

    def __reverse__(self):
        i=1
        while i<=n:
            yield i
            i=i+1

if __name__=='__main__':
    count=CountDown(10)
    for i in iter(count):
        print i

    for i in reversed(list(count)):
        print i
