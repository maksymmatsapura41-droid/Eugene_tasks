import pytest

def is_even(number):
    return number % 2 == 0

@pytest.mark.parametrize("num, expected", [
    (2, True),
    (3, False),
    (0, True),
    (100, True),
    (7, False),
])
def test_is_even(num, expected):
    assert is_even(num) == expected