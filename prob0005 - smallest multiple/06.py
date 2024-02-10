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