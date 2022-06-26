#!/usr/bin/python

def findSizeRecursive(root):
    if root is None:
        return 0
    else:
        return findSizeRecursive(root.left)+findSizeRecursive(root.right)


