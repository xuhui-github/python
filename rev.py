def rev(theString):
    if len(theString) == 0 or len(theString) == 1:
        return theString
    else:
        head = theString[0]
        tail = theString[1:]
        print("head= %s" % head)
        print("tail= %s" % tail)
        print("rev(tail)+head =%s" % rev(tail) + head)
        return rev(tail) + head


print(rev("hello"))
