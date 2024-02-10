#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 22, 2024

@author: johnmcalister

Use binomial formula, using math combinatoric functions
'''

import math

def solution(limit):
    return math.comb(2 * limit, limit)

assert solution(0) == 1
assert solution(1) == 2
assert solution(2) == 6
print(solution(20))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([2, 20], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)