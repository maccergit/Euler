#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 30, 2024

@author: johnmcalister

Direct approach - WORK IN PROGRESS
'''

# Return number of times a month starts on Sunday for a given year
def sundays(year):
    return 0

# "limit" will be ending year (must be after 1900)
def solution(limit):
    return sum(sundays(x) for x in range(1901, limit + 1))

# Determined by manual inspection of calendar for 1900
assert solution(1901) == (2)
assert solution(1902) == (2 + 1)
assert solution(1903) == (2 + 1 + 3)
assert solution(1904) == (2 + 1 + 3 + 1)
assert solution(1905) == (2 + 1 + 3 + 1 + 2)

print(solution(2000))

count = 1
scale = 1

# import utils.timing
# utils.timing.table_timing([1900, 1901, 1902, 1903, 1904, 1905, 2000], count, scale)
# utils.timing.plot_timing([x for x in range(1901, 2001)], count, scale, "prob0019.01")