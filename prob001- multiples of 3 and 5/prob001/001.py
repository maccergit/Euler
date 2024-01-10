# coding: utf8
"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Brute force - sum generated values that are multiple of 3 or 5.

python:
    10    : 1.7 µsec
    100   : 12 µsec
    1000  : 114 µsec
    10000 : 1140 µsec

jython:
    10    : 2.5 µsec
    100   : 11 µsec
    1000  : 81 µsec
    10000 : 780 µsec

O(n)
"""

import timeit

def getSolution(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

assert getSolution(10) == 23

def timeProblem(probLimit, count = 10000):
    print(getSolution(probLimit))
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(1000) == 233168
timeProblem(1000)