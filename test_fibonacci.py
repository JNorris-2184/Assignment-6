"""
test_fibonacci.py -- Test cases for fibonacci.py
"""

import pytest
import fibonacci


def test_invalid_datatype():
    """Assert non-integer raises a ValueError"""
    with pytest.raises(ValueError):
        fibonacci.Fibonacci('hello')
