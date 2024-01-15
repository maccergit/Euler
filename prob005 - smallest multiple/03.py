#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force - no factoring, but adjust checked values to reflect LCM found so far, instead of fixed at 2520.
'''

def lcm(limit, oldlcm):
    result = oldlcm
    done = False
    while not done:
        done = True
        for x in range(1, limit + 1):
            if result % x != 0:
                done = False
        if not done:
            result += oldlcm
    return result

def solution(limit):
    result = 1
    for x in range(1, limit + 1):
        result = lcm(x, result)
    return result

assert solution(10) == 2520
print(solution(20))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], count, scale, "prob0005.03")