import unittest

class TestClass01(unittest.TestCase):
    def test_case01(self):
        my_str="ASHWIN"
        my_int=22
        self.assertTrue(isinstance(my_str,str))
        self.assertTrue(isinstance(my_int,int))

    def test_case02(self):
        my_pi=3.14
        self.assertTrue(isinstance(my_pi,float))
        self.assertEqual(3,len([1,2,4]))

if __name__ == '__main__':
    unittest.main()
