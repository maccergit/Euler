#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 12, 2024

@author: johnmcalister

Use formula for computing values of diagonal elements
'''

def solution(limit):
    total = 1
    elem = 1
    for layer in range(1, (limit - 1) // 2 + 1):
        # repeat for all 4 corners
        for _ in range(4):
            elem += 2 * layer
            total += elem
    return total

assert solution(5) == 101

print(solution(1001))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([5, 1001], count, scale)
utils.timing.plot_timing([101, 201, 301, 401, 501, 601, 701, 801, 901, 1001], count, scale)
