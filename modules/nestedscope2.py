def f1():
    X = 88

    def f2():
        print(X)

    return f2


action = f1()
action()
# in this code ,the call to action is really running the function we named f2 when
# f1 ran,this works because functions are objects in Python like everything else,and
# can be passed back as return values from other functions,Most importantly, f2
# remembers the enclosing scope's X in f1,even though f1 is no longer active.
