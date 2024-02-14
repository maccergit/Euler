#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 13, 2024

@author: johnmcalister

Direct approach
-----
Big problem is we cannot assume it will be 4 digits just because the example is 4 digits.
Must be at least 2 digits to be a sum.
Note that order of digits does not matter - rearrangements produce same powerSum.
For a given number of digits, 100...00 is minimum, and does not provide any reduction in range of possible numbers (power sum is always 1)
-----
Once we have determined a range, there are a couple approaches : 
- iterate over integers, break apart into digits, compute power sum, and then compare with original number.
- iterate over possible digits, compute power sum, and see if result matches number built from those digits (each set of digits can produce several numbers as digits are rearranged).
'''

def powerSums(limit):
    return []

assert powerSums(4) == [1634, 8202, 9474]

def solution(limit):
    return sum(powerSums(limit))

assert solution(4) == 19316

print(solution(5))

# count = 1
# scale = 1

# import utils.timing
# utils.timing.table_timing([5, 100], count, scale)
# utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)
