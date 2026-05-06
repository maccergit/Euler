#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
'''

# primesieve - stream primes lazily via Iterator, stopping as soon as the
# remaining residue is fully factored.  Much faster than bulk-generating all
# primes up to sqrt(limit) up front - especially on composites where small
# factors peel off quickly.

import primesieve

def solution(limit):
    factors = []
    it = primesieve.Iterator()
    p = it.next_prime()
    while p * p <= limit:
        while limit % p == 0:
            factors.append(p)
            limit //= p
        if limit == 1:
            break
        p = it.next_prime()
    if limit > 1:
        factors.append(limit)
    return max(factors)

assert solution(13195) == 29
assert solution(36) == 3
print(solution(600851475143))

count = 100000
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([13195, 600851475143], count, scale)
utils.timing.plot_timing([100000005000, 200000005000, 300000005000, 400000005000, 500000005000, 600000005000, 700000005000, 800000005000, 900000005000, 1000000050000],
                         count, scale)
