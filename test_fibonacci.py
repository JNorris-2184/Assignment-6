"""
test_fibonacci.py -- Test cases for fibonacci.py
"""

import pytest
import fibonacci


def call_fibonacci(value):
    """Accepts integer and returns Fibonacci series"""
    sequence = []
    for number in fibonacci.Fibonacci(value):
        sequence.append(number)
    return sequence


def test_invalid_datatype():
    """Assert non-integer raises a ValueError"""
    with pytest.raises(ValueError):
        fibonacci.Fibonacci('hello')


def test_zero_input():
    """Assert input of 0 returns a list containing only 0"""
    assert call_fibonacci(0) == [0]


def test_one_input():
    """Assert input of 1 returns a list containing 0,1 """
    assert call_fibonacci(1) == [0, 1]


def test_two_input():
    """Assert input of 2 returns a list containing 0,1,1 """
    assert call_fibonacci(2) == [0, 1, 1]


def test_four_input():
    """Assert input of 4 returns a list containing 0,1,1,2,3 """
    assert call_fibonacci(4) == [0, 1, 1, 2, 3]


def test_ten_input():
    """Assert input of 10 returns correct list """
    assert call_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_negative_input():
    """Assert negative value input returns an empty list """
    assert not call_fibonacci(-1)
