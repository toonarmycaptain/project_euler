"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
"""


def prime_factors(number):
    """
    Returns list of prime factors for the number supplied. 

    :param number:
    :return: list.
    """
    # count = 0
    i = 2
    prime_factors_list = []
    while i * i <= number:  # if x*y == number, and x>y, number%y will already have found x.
        if number % i:  # If number not cleanly divisible by i
            i += 1
        else:  # ie number%i = 0 ie i is a factor because is cleanly divisible.
            # number = number//i ->remaining factor must be smaller than number//i or they would have already been found
            # because their multiple to equal number would have been found.
            number //= i
            prime_factors_list.append(i)
    if number > 1:
        prime_factors_list.append(number)
    return prime_factors_list  # , count


def largest_prime_factor(number):
    return max(set(prime_factors(number)))


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
