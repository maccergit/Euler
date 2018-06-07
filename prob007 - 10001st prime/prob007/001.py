# coding: utf8
"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Brute force - 2.5-3.0 sec

Note - using only every other integer above 3 has no impact on time

Note - can't seem to figure out a sieve approach
"""

import timeit

def nextPrime():
    current = 1
    primes = []
    while True:
        current += 1
        for prime in primes:
            if current % prime == 0:
                break
        else:
            primes.append(current)
            yield current

def getSolution(limit):
    nexPrimeGen = nextPrime()
    for _ in xrange(limit):
        value = nexPrimeGen.next()
    return value

assert getSolution(6) == 13

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count) + " sec")

assert getSolution(10001) == 104743
timeProblem(10001, 3)
