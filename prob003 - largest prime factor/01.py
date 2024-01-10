#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force
'''

import itertools

# Generate primes up to sqrt(limit)
def gen_prime(limit):
    sieve = list(itertools.takewhile(lambda x: x * x <= limit, range(2, limit)))
    while sieve:
        current = sieve[0]
        yield current
        for (i, x) in enumerate(sieve):
            if x % current == 0:
                del sieve[i]
        # sieve = [x for x in sieve if x % sieve[0] != 0]

# Returns smallest prime factor of a value
def get_factor(limit, primes):
    for val in primes:
        if limit % val == 0:
            return val
        if val * val > limit:
            break
    return limit

def solution(limit):
    primes = [x for x in gen_prime(limit)]
    current = get_factor(limit, primes)
    while current != limit:
        limit = limit / current
        current = get_factor(limit, primes)
    return int(limit)

assert solution(13195) == 29
# print(solution(600851475143))

count = 100
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([101, 4000001], count, scale)
utils.timing.plot_timing([10000001, 20000003, 30000001, 40000001, 50000003, 60000001, 70000001, 80000003, 90000001, 100000001], count, scale)