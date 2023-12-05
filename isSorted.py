# coding: utf-8
get_ipython().run_line_magic('save', 'test.py')
find
def find(word,letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
    
get_ipython().run_line_magic('save', 'find.py')
help(save)
help(%save)
get_ipython().run_line_magic('colors', '')
get_ipython().run_line_magic('colors', 'green')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '')
dir
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('pwd', '')
issorted([1, 2, 3])
sorted([1,2,3])
sorted([1,2,4,3])
list('first','second')
list([1, 2, 3])
[1,2,5,]
{'name': 'hui','age': 12}.__class__
import requests
dir(requests)
requests.cookies
def isSorted(lst,i):
    if len(lst) == 0:
        return True
    elif len(lst) == 1:
        return True
    elif i == len(lst)-1
def isSorted(lst,i):
    if len(lst) == 0:
        return True
    elif len(lst) == 1:
        return True
    elif i == len(lst)-1:
        return True
    else:
        return lst[i]>list[i+1] and isSorted(lst,i+1)
        
isSorted([1,2,3,5],0)
def isSorted(lst,i):
    if len(lst) == 0:
        return True
    elif len(lst) == 1:
        return True
    elif i == len(lst)-1:
        return True
    else:
        return lst[i]>lst[i+1] and isSorted(lst,i+1)
        
def isSorted(lst,i):
    if len(lst) == 0:
        return True
    elif len(lst) == 1:
        return True
    elif i == len(lst)-1:
        return True
    else:
        return lst[i]>lst[i+1] and isSorted(lst,i+1)
        
isSorted([1,2,3,4],0)
isSorted([4,2,1],0)
isSorted([,100,4,2,1],0)
isSorted([100,4,2,1],0)
isSorted([0,100,4,2,1],0)
