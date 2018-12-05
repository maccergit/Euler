# coding: utf8
"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Sieve - using dict, but stopping short
"""

import timeit

def getSolution(limit):
    sieve = {x: True for x in xrange(2, limit)}
    current = 2
    while (current + current < limit) :
        if not sieve[current]:
            current += 1
        else:
            for index in xrange(current + current, limit, current):
                sieve[index] = False
            current += 1
    return sum(x for x in sieve.keys() if sieve[x])

assert getSolution(10) == 17

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count) + " sec")

print getSolution(100)
print getSolution(1000)
print getSolution(10000)
print getSolution(100000)
print getSolution(1000000)
assert getSolution(2000000) == 142913828922
timeProblem(2000000, 3)
