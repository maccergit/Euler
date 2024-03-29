#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 1, 2024

@author: johnmcalister

Use utils.factor version of calulating sum of divisors - uses the product of (prime^(power + 1) - 1)/(prime - 1) for each prime factor to get sum - don't find every divisor.

NOTE: Again, utils.factor.sumDivisors() generates all divisors, not just proper divisors - so we need to remove the number being factored from the sum.
'''

import utils.factor as factor

assert factor.sumDivisors(220) - 220 == 284
assert factor.sumDivisors(284) - 284 == 220

def isAmicable(x):
    divSum = factor.sumDivisors(x) - x
    return x == factor.sumDivisors(divSum) - divSum and x != divSum

assert isAmicable(220)
assert isAmicable(284)

def solution(limit):
    return sum(x for x in range(limit) if isAmicable(x))

print(solution(10000))

count = 10
scale = 1000

import utils.timing
utils.timing.table_timing([1000, 10000], count, scale)
utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale)