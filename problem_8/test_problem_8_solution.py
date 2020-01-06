"""Tests for Project Euler problem 8"""
import pytest

from problem_8.problem_8_solution import largest_product_in_series, problem_series

def test_largest_product_in_series():
    assert largest_product_in_series(problem_series, 4) == (5832, '9989')
