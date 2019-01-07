# project_euler

[![Build Status](https://travis-ci.org/toonarmycaptain/project_euler.svg?branch=master)](https://travis-ci.org/toonarmycaptain/project_euler)
[![Coverage Status](https://coveralls.io/repos/github/toonarmycaptain/project_euler/badge.svg?branch=master)](https://coveralls.io/github/toonarmycaptain/project_euler?branch=master)
[![Updates](https://pyup.io/repos/github/toonarmycaptain/project_euler/shield.svg)](https://pyup.io/repos/github/toonarmycaptain/project_euler/)
[![Python 3](https://pyup.io/repos/github/toonarmycaptain/project_euler/python-3-shield.svg)](https://pyup.io/repos/github/toonarmycaptain/project_euler/)
Solutions to non-current Project Euler problems. 

This is my repo of my solutions to Project Euler, complete with tests. 

Some problems I will solve with an algorithmic solution that demonstrates an algorithm and an equivalent or more optimised/one-liner solution eg:


**Problem 1 - sum of numbers divisible by 3 or 5:**

Algorithmic solution:
```
def sum_multiples(multiples: tuple, minmax: tuple):
    total = 0
    for i in range(minmax[0], minmax[1]+1):
        for j in multiples:
        if i%j == 0:
            total += i
            break  # break out of inner for loop after first multiple is matched
    return total
```
More efficient one liner solution: 
```
def efficient_sum_multiples_3_or_5(minmax):
    return sum([i for i in range(min, max+1) if i%3 == 0 o r i%5 == 0])
```
