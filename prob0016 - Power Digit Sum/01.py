#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 23, 2024

@author: johnmcalister

Direct approach
'''


def solution(limit):
    return sum(int(x) for x in str(2 ** limit))

assert solution(15) == 26
print(solution(1000))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([15, 1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500], count, scale, ticks=False)