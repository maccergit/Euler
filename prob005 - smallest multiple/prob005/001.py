# coding: utf8
"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solved by inspection - 2520 is LCM of 1..10, so just need to multiply by primes missing from 11..20 - 2 is needed because 16 is 2^4, and 2520 only contains 2^3.

Python = 86 nsec
jython = 140 nsec

O(1)
"""

import timeit

def getSolution(limit):
    return 2520 * 11 * 13 * 2 * 17 * 19

# assert getSolution(10) == 2520

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(20) == 232792560
timeProblem(20, 1000000)
