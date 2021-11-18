from UnitTesting import calc


def test_add():
    assert calc.add(7, 3) == 10
    assert calc.add(7) == 10
    assert calc.add(3) == 10
