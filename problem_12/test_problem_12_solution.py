"""Tests for Project Euler problem 12"""
import pytest

from project_euler.problem_12.problem_12_solution import (get_divisors,
                                                          triangle_number_generator,
                                                          smallest_triangle_number_with_n_divisors,
                                                          )


@pytest.mark.parametrize('number, divisor_list',
                         [(1, [1]),
                          (3, [1, 3]),
                          (6, [1, 2, 3, 6]),
                          (10, [1, 2, 5, 10]),
                          (15, [1, 3, 5, 15]),
                          (21, [1, 3, 7, 21]),
                          (28, [1, 2, 4, 7, 14, 28]),
                          ])
def test_get_divisors(number, divisor_list):
    assert get_divisors(number) == divisor_list


def test_triangle_number_generator():
    triangle_number_sequence = [1, 3, 6, 10, 15, 21, 28]
    for iteration, triangle_number in enumerate(triangle_number_generator()):
        assert triangle_number == triangle_number_sequence[iteration]
        # break after end of list
        if len(triangle_number_sequence) - 1 == iteration:
            break


@pytest.mark.parametrize('number_of_divisors, triangle_number',
                         [(1, 1),
                          (2, 3),
                          (3, 6),
                          (5, 28),
                          (6, 28),
                          ])
def test_smallest_triangle_number_with_n_divisors(number_of_divisors, triangle_number):
    assert smallest_triangle_number_with_n_divisors(number_of_divisors) == triangle_number

# def test_problem_12_solution():
#     assert smallest_triangle_number_with_n_divisors(500) == 70600674
