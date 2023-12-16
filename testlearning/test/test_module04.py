import unittest
import inspect
#python -m unittest -v test_module04
#python -m unittest -v test_module04.TestClass04
#python -m unittest -v test_module04.TestClass05
#python -m unittest -v test_module04.TestClass05.test_case06
class TestClass04(unittest.TestCase):
    def test_case04(self):
        print("\nClassname: " +self.__class__.__name__)
        print("Running Test Method: " + inspect.stack()[0][3])

class TestCase05(unittest.TestCase):
    def test_case05(self):
        print("\nClassname: " + self.__class__.__name__)
        print("Running Test Method: " + inspect.stack()[0][3])

    def test_case06(self):
        print("I am here...")


if __name__ == '__main__':
    unittest.main(verbosity=2)


