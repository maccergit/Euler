# coding: utf8
"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Use Euclid's improved algorithm to get GCD, and then use GCD to get LCM

Python = 8 µsec
"""

import timeit

def gcd(a, b):
    if a < b:
        a, b = b, a
    a = a % b
    if a == 0:
        return b
    return gcd(b, a)

def getSolution(limit):
    current = 1
    for x in xrange(2, limit + 1):
        current = current * x / gcd(current, x)
    return current

assert getSolution(10) == 2520

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(20) == 232792560
timeProblem(20, 100000)