def swaplist(lst):
    start,end=0,len(lst)-1
    while start<end:
        lst[start],lst[end]=lst[end],lst[start]
        start=start+1
        end=end-1

l=[1,2,3,4,5]
swaplist(l)
print l
