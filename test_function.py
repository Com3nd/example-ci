from function import add, subtract, multiply
from function import convert_fahrenheit_to_celsius
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add("space", "ship") == "spaceship"


# uncomment the following test in step 5
def test_subtract():
    assert subtract(2, 3) == -1


# uncomment the following test in step 11
# def test_convert_fahrenheit_to_celsius():
#     assert convert_fahrenheit_to_celsius(32) == 0
#     assert convert_fahrenheit_to_celsius(122) == pytest.approx(50)
#     with pytest.raises(AssertionError):
#         convert_fahrenheit_to_celsius(-600)
