#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 30, 2024

@author: johnmcalister

Direct approach - use calendar library.  Note that the default weekdays for this library are Mon = 0 -> Sun = 6.
'''

import calendar

# Return number of times a month starts on Sunday for a given year
def sundays(year):
    return sum(1 for month in range(1, 13) if calendar.monthrange(year, month)[0] == 6)

assert sundays(1900) == 2
assert sundays(1901) == 2
assert sundays(1902) == 1
assert sundays(1903) == 3
assert sundays(1904) == 1
assert sundays(1905) == 2

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

count = 100
scale = 1000000

import utils.timing
utils.timing.table_timing([1900, 1901, 1902, 1903, 1904, 1905, 2000], count, scale)
utils.timing.plot_timing([x for x in range(1901, 2001)], count, scale, "prob0019.05", ticks=False)