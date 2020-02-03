"""Project Euler problem 10 solution

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
def find_sum_of_primes(largest_prime: int) -> int:
    if largest_prime < 2:
        raise ValueError('Argument must be an integer greater than one.')

    sum_of_primes = 2  # Initialise with 2.
    primes_list = [2]
    num = 3  # Initial prime test at 3

    # Find primes until nth prime:
    while num <= largest_prime:
        # Check if num is divisible by any prime before it, or greater than root.
        for possible_factor in primes_list:
            if num % possible_factor == 0:
                break
            elif possible_factor > num ** 0.5:  # If factor > root of number, number will be prime.
                primes_list.append(num)
                sum_of_primes += num
                break

        # Only check odd numbers ie 3 ++2
        num += 2
    return sum_of_primes

"""
# Solution to problem 10
find_sum_of_primes(2000000) == 142913828922
"""