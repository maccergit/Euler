#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

SymPy
'''

from sympy import primerange

def solution(limit):
    return sum(primerange(2, limit))

assert solution(10) == 17
print(solution(2000000))

count = 1
scale = 1 # sec

import utils.timing
utils.timing.table_timing([10, 2000000], count, scale)
utils.timing.plot_timing([500000, 1000000, 1500000, 2000000], count, scale)