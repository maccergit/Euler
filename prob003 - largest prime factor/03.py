#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# SymPy - primes

from sympy import sieve

def gen_factors(limit):
    current = 1
    current_prime = sieve[current]
    while current_prime * current_prime < limit:
        if limit % current_prime == 0:
            yield current_prime
            limit = limit / current_prime
        else:
            current += 1
            current_prime = sieve[current]
    yield limit

def solution(limit):
    return int(max(x for x in gen_factors(limit)))

assert solution(13195) == 29
print(solution(600851475143))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([13195, 600851475143], count, scale)
utils.timing.plot_timing([100000005000, 200000005000, 300000005000, 400000005000, 500000005000, 600000005000, 700000005000, 800000005000, 900000005000, 1000000050000],
                         count, scale, "prob0003.03")