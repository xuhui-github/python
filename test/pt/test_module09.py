import pytest


def test_case01():
    with pytest.raises(Exception):
        x = 1 / 0


def test_case02():
    with pytest.raises(KeyError):
        d = {"name": "hui"}
        print(d["age"])
