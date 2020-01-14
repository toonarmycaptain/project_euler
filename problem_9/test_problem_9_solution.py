"""Tests for Project Euler problem 9"""
import pytest

from project_euler.problem_9.problem_9_solution import pythagorean_triplet


@pytest.mark.parametrize('sum, product',
                         [(3 + 4 + 5, 3 * 4 * 5),
                          (6+8+10, 6*8*10),
                          (1000, 31875000),
                          (27, None),
                          pytest.param(3 + 4 + 5, 3+4+5, marks=pytest.mark.xfail),
                          pytest.param(6+8+10, 'None found.', marks=pytest.mark.xfail),
                                                    ])
def test_pythagorean_triplet(sum, product):
    assert pythagorean_triplet(sum) == product
