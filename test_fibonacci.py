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
    """Assert input of 2 returns a list containing 0,1 """
    assert call_fibonacci(2) == [0, 1, 1]
