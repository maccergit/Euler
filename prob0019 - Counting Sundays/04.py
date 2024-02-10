#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 30, 2024

@author: johnmcalister

Direct approach - use Gauss's algorithm for computing day of week.
'''

# offsets for each month - first value is for common years, second value is for leap years
months = {
    1 : (0, 0),
    2 : (3, 3),
    3 : (3, 4),
    4 : (6, 0),
    5 : (1, 2),
    6 : (4, 5),
    7 : (6, 0),
    8 : (2, 3),
    9 : (5, 6),
    10 : (0, 1),
    11 : (3, 4),
    12 : (5, 6)
}

def is_leap(year):
    # If divisible by 400, then it trumps everything and is a leap year.
    # Otherwise, if divisible by 100, then not a leap year.
    # Otherwise, if divisible by 4, it's a leap year.
    return (year % 400 == 0) or (year % 100 > 0 and year % 4 == 0)

assert is_leap(2000)
assert is_leap(2024)
assert not is_leap(2023)
assert not is_leap(1900)

def get_start_of_month(month, year):
    offset = months[month][1] if is_leap(year) else months[month][0]
    return (1 + offset + 5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 * ((year - 1) % 400)) % 7

# Return number of times a month starts on Sunday for a given year
def sundays(year):
    return sum(1 for month in range(1, 13) if get_start_of_month(month, year) == 0)

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
utils.timing.plot_timing([x for x in range(1901, 2001)], count, scale, ticks=False)