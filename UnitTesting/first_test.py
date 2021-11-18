import pytest


def func(x):
    return x*x

def test_method():
    assert func(9) == 81

