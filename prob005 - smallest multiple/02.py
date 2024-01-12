#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force - no factoring

NOTE: We know that 2520 is required for 1-10, so any result for limit > 10 will also be a multiple of 2520, so we only check multiples of 2520.
'''

def solution(limit):
    result = 2520
    done = False
    while not done:
        done = True
        for x in range(11, limit + 1):
            if result % x != 0:
                done = False
        if not done:
            result += 2520
    return result

assert solution(10) == 2520
print(solution(20))

count = 10
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 12, 14, 16, 18, 20, 22, 24], count, scale)