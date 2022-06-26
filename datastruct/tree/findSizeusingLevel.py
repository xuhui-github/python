#!/usr/bin/python

def findSizeusingLevel(root):
    if root is None:
        return 0
    else:
        q=Queue()
        q.enQueue(root)
        node=None
        count=0
        while not q.isEmpty():
            node=q.deQueue()
            count+=1
            if node.left is not None:
                q.enQueue(node.left)
            if node.right is not None:
                q.enQueue(node.right)

        return count


