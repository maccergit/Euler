#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 1, 2024

@author: johnmcalister

Direct approach
'''

def isAmicable(x):
    return False

assert isAmicable(220)
assert isAmicable(284)

def solution(limit):
    return sum(x for x in range(limit) if isAmicable(x))

print(solution(10000))

# count = 1000
# scale = 1000000

# import utils.timing
# utils.timing.table_timing([10, 100], count, scale)
# utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale, "prob0020.01")