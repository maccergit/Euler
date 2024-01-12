#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# Brute Force

import util.prod

def gen_trip(limit):
    for c in range(limit / 3 + 1, limit + 1):
        for b in range((limit - c) / 2 + 1, limit - c - 1):
            yield [limit - b - c, b, c]

def solution(limit):
    return util.prod.prod([x for x in gen_trip(limit) if x[0] * x[0] + x[1] * x[1] == x[2] * x[2]][0])

assert solution(12) == 60
print solution(1000)

count = 100
scale = 1000 # msec

import util.timing
util.timing.table_timing([12, 1000], count, scale)
# util.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)