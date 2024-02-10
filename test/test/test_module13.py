import unittest


class TestClass14(unittest.TestCase):
    def test_case01(self):
        try:
            raise Exception
        except Exception as e:
            self.assertRaises(Exception, "raise Exception")
