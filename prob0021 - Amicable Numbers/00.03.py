#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 1, 2024

@author: johnmcalister

run timing tests on fastfactor.gen_divisors
'''

import math
import pyprimesieve
import itertools

def gen_factors(limit):
    factors = pyprimesieve.factorize(limit)
    for x in factors:
        for _ in range(x[1]):
            yield x[0]
            
def gen_divisors(limit):
    s = [*gen_factors(limit)]
    return (y for y in {math.prod(x) for x in itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))})

def solution(limit):
    return [*gen_divisors(limit)]

print(solution(10000))

count = 100
scale = 1000

import utils.timing
utils.timing.table_timing([1000, 10000], count, scale)
utils.timing.plot_timing([1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000], count, scale)