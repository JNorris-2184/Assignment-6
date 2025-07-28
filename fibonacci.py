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
        self.stop = stop    # number of iterations
        self.current = 0    # current number
        self.position = 0   # position in Fibonacci series
        self.previous = 0   # previous value in series

    def __iter__(self):
        """Returns the instance object which is an iterator."""
        return self

    def __next__(self):
        """Defines the instance object as an iterator."""
        if self.position <= self.stop:
            if self.position == 0:
                self.current += 1
                next_number = 0
            elif self.position == 1:
                next_number = 1
            else:
                self.previous, self.current = (self.current,
                                               self.current + self.previous)
                next_number = self.current
            self.position += 1
            return next_number
        raise StopIteration
