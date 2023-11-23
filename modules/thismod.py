var = 99

def local():
    var=0 #change local var
    print("in local() var= %d" %var)
#    global var
#    print("in local global var is %d" % var)

def glob():
    global var #access the global var by global
    var += 1 #change global var
    print("var gobal is %d" % var)
def glob2():
    var=0 #change local var
    import thismod
    thismod.var +=1 #change global var by import module thismod itself
    print("thismod.var=%d" % thismod.var)
def glob3():
    var=0
    import sys
    glob = sys.modules['thismod']
    glob.var += 1
    print("glob.var=%d" % glob.var)

def test():
    print(var)
    local();glob(); glob2(); glob3()
    print(var)
