from nose.tools import assert_equals
from nose.tools import raises


@raises(AssertionError)
def test_case01():
    print("In test_case01()...")
    assert 2 + 2 == 5


@raises(AssertionError)
def test_case02():
    print("In test_case02()...")
    assert_equals(2 + 2, 5)
