#!/usr/bin/python
import os

class WeirdInt(int):
    def __add__(self,other):
        return int.__add__(self,other)+1

    def __repr__(self):
        return '<weirdo %d>' % self

    def do_this(self):
        print('this')

    def do_that(self):
        print('that')
w=WeirdInt(3)
y=WeirdInt(2)
print w+y
w.do_this()
iw.do_that()
