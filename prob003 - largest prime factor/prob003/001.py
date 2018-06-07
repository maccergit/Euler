# coding: utf8
"""
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Brute force - check all numbers up to square root of number.
#
# python:
#     11        : 0.9 µsec
#     101       : 1.75 µsec
#     1001      : 1.4 µsec
#     10001     : 10 µsec
#     100001    : 12.5 µsec
#     1000001   : 13 µsec
#     10000001  : 117 µsec
#     100000001 : 290 µsec
#     1000000001 : 30 µsec
#     1000000003 : 4400 µsec
#     600851475143 : 180 µsec
#
# jython:
#     11        : 3.7 µsec
#     101       : 5 µsec
#     1001      : 7 µsec
#     10001     : 12 µsec
#     100001    : 13.5 µsec
#     1000001   : 13.5 µsec
#     10000001  : 77 µsec
#     100000001 : 178 µsec
#     1000000001 : 28 µsec
#     1000000003 : 40 µsec
#     600851475143 : 360 µsec
#
# O(log n) - highly dependent on data properties
"""

import timeit

def factors(limit):
    factor = 2
    while factor * factor < limit + 1:
        if limit % factor == 0:
            yield factor
            limit = limit / factor
        else:
            factor += 1
    yield limit

def getSolution(limit):
    return max(x for x in factors(limit))

assert getSolution(13195) == 29

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000000) + " µsec")

assert getSolution(600851475143) == 6857
timeProblem(600851475143)