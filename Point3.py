#!/usr/bin/python

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def move(self,x,y):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)
p=Point(3,5)
print(p.x,p.y)
p=Point()
print(p.x,p.y)
