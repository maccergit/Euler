# coding: utf8
"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Brute force

Python = 91 msec
"""

import timeit

def getSolution(limit):
    result = 2520
    done = False
    while not done:
        done = True
        for x in xrange(11, limit + 1):
            if result % x != 0:
                done = False
        if not done:
            result += 2520
    return result

assert getSolution(10) == 2520

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000) + " msec")

assert getSolution(20) == 232792560
timeProblem(20, 100)