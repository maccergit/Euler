# coding: utf8
"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Note that a + b + c is perimeter, so:
c = limit - a - b
c < a + b
a, b, c > 0

therefore:

limit - a - b < a + b

so:

limit / 2 < a + b

Same as brute force, but include:

a ≠ b
of a and b, one must be odd and the other must be even

6 msec
"""

import timeit

def getSolution(limit):
    for a in xrange(1, limit / 2 + 2):
        # a can be odd or even, but b cannot be the same, and must always be opposite even-ness of a.
        for b in xrange(a + 1, limit / 2 + 2, 2):
            c = limit - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return 0

assert getSolution(12) == 60

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count* 1000) + " msec")

assert getSolution(1000) == 31875000
timeProblem(1000, 1000)
