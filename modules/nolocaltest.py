#nonlocal restricts scope lookup to just enclosing defs, requires that the names all
#ready exist there,and allows them to be assigned.Scope lookup does not continue oct##to the global or built-in scope



def tester(start):
    state = start
    def nested(label):
        print(label, start)
    return nested

F = tester(0)
F('spam')
F('ham')
