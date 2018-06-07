# coding: utf8
"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Use primesieve to generate primes, and then compute largest powers of primes to get LCM

Python = 8 µsec
"""

import timeit
import pyprimesieve

def getSolution(limit):
    result = 1
    for prime in pyprimesieve.primes(limit):
        power = 1
        while prime ** (power + 1) <= limit:
            power += 1
        result *= prime ** power
    return result

assert getSolution(10) == 2520

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(20) == 232792560
timeProblem(20, 1000000)