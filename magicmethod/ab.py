class A:
    def hello(self):
        print("I am A")


class B(A):
    pass


class C(A):
    def hello(self):
        print("I am C")


if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    a.hello()
    b.hello()
    c.hello()
