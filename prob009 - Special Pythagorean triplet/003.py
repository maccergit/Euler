#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Substitute "c = limit - a - b" into the pythagorean equation and solve to get:

    b = limit + limit² / (2 * (a - limit))
'''

def solution(limit):
    for a in range(1, int(limit / 2) + 2):
        # NOTE: the equation can return non-integer values even though "a" and "c" are integers, so truncate to integer before trial test.
        b = int(limit + limit * limit / (2 * (a - limit)))
        c = limit - a - b
        if a * a + b * b == c * c:
            return a * b * c
    return 0

assert solution(12) == 60
print(solution(1000))

count = 1000
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([12, 1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)