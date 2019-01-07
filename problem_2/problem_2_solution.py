def sum_even_fibonacci_numbers(maximum: int):
    """
    Sum even fibonacci numbers that are less than the maximum value.

    :param maximum: int
    :return: int
    """
    number_a = 1
    number_b = 2
    total = 0  # Initialise total.
    while number_b < maximum:
        if not number_b % 2:  # If number_b is even.
            total += number_b
        number_a, number_b = number_b, number_a + number_b

        # If number_b > max, loop ends, too great number_b not added to total.
    return total


if __name__ == '__main__':
    print(sum_even_fibonacci_numbers(3999999))
