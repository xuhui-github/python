X = 99


def f1():
    X = 88

    def f2():
        print(X)

    f2()


def f3():
    print("X=%d" % X)


f1()
f3()
