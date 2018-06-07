# coding: utf8
"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Gauss's summation: ∑(multiples of 3) + ∑(multiples of 5) - ∑(multiples of 15) in closed form

python: 1.3 µsec

jython: 4.5 µsec

O(1)
"""

import timeit

def intervalSum(interval, limit):
    lastEement = int((limit - 1) / interval)
    return interval * lastEement * (1 + lastEement) / 2

def getSolution(limit):
    return intervalSum(3, limit) + intervalSum(5, limit) - intervalSum(15, limit)

assert getSolution(10) == 23

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(1000) == 233168
timeProblem(1000)