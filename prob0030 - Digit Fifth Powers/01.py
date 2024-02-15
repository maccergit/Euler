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
11...11 for any power always yields a sum equal to number of digits, but number is 1 + 10 + 100..., which is always larger - so lower limit is now all ones.
A 2 and then all 0 is more interesting - depending on the power, the 2 can eventually cause the power sum to get larger than the number.
However, smallest number with 2 is a leading 1 and trailing 2, with 0 in between as needed.  Foe any number of digits, this is the lowest number in the range to check.
For any given power, all 9 will yield powersum of number of digits * 9^p, but as number of digits grows, base number increase by powers of 10 - so will eventually get larger than powersum.
  This is the max digits for any number in the range.
-----
Once we have determined a range, there are a couple approaches : 
- iterate over integers, break apart into digits, compute power sum, and then compare with original number.
- iterate over possible digits, compute power sum, and see if result matches number built from those digits (each set of digits can produce several numbers as digits are rearranged).
- Construct equation based on digits : d0 + 10 * d1 + 100 * d2 + ... = d0^p + d1^p + d2^p + ..., 0 <= d0, d1, d2, ... <= 9 : since these are constrained to be integers, these are diophantine.
  However, it's not a form that the diophantine solver can recognize.
'''

def getUpperLimit(limit):
    digits = 2
    while (digits * 9 ** limit) > int("9" * digits):
        digits += 1
    return digits

def powerSums(limit):
    retval = []
    for digits in range(2, getUpperLimit(limit) + 1):
        for x in range(int("1" + "0" * (digits - 2) + "2"), int("9" * digits) + 1):
            if x == sum(int(y) ** limit for y in str(x)):
                retval.append(x)
    return retval

assert powerSums(4) == [1634, 8208, 9474]

def solution(limit):
    return sum(powerSums(limit))

assert solution(4) == 19316

print(solution(5))

count = 1
scale = 1

import utils.timing
utils.timing.table_timing([4, 5], count, scale)
utils.timing.plot_timing([2, 3, 4, 5, 6], count, scale)
