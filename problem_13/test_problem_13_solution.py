"""Tests for Project Euler problem 13"""
import pytest

from project_euler.problem_13.problem_13_solution import first_10_digits_of_sum, problem_number_list


@pytest.mark.parametrize('number_list, returned_string',
                         [([1], '0000000001'),
                          ([12], '0000000012'),
                          ([123], '0000000123'),
                          ([1234], '0000001234'),
                          ([12345], '0000012345'),
                          ([123456], '0000123456'),
                          ([1234567], '0001234567'),
                          ([12345678], '0012345678'),
                          ([123456789], '0123456789'),
                          ([1234567890], '1234567890'),
                          ([12345678901], '1234567890'),
                          ([123456789012], '1234567890'),
                          ])
def test_first_10_digits_of_sum(number_list, returned_string):
    assert first_10_digits_of_sum(number_list) == returned_string


def test_problem_13_solution():
    assert first_10_digits_of_sum(problem_number_list) == '5537376230'
