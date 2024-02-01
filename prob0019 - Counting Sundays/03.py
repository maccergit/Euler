#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 30, 2024

@author: johnmcalister

Direct approach - skip by years to current year, then iterate over months.
'''

class Month:
    # Class variable to hold this map to avoid polluting the global namespace
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
    
    def __init__(self, month, day, leap = False):
        self.month = month
        self.day = day;
        self.leap = leap
        if month == 2 and leap:
            self.days = Month.months[2] + 1
        else:
            self.days = Month.months[month]
    
    def nextStart(self):
        return((self.day + self.days) % 7)

month1 = Month(1, 1)
month2 = Month(2, 4)
month3 = Month(2, 4, True)

assert month1.days == 31
assert month1.nextStart() == 4
assert month2.days == 28
assert month2.nextStart() == 4
assert month3.days == 29
assert month3.nextStart() == 5

class Year:
    # Python does not have method overloading, so use the easy way of using an optional parm
    def __init__(self, year, day = -1):
        self.year = year
        self.isLeap = (year % 400 == 0) or (year % 100 > 0 and year % 4 == 0)
        if day < 0:
            day = 1
            myYear = Year(1900, 1)
            while myYear.year < year:
                day = myYear.nextStart()
                myYear = Year(myYear.year + 1, myYear.nextStart())
        self.months = {1 : Month(1, day, self.isLeap)}
        for x in range(2, 13):
            self.months[x] = Month(x, self.months[x - 1].nextStart(), self.isLeap)
    
    def nextStart(self):
        return((self.months[1].day + (366 if self.isLeap else 365)) % 7)
    
    def sundays(self):
        return [self.months[x].day for x in self.months].count(0)

year1900 = Year(1900)
year1901 = Year(1901)
year1902 = Year(1902)
year1903 = Year(1903)
year1904 = Year(1904)
year1905 = Year(1905)
year2000 = Year(2000)
year2023 = Year(2023)
year2024 = Year(2024)

assert year2000.isLeap
assert year2024.isLeap
assert not year2023.isLeap
assert not year1900.isLeap

assert year1900.nextStart() == 2
assert year1901.nextStart() == 3
assert year1902.nextStart() == 4
assert year1903.nextStart() == 5
assert year1904.nextStart() == 0

assert year1900.sundays() == 2
assert year1901.sundays() == 2
assert year1902.sundays() == 1
assert year1903.sundays() == 3
assert year1904.sundays() == 1
assert year1905.sundays() == 2

# "limit" will be ending year (must be after 1900)
def solution(limit):
    return sum(Year(x).sundays() for x in range(1901, limit + 1))

# Determined by manual inspection of calendar for 1900
assert solution(1901) == (2)
assert solution(1902) == (2 + 1)
assert solution(1903) == (2 + 1 + 3)
assert solution(1904) == (2 + 1 + 3 + 1)
assert solution(1905) == (2 + 1 + 3 + 1 + 2)

print(solution(2000))

count = 2
scale = 1000

import utils.timing
utils.timing.table_timing([1900, 1901, 1902, 1903, 1904, 1905, 2000], count, scale)
utils.timing.plot_timing([x for x in range(1901, 2001)], count, scale, "prob0019.02", ticks=False)
