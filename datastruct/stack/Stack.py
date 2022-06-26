#!/usr/bin/python

class Stack(object):

    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit

    def isEmpty(self):
        return len(self.stk)<=0

    def push(self,item):
        if len(self.stk)>=self.limit:
            print "Stack Overflow"
        else:
            self.stk.append(item)

    def pop(self):
        if len(self.stk)<=0:
            print "Stack Underflow"
            return 0
        else:
            return self.stk.pop()
    def peek(self):
        if len(self.stk)<=0:
            print "Stack Underflow"
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

s=Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print s.peek()
print s.pop()
print s.peek()
print s.pop()

