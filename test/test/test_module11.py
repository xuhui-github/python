import unittest


class TestClass12(unittest.TestCase):
    @unittest.skip("skip just a fail test by fail()")
    def test_case01(self):
        """This is a test method..."""
        print(self.id())
        self.fail()
