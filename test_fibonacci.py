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
    assert fibonacci.Fibonacci(0).list == [0]
