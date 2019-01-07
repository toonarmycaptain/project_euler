def sum_even_fibonacci_numbers(maximum: int):
    """
    Sum even fibonacci numbers that are less than the maximum value.
    :param maximum: int
    :return: int
    """

    number_a = 0
    number_b = 1
    total = 0  # initialise total,
    while number_b < maximum:
        number_a, number_b = number_b, number_a + number_b
        if not number_b % 2:  # if number_b is even
            total += number_b
        # if number_b > max, loop ends, too great number_b not added to total
    return total


if __name__ == '__main__':
    print(sum_even_fibonacci_numbers(3999999))