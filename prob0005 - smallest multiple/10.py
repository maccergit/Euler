#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use math.lcm() to get the LCM - since Python 3.9
'''

from math import lcm

def solution(digits):
    return lcm(*range(2, digits + 1))

assert solution(10) == 2520
print(solution(20))

count = 100000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale, "prob0005.10")

# Adjust count/scale to allow larger limits to run in reasonable time with appropriate units
# count = 100
# scale = 1000
# utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale, "math.lcm()")