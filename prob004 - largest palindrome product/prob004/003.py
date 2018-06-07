# coding: utf8
"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Brute force - use generators to reduce memory usage + assume j < i to avoid redundant elements (201 * 304 and 304 * 201 : both yield same number)

.46 sec

O(10 ^ 2n)
"""

import timeit

def nextElem(minval, maxval):
    for i in xrange(maxval, minval, -1):
        for j in xrange(i, minval, -1):
            if str(i * j) == str(i * j)[::-1]:
                yield i * j

def getSolution(limit):
    minval = int('9' * (limit - 1))
    maxval = int('9' * limit)
    return max(nextElem(minval, maxval))

assert getSolution(2) == 9009

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count * 1000) + " msec")

assert getSolution(3) == 906609
timeProblem(3, 10)