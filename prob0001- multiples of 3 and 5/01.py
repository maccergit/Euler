#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 16, 2020

@author: johnmcalister

Brute force with trial division - sum generated values that are multiple of 3 or 5.
'''

def solution(limit):
    return sum(x for x in range(1, limit) if x % 3 == 0 or x % 5 == 0)

assert solution(10) == 23
print(solution(1000))

count = 100
scale = 1000

import utils.timing
utils.timing.table_timing([10, 1000], count, scale)
utils.timing.plot_timing([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000], count, scale)