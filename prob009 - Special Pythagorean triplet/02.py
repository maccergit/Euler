#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Same as brute force, but include:

a ≠ b
of a and b, one must be odd and the other must be even
'''

def solution(limit):
    for a in range(1, limit // 2 + 2):
        # a can be odd or even, but b cannot be the same, and must always be opposite even-ness of a.
        for b in range(a + 1, limit // 2 + 2, 2):
            c = limit - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return 0

assert solution(12) == 60
print(solution(1000))

count = 100
scale = 1000

import utils.timing
utils.timing.table_timing([12, 1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale, "prob0009.02")