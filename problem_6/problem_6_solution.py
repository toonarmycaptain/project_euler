"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def sum_consecutive_squared_natural_numbers(range_low: int, range_high: int) -> int:
    """
    Return the sum of the squares of the given range of numbers.

    :param range_low: int >0
    :param range_high: int >0
    :return: int
    """

    if not isinstance(range_low, int) or not isinstance(range_high, int):
        raise TypeError("Arguments must be integers.")
    if range_low <= 0 or range_high <=0:
        raise ValueError("Arguments must be greater than 0.")
    if range_low > range_high:
        raise ValueError("Low end of range cannot be higher than high end.")

    return sum((n**2 for n in range(range_low, range_high+1)))


def square_sum_of_consecutive_natural_numbers(range_low: int, range_high: int) -> int:
    """
    Return the square of the sum of the given range of numbers.

    :param range_low: int >0
    :param range_high: int >0
    :return: int
    """
    if not isinstance(range_low, int) or not isinstance(range_high, int):
        raise TypeError("Arguments must be integers.")
    if range_low <= 0 or range_high <=0:
        raise ValueError("Arguments must be greater than 0.")
    if range_low > range_high:
        raise ValueError("Low end of range cannot be higher than high end.")

    return sum((n for n in range(range_low, range_high+1)))**2


def difference_between_sum_of_squares_and_square_of_sum(range_low: int, range_high: int) -> int:
    """
    Return difference between the sum of the squares and the square of the sum
    of the given range of numbers

    :param range_low: int >0
    :param range_high: int >0
    :return: int
    """
    if not isinstance(range_low, int) or not isinstance(range_high, int):
        raise TypeError("Arguments must be integers.")
    if range_low <= 0 or range_high <=0:
        raise ValueError("Arguments must be greater than 0.")
    if range_low > range_high:
        raise ValueError("Low end of range cannot be higher than high end.")

    return square_sum_of_consecutive_natural_numbers(range_low, range_high) - sum_consecutive_squared_natural_numbers(range_low, range_high)


if __name__ == '__main__':
    print(difference_between_sum_of_squares_and_square_of_sum(1, 100))
