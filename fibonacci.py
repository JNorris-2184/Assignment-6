"""
fibonacci.py:
    Iterable which produces an iterator of the Fibonacci series
     for a given value
"""


class Fibonacci:
    """An iterable to generate Fibonacci series."""

    def __init__(self, stop):
        """ Requires a single integer as input."""
        if int(stop):
            self.stop = stop
        raise ValueError

    def __iter__(self):
        """Returns the instance object which is an iterator."""
        return self

    def __next__(self):
        """Defines the instance object as an iterator."""
        return self
