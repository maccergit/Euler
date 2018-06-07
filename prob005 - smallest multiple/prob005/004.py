# coding: utf8
"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Use primesieve to factor numbers to get LCM

Python = 18 µsec
"""

import timeit
import pyprimesieve
import operator

def getSolution(limit):
    resultFactors = {x: 0 for x in xrange(1, limit + 1)}
    for x in (pyprimesieve.factorize(x) for x in xrange(2, limit + 1)):
        for prime, power in x:
            if resultFactors[prime] < power:
                resultFactors[prime] = power
    return reduce(operator.mul, (x ** resultFactors[x] for x in resultFactors), 1)

assert getSolution(10) == 2520

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(20) == 232792560
timeProblem(20)