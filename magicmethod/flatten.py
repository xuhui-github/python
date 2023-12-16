def flatten(nested):
    try:
        for sub in nested:
            for elem in flatten(sub):
                yield elem
    except TypeError:
        yield nested

print(list(flatten([[[1],2],3,4,[5,[6,7]],8])))

  
