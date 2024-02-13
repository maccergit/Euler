#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 12, 2024

@author: johnmcalister

Direct approach using NumPy
'''

import numpy as np

def initData(limit):
    data = np.zeros((limit, limit))
    start = limit //2
    x = start
    y = start
    dx = 0
    dy = 0
    for elem in range(1, limit * limit + 1):
        x += dx
        y += dy
        data[x, y] = elem
        # we are somewhere on ascending spiral
        if x == y:
            # we are on upper, right and need to start new layer
            if x>= start:
                x += 1
                y += 1
                dx = 0
                dy = -1
            else:
                # we are on lower, left diagonal and need to move upwards
                dx = 0
                dy = 1
        # we are somewhere on descending diagonal
        elif x + y == limit - 1:
            # we are on lower, right and need to move left
            if x > start:
                dx = -1
                dy = 0
            # we are on upper, left and need to move right
            else:
                dx = 1
                dy = 0
    return data

def solution(limit):
    data = initData(limit)
    total = 0
    for index in range(0, limit):
        total += data[index, index]
        total += data[index, limit - index - 1]
    # central element gets double counted, and is always 1
    total -= 1
    return total

assert solution(5) == 101

print(solution(1001))

count = 5
scale = 1000

import utils.timing
utils.timing.table_timing([5, 1001], count, scale)
utils.timing.plot_timing([101, 201, 301, 401, 501, 601, 701, 801, 901, 1001], count, scale)
