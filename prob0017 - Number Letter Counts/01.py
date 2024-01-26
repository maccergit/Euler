#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 25, 2024

@author: johnmcalister
'''

# Compute the number of digits in the text version of a value
# TODO - implement this - just a placeholder right now
def digits(value):
    return 1

assert digits(1) == 3
assert digits(2) == 3
assert digits(3) == 5
assert digits(4) == 4
assert digits(5) == 4
assert digits(342) == 23
assert digits(115) == 20

def solution(limit):
    return sum(digits(x + 1) for x in range(limit))

assert solution(5) == 19
print(solution(1000))

count = 1
scale = 1

# mport utils.timing
# utils.timing.table_timing([15, 1000], count, scale)
# utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500], count, scale, "prob0017.01")