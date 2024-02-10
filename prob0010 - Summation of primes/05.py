#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Sieve - use NumPy array and vector operations
'''

import numpy as np

def solution(limit):
    sieve = np.ones((limit + 1,), dtype=bool)
    sieve[0] = False
    sieve[1] = False
    current = 2
    while (current < limit) :
        if sieve[current]:
            sieve[current * current::current if current == 2 else current + current] = False
        current += 1
    return sum(x for x in range(len(sieve)) if sieve[x])

assert solution(10) == 17
print(solution(2000000))

count = 4
scale = 1000

import utils.timing
utils.timing.table_timing([10, 2000000], count, scale)
utils.timing.plot_timing([500000, 1000000, 1500000, 2000000], count, scale)