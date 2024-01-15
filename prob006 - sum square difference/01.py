#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force
'''

def solution(limit):
    return sum(x for x in range(limit + 1)) ** 2 - sum(x * x for x in range(limit + 1))

assert solution(10) == 2640
print(solution(100))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 100], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale, "prob0006.01")