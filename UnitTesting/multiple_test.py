import pytest


@pytest.mark.one
def test_method1():
    x = 10
    y = 10
    assert x == y


@pytest.mark.two
def test_method2():
    x = 15
    y = 20
    assert x + 5 == y
