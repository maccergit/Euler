#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 30, 2024

@author: johnmcalister

Iterative approach from last row to first
'''

current_data = []

with open("0067_triangle.txt") as f:
    for line in f:
        current_data.append([int(x) for x in line.split()])

def get_max(data):
    if len(data) == 1:
        return data[0][0]
    subtree_leaf = [x for x in data[-2]]
    data[-2] = [subtree_leaf[x] + max(data[-1][x], data[-1][x + 1]) for x in range(len(subtree_leaf))]
    return get_max(data[:-1])

def solution(limit):
    return get_max([x for x in current_data[:limit]])

print(solution(len(current_data)))

count = 10
scale = 1000000

import utils.timing
# utils.timing.table_timing([x + 1 for x in range(len(current_data))], count, scale)
utils.timing.plot_timing([x + 1 for x in range(len(current_data))], count, scale, "prob0067.01", ticks = False)