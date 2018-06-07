# coding: utf8
"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Brute force using rolling step size of previous LCM values

Python = 104 µsec
"""

import timeit

def lcm(limit, oldlcm):
    result = oldlcm
    done = False
    while not done:
        done = True
        for x in xrange(1, limit + 1):
            if result % x != 0:
                done = False
        if not done:
            result += oldlcm
    return result

def getSolution(limit):
    result = 1
    for x in xrange(1, limit + 1):
        result = lcm(x, result)
    return result

assert getSolution(10) == 2520

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(20) == 232792560
timeProblem(20)
