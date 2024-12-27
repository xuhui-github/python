def maxit(l,i):
    if i==len(l)-1:
        return l[i]
    else:
        if l[i]>maxit(l,i+1):
            return l[i]
        else:
            return maxit(l,i+1)
def minit(l,i):
    if i==len(l)-1:
        return l[i]
    else:
        if l[i]<minit(l,i+1):
            return l[i]
        else:
            return minit(l,i+1)

def issorted(l,i):
    if i==len(l)-1:
        return True
    else:
        return l[i]>l[i+1] and issorted(l,i+1)


l=[3,4,2,5]
v=maxit(l,0)
print v
v=minit(l,0)
print "min %d\n" %(v)
l=[3,2,1,0]
l=[1]
s=issorted(l,0)
print s
