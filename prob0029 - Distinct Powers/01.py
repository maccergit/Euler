#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 13, 2024

@author: johnmcalister

Direct approach
'''

def powers(limit):
    return {a ** b for a in range(2, limit + 1) for b in range(2, limit + 1)}

assert powers(5) == {4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125}

def solution(limit):
    return len(powers(limit))

assert solution(5) == 15

print(solution(100))

count = 100
scale = 1000

import utils.timing
utils.timing.table_timing([5, 100], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)
