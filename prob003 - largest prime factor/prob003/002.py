# coding: utf8
"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Use pyprimesieve library to factor number.  Not available in Jython.

9 µsec
"""

import timeit
import pyprimesieve

def getSolution(limit):
    return max(x[0] for x in pyprimesieve.factorize(limit))

assert getSolution(13195) == 29

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(600851475143) == 6857
timeProblem(600851475143)