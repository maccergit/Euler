#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use NumPy to get the LCM
'''

# numpy

from numpy import lcm

def solution(digits):
    return lcm.reduce(range(2, digits + 1))

assert solution(10) == 2520
print(solution(20))

count = 100000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
# utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale, "prob0005.06")

# Adjust count/scale so larger range runs in reasonable time with appropriate units
# count = 1000
# scale = 1000
# utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale, "NumPy")