"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def smallest_divisible(range_low: int, range_high: int) -> int:
    """
    Return smallest number that is a multiple of each of the numbers in the
    range. Or "the  smallest positive number that is evenly divisible by all
    of the numbers" in the given range.

    :param range_low: int >0
    :param range_high: int >0
    :return: int
    """
    if not isinstance(range_low, int) or not isinstance(range_high, int):
        raise TypeError("Arguments must be integers.")
    if range_low <= 0 or range_high <= 0:
        raise ValueError("Arguments must be greater than 0.")
    if range_low > range_high:
        raise ValueError("Low end of range cannot be higher than high end.")

    candidate_multiple = range_high  # Start with highest number, as answer must be a multiple.

    for factor in range(range_low, range_high):
        if candidate_multiple % factor > 0:  # ie candidate_multiple not already divisible by factor
            # Find lowest number in range that candidate_multiple*factor is divisible by:
            for new_candidate_factor in range(range_low, range_high):
                # Check if candidate_multiple * new_candidate_factor_candidate
                if (candidate_multiple * new_candidate_factor) % factor == 0:
                    candidate_multiple *= new_candidate_factor  # Multiple candidate_multiple by that factor.
                    break
    return candidate_multiple


"""
# Solution to problem 5
print(smallest_divisible(1, 20)) == 232792560
"""
