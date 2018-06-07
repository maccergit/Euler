# coding: utf8
"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

pyprimesieve - 60 µsec
"""

import timeit
import pyprimesieve

def getSolution(limit):
    return pyprimesieve.primes_nth(limit)

assert getSolution(6) == 13

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(10001) == 104743
timeProblem(10001)
