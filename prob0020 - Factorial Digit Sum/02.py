#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 1, 2024

@author: johnmcalister

Direct approach - but use math.factorial() instead of generator comprehension
'''

import math

def solution(limit):
    return sum(int(x) for x in str(math.factorial(limit)))

assert solution(10) == (27)

print(solution(100))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 100], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale, "prob0020.01")