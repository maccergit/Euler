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
        self.nextStart = (day + self.days) % 7
    
    def assertDays(self, expectedDays):
        assert self.days == expectedDays
    
    def assertNextStart(self, expectedStart):
        assert self.nextStart == expectedStart

month1 = Month(1, 1)
month2 = Month(2, 4)
month3 = Month(2, 4, True)

month1.assertDays(31)
month1.assertNextStart(4)
month2.assertDays(28)
month2.assertNextStart(4)
month3.assertDays(29)
month3.assertNextStart(5)

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
            self.months[x] = Month(x, self.months[x - 1].nextStart, self.isLeap)
    
    def nextStart(self):
        return((self.months[1].day + (366 if self.isLeap else 365)) % 7)
    
    def sundays(self):
        return [self.months[x].day for x in self.months].count(0)
    
    def assertIsLeap(self):
        assert self.isLeap
    
    def assertIsNotLeap(self):
        assert not self.isLeap
    
    def assertNextStart(self, expectedStart):
        assert self.nextStart() == expectedStart
    
    def assertSundays(self, expectedSundays):
        assert self.sundays() == expectedSundays

year1900 = Year(1900)
year1901 = Year(1901)
year1902 = Year(1902)
year1903 = Year(1903)
year1904 = Year(1904)
year1905 = Year(1905)
year2000 = Year(2000)
year2023 = Year(2023)
year2024 = Year(2024)

year2000.assertIsLeap()
year2024.assertIsLeap()
year2023.assertIsNotLeap()
year1900.assertIsNotLeap()

year1900.assertNextStart(2)
year1901.assertNextStart(3)
year1902.assertNextStart(4)
year1903.assertNextStart(5)
year1904.assertNextStart(0)

year1900.assertSundays(2)
year1901.assertSundays(2)
year1902.assertSundays(1)
year1903.assertSundays(3)
year1904.assertSundays(1)
year1905.assertSundays(2)

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
utils.timing.plot_timing([x for x in range(1901, 2001)], count, scale, "prob0019.03", ticks=False)
