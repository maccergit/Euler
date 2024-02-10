#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# SymPy - factor

from sympy import primefactors

def solution(limit):
    return max(primefactors(limit))

assert solution(13195) == 29
print(solution(600851475143))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([13195, 600851475143], count, scale)
utils.timing.plot_timing([100000005000, 200000005000, 300000005000, 400000005000, 500000005000, 600000005000, 700000005000, 800000005000, 900000005000, 1000000050000],
                         count, scale)