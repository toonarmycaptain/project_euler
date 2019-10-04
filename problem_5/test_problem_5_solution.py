import pytest

from project_euler.problem_5.problem_5_solution import smallest_divisible


def test_smallest_divisible_1_10():
    assert smallest_divisible(1, 10) == 2520

def test_smallest_divisible_1_10():
    assert smallest_divisible(1, 20) == 232792560

@pytest.mark.parametrize(
    'arg1, arg2',
    [('a', 'b'),  # Strings
     (1.1, 2.2),  # Floats
     ([1], [2]),  # Lists
     ((3,), (4,)),  # Tuples
     ({5: 6}, {7: 8}),  # Dicts
     ])
def test_smallest_divisible_non_int_args(arg1, arg2):
    with pytest.raises(TypeError):
        smallest_divisible(arg1, arg2)

@pytest.mark.parametrize(
    'arg1, arg2',
    [(1, 0),
     (0, 1),
     (1, -1),
     (-1, 1),
     ])
def test_smallest_divisible_zero_or_less_args(arg1, arg2):
    with pytest.raises(ValueError):
        smallest_divisible(arg1, arg2)

def smallest_divisible_range_low_larger_than_range_high():
    with pytest.raises(ValueError):
        smallest_divisible(2, 1)