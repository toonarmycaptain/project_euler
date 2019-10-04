# https://projecteuler.net/problem=1


def sum_multiples(multiples: tuple, min_max: tuple) -> int:
    """
    Takes a range and a list of numbers, returns the sum of the numbers
    within the range that are multiples of any number in the list of
    multiples.

    :param multiples: tuple (**int)
    :param min_max: tuple (int, int)
    :return: int
    """
    minimum = min_max[0]
    maximum = min_max[1]
    total = 0
    for i in range(minimum, maximum+1):
        for j in multiples:
            if i % j == 0:
                total += i
                break

    return total


def efficient_sum_multiples_3_or_5(min_max: tuple):
    """
    One-liner of sum_multiples using list comprehension.
    :param min_max: tuple (int, int)
    :return: int
    """
    minimum = min_max[0]
    maximum = min_max[1]
    return sum([i for i in range(minimum, maximum+1)
                if i % 3 == 0
                or i % 5 == 0
                ])


if __name__ == '__main__':
    # Solution to problem 1
    print(sum_multiples((3, 5), (0, 999)))
