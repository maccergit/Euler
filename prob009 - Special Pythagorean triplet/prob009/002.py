# coding: utf8
"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Substitute c = limit - a - b into the pythagorean equation and solve to get:

b = limit + limit^2 / (2 * (a - limit))

55 µsec
"""

import timeit

def getSolution(limit):
    for a in xrange(1, limit / 2 + 2):
        b = limit + limit * limit / (2 * (a - limit))
        c = limit - a - b
        if a * a + b * b == c * c:
            return a * b * c
    return 0

assert getSolution(12) == 60

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count* 1000000) + " µsec")

assert getSolution(1000) == 31875000
timeProblem(1000)
