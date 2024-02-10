import unittest


class TestCase08(unittest.TestCase):

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case01()")

    def test_case02(self):
        self.assertFalse("Python".isupper())
        print("In test_case02()...")

    def test_case03(self):
        self.assertTrue(True)
        print("\nIn test_case03()...")

    def notest(self):
        self.assertTrue(True)
