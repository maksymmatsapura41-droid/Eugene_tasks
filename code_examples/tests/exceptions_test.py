import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("На нуль ділити не можна!")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert str(excinfo.value) == "На нуль ділити не можна!"