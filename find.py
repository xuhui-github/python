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
    
