import pytest

from project_euler.problem_3.problem_3_solution import largest_prime_factor, prime_factors


class TestPrimeFactors:
    @pytest.mark.parametrize(
        'input_number,output_list',
        [(6, [2, 3]),
         (24, [2, 2, 2, 3]),
         (120, [2, 2, 2, 3, 5]),
         (720, [2, 2, 2, 2, 3, 3, 5]),
         ])
    def test_prime_factors(self, input_number, output_list):
        """
        2*3 = 6
        2*3*4 = 2 * 3 * 2*2 = 24
        2*3*4*5 = 2 * 3 * 2*2 * 5= 120
        2*3*4*5*6 = 2 * 3 * 2*2 * 5 * 2*3 = 720
        """
        assert prime_factors(input_number) == output_list


class TestLargestPrimeFactor:
    @pytest.mark.parametrize(
        'input_number,output_largest_prime_factor',
        [(6, 3),
         (24, 3),
         (120, 5),
         (720, 5),
         ])
    def test_prime_factors(self, input_number, output_largest_prime_factor):
        assert largest_prime_factor(input_number) == output_largest_prime_factor
