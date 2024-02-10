def func():
    x = 4
    action = lambda n: x**n
    return action


x = func()
print(x(2))


def func1():
    x = 4
    action = lambda n, x=x: x**n
    return action


x = func1()
print(x(3))


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i**x)
    return acts


acts = makeActions()
print(acts[0](1))


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i**x)
    return acts


acts = makeActions()
for i in range(5):
    print(acts[i](2))
