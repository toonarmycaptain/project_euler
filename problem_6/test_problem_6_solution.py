import pytest

from project_euler.problem_6.problem_6_solution import (difference_between_sum_of_squares_and_square_of_sum,
                                                        square_sum_of_consecutive_natural_numbers,
                                                        sum_consecutive_squared_natural_numbers,
                                                        )

class TestSumConsecutiveSquarednaturalNumbers:
    @pytest.mark.parametrize(
        'min_range, max_range, result',
        [(1, 10, 385),
         (2, 10, 384)]
    )
    def test_sum_consecutive_squared_numbers(self, min_range, max_range, result):
        assert sum_consecutive_squared_natural_numbers(min_range, max_range) == result

    @pytest.mark.parametrize(
    'arg1, arg2',
    [('a', 'b'),  # Strings
     (1.1, 2.2),  # Floats
     ([1], [2]),  # Lists
     ((3,), (4,)),  # Tuples
     ({5: 6}, {7: 8}),  # Dicts
     ])
    def test_sum_consecutive_squared_natural_numbers_non_int_args(self, arg1, arg2):
        with pytest.raises(TypeError):
            sum_consecutive_squared_natural_numbers(arg1, arg2)

    @pytest.mark.parametrize(
        'arg1, arg2',
        [(1, 0),
         (0, 1),
         (1, -1),
         (-1, 1),
         ])
    def test_sum_consecutive_squared_natural_numbers_zero_or_less_args(self, arg1, arg2):
        with pytest.raises(ValueError):
            sum_consecutive_squared_natural_numbers(arg1, arg2)

    def test_sum_consecutive_squared_natural_numbers_range_low_larger_than_range_high(self):
        with pytest.raises(ValueError):
            sum_consecutive_squared_natural_numbers(2, 1)


class TestSquareSumOfConsecutiveNaturalNumbers:
    @pytest.mark.parametrize(
        'min_range, max_range, result',
        [(1, 10, 3025),  # 1+2..10 = 55, 55^2 = 3025
         (2, 10, 2916),  # 2+3..10 = 55, 54^2 = 2916
         ]
    )
    def test_square_sum_of_consecutive_natural_numbers(self, min_range, max_range, result):
        assert square_sum_of_consecutive_natural_numbers(min_range, max_range) == result

    @pytest.mark.parametrize(
    'arg1, arg2',
    [('a', 'b'),  # Strings
     (1.1, 2.2),  # Floats
     ([1], [2]),  # Lists
     ((3,), (4,)),  # Tuples
     ({5: 6}, {7: 8}),  # Dicts
     ])
    def test_square_sum_of_consecutive_natural_numbers_non_int_args(self, arg1, arg2):
        with pytest.raises(TypeError):
            square_sum_of_consecutive_natural_numbers(arg1, arg2)

    @pytest.mark.parametrize(
        'arg1, arg2',
        [(1, 0),
         (0, 1),
         (1, -1),
         (-1, 1),
         ])
    def test_square_sum_of_consecutive_natural_numbers_zero_or_less_args(self, arg1, arg2):
        with pytest.raises(ValueError):
            square_sum_of_consecutive_natural_numbers(arg1, arg2)

    def test_square_sum_of_consecutive_natural_numbers_range_low_larger_than_range_high(self):
        with pytest.raises(ValueError):
            square_sum_of_consecutive_natural_numbers(2, 1)


class TestDifferenceBetweenSumOfSquaresAndSquareOfSum:
    @pytest.mark.parametrize(
        'min_range, max_range, result',
        [(1, 10, 3025-385),
         (2, 10, 2916-384),
         ]
    )
    def test_difference_between_sum_of_squares_and_square_of_sum(self, min_range, max_range, result):
        assert difference_between_sum_of_squares_and_square_of_sum(min_range, max_range) == result

    @pytest.mark.parametrize(
        'arg1, arg2',
        [('a', 'b'),  # Strings
         (1.1, 2.2),  # Floats
         ([1], [2]),  # Lists
         ((3,), (4,)),  # Tuples
         ({5: 6}, {7: 8}),  # Dicts
         ])
    def test_difference_between_sum_of_squares_and_square_of_sum_non_int_args(self, arg1, arg2):
        with pytest.raises(TypeError):
            difference_between_sum_of_squares_and_square_of_sum(arg1, arg2)

    @pytest.mark.parametrize(
        'arg1, arg2',
        [(1, 0),
         (0, 1),
         (1, -1),
         (-1, 1),
         ])
    def test_difference_between_sum_of_squares_and_square_of_sum_zero_or_less_args(self, arg1, arg2):
        with pytest.raises(ValueError):
            difference_between_sum_of_squares_and_square_of_sum(arg1, arg2)

    def test_square_sum_of_consecutive_numbers_range_low_larger_than_range_high(self):
        with pytest.raises(ValueError):
            difference_between_sum_of_squares_and_square_of_sum(2, 1)