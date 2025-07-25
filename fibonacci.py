"""
fibonacci.py:
    Iterable which produces an iterator of the Fibonacci series
     for a given value
"""


class Fibonacci:
    """An iterable to generate Fibonacci series."""

    def __init__(self, stop):
        """ Requires a single integer as input."""
        if not isinstance(stop, int):
            raise ValueError
        self.stop = stop
        self.current = 0
        self.sum = 0

    def __iter__(self):
        """Returns the instance object which is an iterator."""
        return self

    def __next__(self):
        """Defines the instance object as an iterator."""
        if self.sum <= self.stop:
            next_number = self.current
            self.current += 1
            self.sum += self.current
            return next_number
        raise StopIteration
