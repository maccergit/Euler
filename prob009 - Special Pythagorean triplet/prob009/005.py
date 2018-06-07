# coding: utf8
"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Use Euclid's formula of generating Pythagorean triplets, testing only Pythagorean triplets until
we hit the one that has the correct perimeter.

for p and q, natural numbers that cannot both be odd:

a = 2 * p * q
b = p^2 - q^2
c = p^2 + q^2

140 µsec
"""

import timeit

def getSolution(limit):
    for p in xrange(1, limit / 4 + 2):
        for q in xrange(p % 2 + 1, limit / 4 + 2, 2):
            a = 2 * p * q
            b = p * p - q * q
            if b < 0:
                b = -b
            c = p * p + q * q
            if (a + b + c) == limit:
                return a * b * c
    return 0

assert getSolution(12) == 60

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count* 1000000) + " µsec")

assert getSolution(1000) == 31875000
timeProblem(1000)
