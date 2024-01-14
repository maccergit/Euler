#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Sieve - accumulating list of primes
'''

def solution(limit):
    sieve = {x: True for x in range(2, limit)}
    current = 2
    primes = []
    while (current < limit) :
        if not sieve[current]:
            current += 1
        else:
            for index in range(current + current, limit, current):
                sieve[index] = False
            primes.append(current)
            current += 1
    return sum(primes)

assert solution(10) == 17
print(solution(2000000))

count = 1
scale = 1 # sec

import utils.timing
utils.timing.table_timing([10, 2000000], count, scale)
utils.timing.plot_timing([500000, 1000000, 1500000, 2000000], count, scale)