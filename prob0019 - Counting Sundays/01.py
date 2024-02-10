#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 30, 2024

@author: johnmcalister

Direct approach
'''

months = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
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

def get_start_next_year(day, year):
    for month in range(1, 13):
        day = (day + months[month])
    if is_leap(year):
        day += 1
    return day % 7

assert get_start_next_year(1, 1900) == 2
assert get_start_next_year(2, 1901) == 3
assert get_start_next_year(3, 1902) == 4
assert get_start_next_year(4, 1903) == 5
assert get_start_next_year(5, 1904) == 0

def count_start_sundays_year(day, year):
    count = 0
    for month in range(1, 13):
        if day == 0:
            count += 1
        day = (day + months[month])
        if month == 2 and is_leap(year):
            day += 1
        day %= 7
    return count

assert count_start_sundays_year(1, 1900) == 2
assert count_start_sundays_year(2, 1901) == 2
assert count_start_sundays_year(3, 1902) == 1
assert count_start_sundays_year(4, 1903) == 3
assert count_start_sundays_year(5, 1904) == 1
assert count_start_sundays_year(0, 1905) == 2

# Return number of times a month starts on Sunday for a given year
def sundays(year):
    # 1 Jan 1990 was a Monday, Sunday = 0
    start_year = 1900
    start_day = 1
    
    current_year = start_year
    current_day = start_day
    while current_year < year:
        current_day = get_start_next_year(current_day, current_year)
        current_year += 1
    return count_start_sundays_year(current_day, year)

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

count = 10
scale = 1000

import utils.timing
utils.timing.table_timing([1900, 1901, 1902, 1903, 1904, 1905, 2000], count, scale)
utils.timing.plot_timing([x for x in range(1901, 2001)], count, scale, ticks=False)