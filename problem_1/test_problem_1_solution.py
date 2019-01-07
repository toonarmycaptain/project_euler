from project_euler.problem_1.problem_1_solution import sum_multiples, efficient_sum_multiples_3_or_5


def test_sum_multiples():
    multiples = (3, 5)
    minimum = 0
    maximum = 9
    min_max = (minimum, maximum)
    assert sum_multiples(multiples, min_max) == 23


def test_efficient_sum_multiples_3_or_5():
    min_max = (0, 9)
    assert efficient_sum_multiples_3_or_5(min_max) == 23


def test_all_solutions_are_equal():
    multiples = (3, 5)
    minimum = 0
    maximum = 9
    min_max= (minimum, maximum)
    assert sum_multiples(multiples, min_max) == efficient_sum_multiples_3_or_5(min_max)

