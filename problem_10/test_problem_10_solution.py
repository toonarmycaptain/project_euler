"""Tests for Project Euler problem 10"""
import pytest

from project_euler.problem_10.problem_10_solution import find_sum_of_primes


@pytest.mark.parametrize('limit, sum_of_primes',
                         [(2, 2),
                          (3, 5),
                          (10, 17),
                          # (2000000, 142913828922),  # Long running test.
                          pytest.param(11, 20, marks=pytest.mark.xfail),
                          ])
def test_find_sum_of_primes(limit, sum_of_primes):
    assert find_sum_of_primes(limit) == sum_of_primes


@pytest.mark.parametrize('limit, sum_of_primes',
                         [(-5001, 'Should raise error.'),
                          (-1, 'Should raise error.'),
                          (0, 'Should raise error.'),
                          (1, 'Should raise error.'),
                          ])
def test_find_sum_of_primes_raising_error(limit, sum_of_primes):
    with pytest.raises(ValueError):
        assert find_sum_of_primes(limit) == sum_of_primes
