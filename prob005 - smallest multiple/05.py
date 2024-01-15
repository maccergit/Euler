#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use SymPy to get the LCM.
'''

from sympy.core.numbers import ilcm

def solution(digits):
    return ilcm(*range(2, digits + 1))

assert solution(10) == 2520
print(solution(20))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale, "prob0005.05")