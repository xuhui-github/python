def tester(start):
    global state  # Move it out of the module to change it
    state = start  # global allows change in module scope

    def nested(label):
        global state
        print(label, state)
        state += 1

    return nested


F = tester(0)
F("abc")
F("def")
state += 3
F("ghi")
# import StateWithGlobals
# print(StateWithGlobals.state)
