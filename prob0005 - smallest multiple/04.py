#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force factoring
'''

import utils.factor
import math

def solution(digits):
    factors = {}
    for x in ([y for y in utils.factor.gen_factors(x)] for x in range(2, digits + 1)):
        for y in {z for z in x}:
            factor_count = x.count(y)
            if y not in factors or factor_count > factors[y]:
                factors[y] = factor_count
    return math.prod(x ** factors[x] for x in factors)

assert solution(10) == 2520
print(solution(20))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale, "prob0005.04")

# Adjust count/scale values to make large limits run in reasonable time and display in appropriate units
# count = 10
# scale = 1000
# utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale, "prob0005.04")