# coding: utf8
"""
Sum square difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Closed form for sum and sum of squares.

Python : .34 µsec
"""

import timeit

def getSolution(limit):
    return ((1 + limit) * limit / 2) ** 2 - (2 * limit + 1) * (limit + 1) * limit / 6

assert getSolution(10) == 2640

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(100) == 25164150
timeProblem(100, 1000000)
