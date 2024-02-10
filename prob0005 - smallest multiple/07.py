#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use pyprimesieve to factor
'''

# pyprimesieve

from pyprimesieve import factorize
import math

def solution(digits):
    factors = {}
    
    for factorization in ([y for y in factorize(x)] for x in range(2, digits + 1)):
        for fact in factorization:
            if fact[0] not in factors or fact[1] > factors[fact[0]]:
                factors[fact[0]] = fact[1]
    return math.prod(x ** factors[x] for x in factors)

assert solution(10) == 2520
print(solution(20))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)