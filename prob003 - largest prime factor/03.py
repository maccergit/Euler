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

count = 1000
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([101, 4000001], count, scale)
utils.timing.plot_timing([10000001, 20000003, 30000001, 40000001, 50000003, 60000001, 70000001, 80000003, 90000001, 100000001], count, scale)