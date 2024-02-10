#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force
'''

def is_palindrome(x):
    xs = str(x)
    xsr = xs[::-1]
    return xs == xsr

def solution(digits):
    values = range(int('1' + '0' * (digits - 1)), int('9' * digits) + 1)
    return max(z for z in (x * y for x in values for y in values if y >= x and (x % 11 == 0 or y % 11 == 0)) if is_palindrome(z))

assert solution(2) == 9009
print(solution(3))

count = 5
scale = 1000 # msec

import utils.timing
utils.timing.table_timing([2, 3, 4], count, scale)
utils.timing.plot_timing([2, 3, 4], count, scale, "prob0004.01")