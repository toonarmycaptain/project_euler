from project_euler.problem_2.problem_2_solution import sum_even_fibonacci_numbers

def test_sum_even_fibonacci_numbers():
    fib_to_90 = [i for i in (1, 2, 3, 5, 8, 13, 21, 34, 55, 89) if not i%2]
    assert sum(fib_to_90) == sum_even_fibonacci_numbers(90)
