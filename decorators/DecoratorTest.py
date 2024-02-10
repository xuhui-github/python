class DecoratorTest(object):
    """
    Test regular method vs @classmetho vs @staticmethod
    """

    def __init__(self):
        """Constructor"""
        pass

    def doubler(self, x):
        """"""
        print("running doubler")
        return x * 2

    @classmethod
    def class_tripler(kclass, x):
        """"""
        print("running tripler %s" % kclass)
        return x * 3

    @staticmethod
    def static_quad(x):
        """"""
        print("running quard")
        return x * 4


if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    print(decor.static_quad(3))

    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)
