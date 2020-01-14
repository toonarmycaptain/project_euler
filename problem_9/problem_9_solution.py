"""Project Euler problem 9 solution

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import math

from typing import Optional


def pythagorean_triplet(n: int) -> Optional[int]:
    """

    :param n: int
    :return: int or None
    """
    for b in range(n):
        for a in range(1, b):  # a<b<c
            c = math.sqrt(a**2 + b**2)
            # c is a whole number and triplet adds to 1000
            if c % 1 == 0 and a + b + c == n:
                # int() is safe before a and b are integers, and c is tested:
                return int(a * b * c)
    # Apparently PEP8 advocates an explicit return None.
    return None


"""
# Solution to problem 9
pythagorean_triplet(1000) == 31875000
"""