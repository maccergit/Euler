#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

NOTE:

a + b + c is perimeter, so:

    c = limit - a - b
    c < a + b
    a, b, c > 0
    c > limit / 3 (largest side must be larger than equilateral triangle)

therefore:

    limit - a - b < a + b:

add "a" and "b" to each side to get:

    limit < 2a + 2b

so:

    limit / 2 < a + b

Brute Force
'''

import math

def gen_trip(limit):
    # "c" can range from [c / 3 .. limit], integers only
    for c in range(int(limit / 3 + 1), limit + 1):
        # "b" can range from [a + 1 .. a + b]
        for b in range(int((limit - c) / 2) + 1, limit - c - 1):
            # we have trial values for "b" and "c", so we also have trial value for "a"
            yield [limit - b - c, b, c]

def solution(limit):
    # generate trial triplets, see if any are pythagorean, and return first one found
    return math.prod([x for x in gen_trip(limit) if x[0] * x[0] + x[1] * x[1] == x[2] * x[2]][0])

assert solution(12) == 60
print(solution(1000))

count = 100
scale = 1000 # msec

import utils.timing
utils.timing.table_timing([12, 1000], count, scale)
# TODO - the solution is not robust for all limit values, and fails on the list below.
# utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)