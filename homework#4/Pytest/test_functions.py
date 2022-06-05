import pytest
from functions_to_test import *

calc = Calculator(4, 6)
calc2 = Calculator(12, 0)

def test_add():
    assert calc.add() == 10
    assert calc2.add() == 12

def test_subtract():
    assert calc.subtract() == -2
    assert calc2.subtract() == 12

def test_multiply():
    assert calc.multiply() == 24
    assert calc2.multiply() == 0

def test_divide():
    assert calc.divide() == 0.6666666666666666
    with pytest.raises(ValueError):
        calc2.divide()
