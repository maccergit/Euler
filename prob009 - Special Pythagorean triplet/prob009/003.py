# coding: utf8
"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

TODO - 2 - Matrix multiplication - see wikipedia "Tree of primitive Pythagorean triples"

TODO - 3 - Dickson's method, when s and t are coprime - see wikipedia "Formulas for generating Pythagorean triples", "Dickson's method"

TODO - 4 - Diophantine solver - try different diophantine approaches for each technique.

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
