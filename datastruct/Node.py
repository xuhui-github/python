#!/usr/bin/python

class Node:
    def __init__(self,val):
        self.value=val
        self.children=[]

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self,node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)

if __name__=='__main__':
    root=Node(0)
    child1=Node(1)
    child2=Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print ch


