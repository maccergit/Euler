# coding: utf8
"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

pyprimesieve

600 µsec
"""

import timeit
import pyprimesieve

def getSolution(limit):
    return pyprimesieve.primes_sum(limit)

assert getSolution(10) == 17

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(2000000) == 142913828922
timeProblem(2000000)
