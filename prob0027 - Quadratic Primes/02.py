#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 12, 2024

@author: johnmcalister

Direct approach - iterate through a and b, finding number of primes each generates.  Primality test is factoring to see if any factors > 1 exist.

Use fastfactor library as drop-in replacement for factor library.
'''

import utils.fastfactor as factor

def numPrimes(a, b):
    n = 0
    p = 1
    factors = [0]
    while len(factors) == 1:
        n += 1
        p = n * n + a * n + b
        factors = [*factor.gen_factors(p)]
    return n

# assert numPrimes(1, 41) == 40
# assert numPrimes(-79, 1601) == 80

def solution(limit):
    maxResult = -1
    for a in range(1-limit, limit):
        for b in range(-limit, limit + 1):
            result = numPrimes(a, b)
            if result > maxResult:
                maxResult = result
                maxAB = (a, b)
    return maxAB[0] * maxAB[1]

print(solution(1000))

count = 1
scale = 1

import utils.timing
utils.timing.table_timing([40, 1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500], count, scale)
