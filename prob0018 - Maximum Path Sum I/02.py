#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 29, 2024

@author: johnmcalister

Iterative approach from last row to first
'''

sample_data = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

problem_data = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

def get_max(data):
    if len(data) == 1:
        return data[0][0]
    subtree_leaf = [x for x in data[-2]]
    data[-2] = [subtree_leaf[x] + max(data[-1][x], data[-1][x + 1]) for x in range(len(subtree_leaf))]
    return get_max(data[:-1])

def solution(limit):
    return get_max([x for x in current_data[:limit]])

current_data = sample_data
assert solution(1) == 3
assert solution(4) == 23

current_data = problem_data
print(solution(len(problem_data)))

count = 10000
scale = 1000000

import utils.timing
# utils.timing.table_timing([x + 1 for x in range(len(current_data))], count, scale)
utils.timing.plot_timing([x + 1 for x in range(len(current_data))], count, scale, "prob0018.01")