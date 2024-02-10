#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Direct approach

NOTE: most time is spent in the removal of all possible sums - replacing utils.factor with utils.fastfactor makes no difference, and neither does memoization.
'''

import utils.factor as factor
import itertools

def abundant(x):
    return((factor.sumDivisors(x) - x) > x)

for i in range(1, 12):
    assert not abundant(i)

assert abundant(12)
assert not abundant(13)
assert not abundant(14)
assert not abundant(15)
assert not abundant(16)
assert not abundant(17)
assert abundant(18)
assert not abundant(19)
assert abundant(20)
assert not abundant(21)
assert not abundant(22)
assert not abundant(23)
assert abundant(24)
assert not abundant(25)
assert abundant(30)

def solution(limit):
    abundants = (x for x in range(12, limit + 1) if abundant(x))
    return sum({x for x in range(1, limit + 1)} - {sum(y) for y in itertools.combinations_with_replacement(abundants, 2)})

# all numbers less than 24 are not sums of abundant numbers, as smallest abundant number is 12, and smallest sum of abundants is 24
for i in range(1, 24):
    assert solution(i) == sum(x for x in range(i + 1))

# 24 is first sum of abundants, and thus would not be included in the solution
assert solution(24) == sum(x for x in range(25)) - sum([24])

# next abundant number is 18, so next possible sum is 12 + 18 = 30
assert solution(30) == sum(x for x in range(31)) - sum([24, 30])

print(solution(28123))

count = 1
scale = 1

import utils.timing
utils.timing.table_timing([24, 28123], count, scale)
utils.timing.plot_timing([1000, 4000, 7000, 10000, 13000, 16000, 19000, 22000, 25000, 28123], count, scale, "prob0023.01")