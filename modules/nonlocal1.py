def tester(start):
    state = start #Each call gets its own state
    def nested(label):
        nonlocal state #Remember state in enclosing scope
        print(label,state)
        state += 1 #Allowed to change it if nonlocal #UnboundLocalError: local variable 'state' referenced before assignment
    return nested


F = tester(0)
F('spam')
F('ham')
F('eggs')


#def tester(start):
#    def nested(label):
#        nonlocal state #SyntaxError: no binding for nonlocal 'state' found 
#        state = 0
#        print(label, state)
#    return nested


def tester(start):
    def nested(label):
        global state #Global do not have to exist yet when declared
        state=0      #This creates the name in the module now
        print(label,state)
        
    return nested

F = tester(0)
F('abc')
F('def')
print(state)

#spam = 99 #SyntaxError: no binding for nonlocal 'spam' found
def tester():
    spam = 99
    def nested():
        nonlocal spam
        print('Current=',spam)
        spam += 1
    return nested
F = tester()
F()
F()
