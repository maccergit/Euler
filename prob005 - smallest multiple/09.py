#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use library to get GCD, and then use GCD to get LCM
'''

import math

def solution(limit):
    result = 1
    for x in range(2, limit + 1):
        result = x * result / math.gcd(x, int(result))
    return int(result)

assert solution(10) == 2520
print(solution(20))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale, "prob0005.08")