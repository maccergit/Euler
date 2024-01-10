#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 18, 2020

@author: johnmcalister

Use summation formula to avoid brute force.  Summation formula is adjusted for skip value, but still needs adjust to avoid double addition of multiples of both values.
Gauss's summation: ∑(multiples of 3) + ∑(multiples of 5) - ∑(multiples of 15) in closed form
'''

# Compute sum[n..end), but only for multiples of "n".  Do this by finding sum[1..end // n), and then multiply by "n" to get n, 2n, 3n, ...
def sumRange(n, end):
    new_end = (end - 1) // n # Adjust because range is open on right - this is all values < end, not ≤ end
    return new_end * (new_end + 1) * n / 2

def solution(limit):
    return sumRange(3, limit) + sumRange(5, limit) - sumRange(15, limit)

assert solution(10) == 23
print(solution(1000))

count = 1000000
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([1000, 100000], count, scale)
utils.timing.plot_timing([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000], count, scale)