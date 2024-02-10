#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 22, 2024

@author: johnmcalister

Use NumPy to provide an array that we can iterate over - try to use vector approach
'''

import numpy as np

def solution(limit):
    grid = np.zeros([limit + 1, limit + 1], dtype = object)
    grid[:,limit] = 1
    for y in range(limit - 1, -1, -1):
        grid[:,y] = np.flip(np.cumsum(grid[:,y] + grid[:,y + 1]))
    return grid[0, 0]

assert solution(0) == 1
assert solution(1) == 2
assert solution(2) == 6
print(solution(20))

count = 30
scale = 1000

import utils.timing
utils.timing.table_timing([2, 20], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250], count, scale, ticks = False)