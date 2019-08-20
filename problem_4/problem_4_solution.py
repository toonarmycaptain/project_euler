"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from typing import Generator, Sequence, Iterable, Union


def yield_3_digit_products_from_largest_to_shortest() -> Generator[int, None, None]:
    """
    Yields all three digit products, one at a time.

    :return: Generator[int]
    """
    # for i in range(0, 1000):
    #     for j in range(0, 1000):
    # Iterating backwards is faster.
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            yield i * j


def is_palindrome(candidate: Union[int, Sequence]) -> bool:
    """
    Return bool if revered string is identical to original.

    NB Sequence typing means
    :param candidate: int, list, tuple, string
    :return: bool
    """
    if isinstance(candidate, int):
        candidate = str(candidate)
    return candidate[::-1] == candidate


def find_largest_palindrome(source_list: Iterable[int]) -> int:
    """Cycle through given iterable and return largest item.
    """
    largest = 0
    for item in source_list:
        if is_palindrome(item) and item > largest:
            largest = item
    return largest


if __name__ == '__main__':
    print(find_largest_palindrome(yield_3_digit_products_from_largest_to_shortest()))
