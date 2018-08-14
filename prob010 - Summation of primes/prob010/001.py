# coding: utf8
"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Brute force - ?
"""

import timeit

def nextPrime():
    current = 1
    primes = []
    while True:
        current += 1
        if all(current % prime > 0 for prime in primes):
            primes.append(current)
            yield current

def getSolution(limit):
    nexPrimeGen = nextPrime()
    total = 0
    prime = nexPrimeGen.next()
    while prime < limit:
        total += prime
        prime = nexPrimeGen.next()
    return total

assert getSolution(10) == 17

def timeProblem(probLimit, count = 10000):
    print getSolution(probLimit)
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count) + " sec")

print getSolution(100)
print getSolution(1000)
print getSolution(10000)
print getSolution(100000)
print getSolution(1000000)
# assert getSolution(2000000) == 142913828922
# timeProblem(2000000, 3)
