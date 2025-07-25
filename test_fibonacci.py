"""
test_fibonacci.py -- Test cases for fibonacci.py
"""

import pytest
import fibonacci


def test_invalid_datatype():
    """Assert non-integer raises a ValueError"""
    with pytest.raises(ValueError):
        fibonacci.Fibonacci('hello')


def test_zero_input():
    """Assert input of 0 returns a list containing only 0"""
    sequence = []
    for number in fibonacci.Fibonacci(0):
        print("number:", number)
        sequence.append(number)
    assert sequence == [0]


def test_one_input():
    """Assert input of 1 returns a list containing 0,1 """
#   for number in fibonacci.Fibonacci(1):
#        continue
    sequence = []
    for number in fibonacci.Fibonacci(1):
        print("number:", number)
        sequence.append(number)
    assert sequence == [0, 1]
