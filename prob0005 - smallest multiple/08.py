#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use Euclid's improved algorithm to get GCD, and then use GCD to get LCM
'''

def gcd(a, b):
    a = a % b
    if a == 0:
        return b
    return gcd(b, a)

def solution(limit):
    current = 1
    for x in range(2, limit + 1):
        current = current * x // gcd(current, x)
    return current

assert solution(10) == 2520
print(solution(20))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 20], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)