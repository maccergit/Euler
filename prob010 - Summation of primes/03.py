#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Sieve - same as before, don't accumulate primes in a separate list - just iterate over the keys in the dict that are not flagged.
'''

def solution(limit):
    sieve = {x: True for x in range(2, limit)}
    current = 2
    while (current < limit) :
        if not sieve[current]:
            current += 1
        else:
            for index in range(current * current, limit, current if current == 2 else current + current):
                sieve[index] = False
            current += 1
    return sum(x for x in sieve.keys() if sieve[x])

assert solution(10) == 17
print(solution(2000000))

count = 2
scale = 1000

import utils.timing
utils.timing.table_timing([10, 2000000], count, scale)
utils.timing.plot_timing([500000, 1000000, 1500000, 2000000], count, scale, "prob0010.03")