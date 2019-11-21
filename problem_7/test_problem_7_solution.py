import pytest

from project_euler.problem_7.problem_7_solution import nth_prime


def test_nth_prime():
    assert nth_prime(6) == 13


@pytest.mark.parametrize('argument',
                         [-1, 0, ])
def test_nth_prime_n_less_than_one_raising_error(argument):
    with pytest.raises(ValueError):
        nth_prime(argument)
