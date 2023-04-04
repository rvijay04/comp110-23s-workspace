"""EX04 - 'list' Utility Functions."""

__author__ = "730555483"


def all(x: list[int], y: int) -> bool:
    """To see if the y integer is each element in list."""
    i: int = 0
    if len(x) == 0:
        return False
    while i < len(x):
        if x[i] != y:
            return False
        i += 1
    return True


def max(x: list[int]) -> int:
    """Find max value in a list."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = x[0]
    i: int = 0
    while i < len(x):
        if x[i] > max_value:
            max_value = x[i]
        i += 1
    return max_value


def is_equal(a: list[int], b: list[int]) -> bool:
    """See if each element in a list are equal to each other."""
    i: int = 0
    if len(a) != len(b):
        return False
    else:
        while i < len(a):
            if a[i] != b[i]:
                return False
            i += 1
        return True