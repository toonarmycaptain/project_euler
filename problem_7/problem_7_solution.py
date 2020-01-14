"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def nth_prime(n: int) -> int:
    """
    Returns the nth prime in sequence starting at 2.
    
    Implicitly define 0th and 1st prime as 2.
    
    :param n: int > 0
    :return: int
    """
    if n < 1:
        raise ValueError('Argument must be an integer greater than zero.')

    primes_list = [2]  # Initialise with 2.
    num = 3  # Initial prime test at 3

    # Find primes until nth prime:
    while len(primes_list) < n:
        # Check if num is divisible by any prime before it, or greater than root.
        for possible_factor in primes_list:
            if num % possible_factor == 0:
                break
            elif possible_factor > num ** 0.5:  # If factor > root of number, number will be prime.
                primes_list.append(num)
                break

        # Only check odd numbers ie 3 ++2
        num += 2

    # Return nth prime
    return primes_list[-1]


"""
# Solution to problem 7
nth_prime(10001) == 104743
"""