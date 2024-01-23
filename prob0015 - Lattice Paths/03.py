#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 22, 2024

@author: johnmcalister

Use NumPy to provide an array that we can iterate over
'''

import numpy as np

def solution(limit):
    grid = np.empty([limit + 1, limit + 1], dtype = np.ulonglong)
    for y in range(limit, -1, -1):
        for x in range(limit, -1, -1):
            if x == limit or y == limit:
                grid[x, y] = 1
            else:
                grid[x, y] = grid[x, y + 1] + grid[x + 1, y]
    return grid[0, 0]

assert solution(0) == 1
assert solution(1) == 2
assert solution(2) == 6
print(solution(20))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([2, 20], count, scale)
# utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200], count, scale, "prob0015.03", ticks = False)
utils.timing.plot_timing([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], count, scale, "prob0015.03")