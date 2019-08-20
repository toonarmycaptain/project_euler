from types import GeneratorType
import pytest

from project_euler.problem_4.problem_4_solution import (yield_3_digit_products_from_largest_to_shortest,
                                                        find_largest_palindrome,
                                                        is_palindrome,
                                                        )


def test_yield_3_digit_products_from_largest_to_shortest():
    assert isinstance(yield_3_digit_products_from_largest_to_shortest(), GeneratorType)


@pytest.mark.parametrize(
    'argument,output',
    # Single character
    [('a', True),
     (1, True),
     ('aa', True),
     ('ab', False),
     (12, False),
     (55, True),
     ('abc', False),
     ('abccba', True),
     ])
def test_is_palindrome(argument, output):
    assert is_palindrome(argument) is output


@pytest.mark.parametrize(
    'argument,largest',
    [  # Lists
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 5),
        # Sets
        ((1, 2, 3, 4, 5), 5),
        ((5, 4, 3, 2, 1), 5),
        # Generators
        ((x for x in range(50)), 44),
        ((x for x in range(50, 0, -1)), 44)
    ])
def test_find_largest_palindrome(argument, largest):
    assert find_largest_palindrome(argument) == largest


def test_full_test():
    assert find_largest_palindrome(yield_3_digit_products_from_largest_to_shortest()) == 906609
