"""Tests for Project Euler problem 11"""

from project_euler.problem_11.problem_11_solution import (algorithms,
                                                          problem_grid,
                                                          run_alg,
                                                          )

def test_problem_11_solution():
    assert run_alg(problem_grid, algorithms) == 70600674
