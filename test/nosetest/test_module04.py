from nose.tools import with_setup


def setUpModule():
    print("\nIn setUpModule()...")


def tearDownModule():
    print("\nIn tearDownModule()...")


def setup_function():
    print("\nsetup_function()...")


def teardown_function():
    print("\nteardown_function()...")


def test_case01():
    print("In test_case01()...")


def test_case02():
    print("In test_case02()...")


@with_setup(setup_function, teardown_function)
def test_case03():
    print("In test_case03()...")
