#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 22, 2024

@author: johnmcalister

Direct recursion
'''

def paths(x, y, limit):
    if x == limit and y == limit:
        return 1
    if y == limit:
        return paths(x + 1, y, limit)
    if x == limit:
        return paths(x, y + 1, limit)
    return paths(x, y + 1, limit) + paths(x + 1, y, limit)

def solution(limit):
    return paths(0, 0, limit)

assert solution(0) == 1
assert solution(1) == 2
assert solution(2) == 6
# print(solution(20))

count = 10
scale = 1000

import utils.timing
# utils.timing.table_timing([2, 20], count, scale)
utils.timing.plot_timing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], count, scale, "prob0015.01")