#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# SymPy

from sympy import divisor_count

def triangle(n):
    return int((n + 1) * n / 2)

assert triangle(1) == 1
assert triangle(2) == 3
assert triangle(3) == 6
assert triangle(4) == 10
assert triangle(5) == 15
assert triangle(6) == 21
assert triangle(7) == 28
assert triangle(8) == 36
assert triangle(9) == 45
assert triangle(10) == 55

def solution(limit):
    current = 1
    while divisor_count(triangle(current)) <= limit:
        current += 1
    return triangle(current)

assert solution(5) == 28
print(solution(500))

count = 10
scale = 1000 # msec

import utils.timing
utils.timing.table_timing([10, 500], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500], count, scale)